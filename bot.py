#imports
import os
import discord
import asyncio
from discord import voice_client
from dotenv import load_dotenv
import youtube_dl

#grabbing commands
from discord.ext import commands
#bring in environment file
load_dotenv()
#setting tokens
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
client = discord.Client(intents=intents)

#setting bot
bot = commands.Bot(command_prefix = '!', intents=intents)

playlist = []

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options={
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def _init_(self, source, *, data, volume = 0.5):
        super()._init_(source,volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    
    @classmethod
    async def from_url(cls,url,*,loop=None, stream = False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=True))

        if 'entries' in data:
            data = data['entries'][0]
            
        file = data['url'] if stream else ytdl.prepare_filename(data)
        filename = data['title']
        return file, filename



@bot.command(name='leave', help = 'To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command("play", help = 'Plays whatever url is put next to it.')
async def play(ctx,url):
    # Checking to see if the user is in the voice channel
    if not ctx.message.author.voice:
        # USER Not in voice channel
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    elif not ctx.message.guild.voice_client:
        # User is in channel
        #  Gets the channel
        channel = ctx.message.author.voice.channel
    # Connects to voice channel
        await channel.connect()
        
    # Trys to play a song
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            file, filename = await YTDLSource.from_url(url, loop=bot.loop, stream=False)
            playlist.append(file)
            #for elements in playlist:
            voice_channel.play(discord.FFmpegPCMAudio(executable="C:/Users/Alex/Desktop/Code Projects/Discord-Code/Personal/ffmpeg/bin/ffmpeg.exe", source=file))
        await ctx.send("Now Playing: {}".format(filename))
    # If anyyyy failures, results in this
    except:
        await ctx.send("The bot is not connected to a voice channel.")
        print('Not connected.')
        
        

@bot.command("pause", help = 'Pauses current song')
async def pause(ctx):
    voice_client=ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.command("resume", help = 'Resumes current song.')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use !play.")

@bot.command("stop", help = 'Stops current song. Will not be able to resume.')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if str(channel) == 'general':
                await channel.send('I have awakened!')
                await channel.send(file=discord.File('C:/Users/Alex/Desktop/Code Projects/Discord-Code/Personal/dog.gif'))

bot.run(TOKEN)
import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __int__(self, client):
      self.client = client

@commands.command()
async def join(self,ctx):
  if ctx.author.voice is None:
     await ctx.send("you're not in a voice channel")
     voice_channel = ctx.author.voice.channel
     if ctx.voice_client is None:
       await voice_channel.connect ()
       else:
         await ctx.voice_client.move_to(voice_channel)
         
  @commands.command()
async def disconnect(self,ctx):
await ctx.voice_client.disconnect()

@commands.command()
async def play (self,ctx,url):
   ctx.voice_client.stop()
   FFMPEG_OPTIONS = {'before_options':'-reconnect 1  -reconnect_streamed 1 -reconnect_delay_max 5', 'option': '-vn'}
YDL_OPTION = {'format':"bestaudio"}
vc = ctx.voice_client

with youtube_dl.YOUTUBEDL(YDL_OPTION) as ydl:
  info = ydl..extract_info(url, download=Flase)
  url2 = info['formats'][0]['url']
  source = await discord.FFmpeg0pusAudio.from_probe(url2**FFMPEG_OPTIONS)
  vc.play(source)

   @commands.command()
async def pause(self,ctx):
await ctx.voice_client.pause()
await ctx.send("paused :pause_button: ")

 @commands.command()
async def resume(self,ctx):
await ctx.voice_client.resume()
await ctx.send("resume :play_pause:  ")




def setup(client):
  client.add_cog(music(client))      

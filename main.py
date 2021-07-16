import os

from discord import channel
import dictionary
import discord
from asyncio import sleep

TOKEN = 'NzM1MTk1MjE4OTM2MzMyMzIw.Xxct5w.MSOBJi1POO_XtGOMcUhOQKtI68w'

class MyClient(discord.Client):

    async def on_ready(self):
        print('Username: {0.name}\nID: {0.id}'.format(self.user))

    async def on_message(self, message):
        if message.author.bot:
            return

        #channel = client.get_channel(int(VC_ID))


        if message.content in dictionary.dict:
            if message.guild.voice_client is not None:
                await message.channel.send("あなたはボイスチャンネルに接続していません。")
                return
                # ボイスチャンネルに接続する
            await message.author.voice.channel.connect()
            await message.delete()
            mp3 = dictionary.dict.get(message.content)
            message.guild.voice_client.play(discord.FFmpegPCMAudio(mp3))
            while  message.guild.voice_client.is_playing():
                await sleep(1)
            await  message.guild.voice_client.disconnect()

        if message.content == '?stop':
            if message.guild.voice_client is not None:
                message.guild.voice_client.stop()
                await message.guild.voice_client.disconnect()
            await message.delete()

client = MyClient()

if TOKEN is None :
    print('環境変数が適切に設定されていません')
else:
    client.run(TOKEN)

import discord
from discord.ext import commands
import json
import os

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>',intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    embed=discord.Embed(description=f'**{extension}** 載入成功',color=0x00ff62)
    embed.set_author(name="🛑 系統通知 🛑")
    await ctx.send(embed=embed)

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    embed=discord.Embed(description=f'**{extension}** 移除成功',color=0x00ff62)
    embed.set_author(name="🛑 系統通知 🛑")
    await ctx.send(embed=embed)
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    embed=discord.Embed(description=f'重載 **{extension}** 成功!',color=0x00ff62)
    embed.set_author(name="🛑 系統通知 🛑")
    await ctx.send(embed=embed)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN']) 
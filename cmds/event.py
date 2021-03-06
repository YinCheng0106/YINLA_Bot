from code import interact
from random import random
import discord
from discord.ext import commands
from core.classes import Cog_EX
from cmds.bank import Bank
from cmds.money import Money
from cmds.main import Main
import json
import asyncio
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Event(Cog_EX):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        embed=discord.Embed(title=f'â¨ â **{member}** å å¥!', color=0xff8800, timestamp = datetime.datetime.now())
        embed.set_author(name="ð æå¡å å¥éç¥ ð")
        await channel.send(member.mention , embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['CHANNEL']))
        embed=discord.Embed(title=f'ð¢ â **{member}** é¢éäº...', color=0xff8800, timestamp = datetime.datetime.now())
        embed.set_author(name="ð æå¡é¢ééç¥ ð")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author != self.bot.user:
            return
        if msg.content == 'å®å®' :
            await msg.channel.send('å¨')
        elif msg.content == 'test':
            await msg.channel.send('<@&801115250165940244>') # @USER ==> '<@ä½¿ç¨èID>' #@ROLE ==> '<@&èº«åçµID>'
        elif msg.content == 'æ©ä¸å¥½' :
            await msg.channel.send('ä¸­å\næç¾å¨æå°æ·æ·')
        elif msg.content == 'æå®' :
            await msg.channel.send('å¯¶ï¼æå®!')
        elif msg.content == 'å©åç¦®æä»¥å¾' :
            await msg.channel.send('éåº¦èæ¿æ9 ~')
        elif msg.content == 'æ©å®' :
            await msg.channel.send('æ¿éµ\nå¼æ!')
        elif msg.content == 'æå¥½å¸¥å':
            await msg.delete()
            await msg.channel.send('ä¸å¥½ææï¼ä¸è¦é¨äººå¦')
        elif msg.content == 'æå¥½å¸¥':
            await msg.delete()
            await msg.channel.send('ä¸å¥½ææï¼ä¸è¦é¨äººå¦')
        elif msg.content == 'æ¨çå¥½æ¼äº®':
            await msg.delete()
            await msg.channel.send('å!ï¼ä½ å¤ªèª å¯¦äºå¦ð')
        elif msg.content == 'æ¨çå¥½ç¾':
            await msg.delete()
            await msg.channel.send('å!ï¼ä½ å¤ªèª å¯¦äºå¦ð')
    

    #ERROR HANDLER
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=2727
        if hasattr(ctx.command,'on_error'):
            return

        if isinstance(error,commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title=" ââ æä»¤ä¸å®æ´æé¯èª¤ï¼è«éæ°è¼¸å¥\nè¼¸å¥ `>command` æ¥è©¢ç¾ææä»¤", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="â ï¸ ç¼çé¯èª¤ â ï¸")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.CommandNotFound):
            embed=discord.Embed(title=" ââ ç¡æ­¤æä»¤\nè¼¸å¥ `>command` æ¥è©¢ç¾ææä»¤", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="â ï¸ ç¼çé¯èª¤ â ï¸")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=" ð â è«éå ± **ç®¡çå¡** ä¿®å¾©",color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="â ï¸ ç¼çæªç¥é¯èª¤ â ï¸")
            await ctx.send(embed=embed)
            print(error)

    
    # https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=1748
    #åå¥é¯èª¤èç
    @Bank.lm.error
    async def lm_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            msg = await ctx.send("èª°?")
            await asyncio.sleep(3)
            await ctx.message.delete()
            await msg.delete()
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title=" ââ æä»¤ä¸å®æ´æé¯èª¤ï¼è«éæ°è¼¸å¥\nè¼¸å¥ `>command` æ¥è©¢ç¾ææä»¤", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="â ï¸ ç¼çé¯èª¤ â ï¸")
            await ctx.send(embed = embed)

    @Money.daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
            cd = int(error.retry_after)
            H = int(cd / 3600)
            M = (int(cd / 60)- H*60)
            S = int(cd % 60)
            em = discord.Embed(title=f"â â å·²ç°½å°\nå·å»æé `{H}` H `{int(M)}` M `{int(S)}`S .", color=0xff0000, timestamp = datetime.datetime.now())
            em.set_author(name="â ï¸ å·å»æé â ï¸")
            await ctx.send(embed=em)
        else:
            pass

    @Main.avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            #a = "ð¤ | æä¸èªè­éåäººå§..."
            #b = "ð¤ | ä»æ¯èª°?"
            #title = random.choice([a,b])
            embed = discord.Embed(
                title = "ð¤ | æä¸èªè­éåäººå§...",
                color = 0xff0000
            )
            await ctx.reply(embed = embed)
        else:
            pass

    @Main.profile.error
    async def profile_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            #a = "ð¤ | æä¸èªè­éåäººå§..."
            #b = "ð¤ | ä»æ¯èª°?"
            #title = random.choice([a,b])
            embed = discord.Embed(
                title = "ð¤ | æä¸èªè­éåäººå§...",
                color = 0xff0000
            )
            await ctx.reply(embed = embed)
        else:
            pass

    #æ°å¢åæç²å¾èº«åçµ
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id ==974926070451150899:
            if str(payload.emoji) == '<:emoji_1:801114598408192044>':
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(974906252079550505)
                await payload.member.add_roles(role)
                embed=discord.Embed(title=f"â â å·²æ°å¢ {role} èº«åçµ",color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="ð« èº«åçµé åéç¥ ð«")
                await payload.member.send(embed = embed)

    #ç§»é¤åæç²å¾èº«åçµ
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id ==974926070451150899:
            if str(payload.emoji) == '<:emoji_1:801114598408192044>':
                guild = self.bot.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                role = guild.get_role(974906252079550505)
                await user.remove_roles(role)
                embed=discord.Embed(title=f"â â å·²ç§»é¤ {role} èº«åçµ",color=0xff0000, timestamp = datetime.datetime.now())
                embed.set_author(name="ð« èº«åçµç§»é¤éç¥ ð«")
                await user.send(embed = embed)
    
    #å¯©æ ¸æ¥èª è¨æ¯åªé¤ç´é
#    @commands.Cog.listener()
#    async def on_message_delete(self, msg):
#        counter = 1
#        async for audilog in msg.guild.audit_logs(action = discord.AuditLogAction.message_delete):
#            if counter == 1:
#                await msg.channel.send("åªé¤è¨æ¯è:" + audilog.user.name)
#                counter += 1
#        await msg.channel.send("å·²åªé¤è¨æ¯ï¼" + str(msg.content))
#        await msg.channel.send("è¨æ¯åªé¤èï¼" + str(msg.author))


def setup(bot):
    bot.add_cog(Event(bot))
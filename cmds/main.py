import datetime
import discord
from discord.ui import Button, View
from discord.ext import commands
from core.classes import Cog_EX
import asyncio
import random

class Main(Cog_EX):

    @commands.command()
    async def ping(self, ctx):
        # ζι # https://youtu.be/kNUuYEWGOxA
        button1 = Button(label = "ζ΄ζ°", style = discord.ButtonStyle.green, emoji = "π")

        async def button_callback(interaction):
            embed2=discord.Embed(title =f'ε»Άι² `{round(self.bot.latency*1000)}` ms', color = 0x1eff00, timestamp = datetime.datetime.now())
            embed2.set_author(name = "π€ ζ©ε¨δΊΊηζ π€")
            msg = await interaction.response.edit_message(embed = embed2, view = view)

        button1.callback = button_callback
        

        view = View()
        view.add_item(button1)
        

        embed=discord.Embed(title =f'ε»Άι² `{round(self.bot.latency*1000)}` ms', color = 0x1eff00, timestamp = datetime.datetime.now())
        embed.set_author(name = "π€ ζ©ε¨δΊΊηζ π€")

        msg = await ctx.reply(mention_author = False, embed = embed, view = view)


    @commands.command()
    async def timer(self, ctx, seconds):

        secondint = int(seconds)
        await ctx.message.delete()
        if secondint > 600:
            embed=discord.Embed(title="ζη‘ζ³θ¨ζι£ιΊΌδΉ...(ζε€ 600 η§)", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="π η³»η΅±ιη₯ π")
            msg = await ctx.send(embed = embed)
            await ctx.message.delete()
            await asyncio.sleep(3)
            await msg.delete()

        if secondint <= 0:
            embed=discord.Embed(title="ζθ¨...ζιζ²ζθ² η", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="π η³»η΅±ιη₯ π")
            msg = await ctx.send(embed = embed)
            await ctx.message.delete()
            await asyncio.sleep(3)
            await msg.delete()
        embed = discord.Embed(title=f"ε©ι€ζιοΌ`{seconds}`", color= 0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="β±οΈ θ¨ζε¨ β±οΈ")
        message = await ctx.send(embed = embed)
            
        while True:
            secondint -= 1
            
            embed2 = discord.Embed(title=f"ε©ι€ζιοΌ`{secondint}`", color=0xff0000, timestamp = datetime.datetime.now())
            embed2.set_author(name="β±οΈ θ¨ζε¨ β±οΈ")
            msg = await message.edit(embed = embed2)

            if secondint == 0:
                break
            await asyncio.sleep(1)
        
        embed3 = discord.Embed(
            title = f"δ½ ζιε°δΊ!!\n δ½ ζθ¨­ε?ηζιηΊ `{seconds}`",
            color = 0xff0000,
            timestamp = datetime.datetime.now()
            )
        await ctx.send(ctx.author.mention, embed = embed3)
        
        await msg.delete()


    @commands.command()
    async def avatar(self, ctx, user : discord.Member):
        embed = discord.Embed(
            title = f"{user.name} ηι ­ε",
            color = user.color,
            timestamp = datetime.datetime.now()
        )
        embed.set_image(url = user.avatar)
        await ctx.reply(mention_author = False, embed = embed)


    @commands.command()
    async def profile(self, ctx, user : discord.Member):
        embed = discord.Embed(
            title = user.name,
            color = user.color,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = user.avatar)
        embed.set_author(name = "εδΊΊζͺζ‘", icon_url = user.avatar)
        embed.add_field(name = "ζ±η¨±", value = user.nick)
        embed.add_field(name = "ηζ", value = user.status, inline = False)
        embed.add_field(name = "ε»Ίη«εΈ³θζι", value = f"<t:{int(user.created_at.timestamp())}:f>\n<t:{int(user.created_at.timestamp())}:R>",inline = False)
        embed.add_field(name = "ε ε₯δΌΊζζι", value = f"<t:{int(user.joined_at.timestamp())}:f>\n<t:{int(user.joined_at.timestamp())}:R>")
        embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.reply(mention_author = False, embed = embed)
    
    @commands.command()
    async def sp(self, ctx):
        embed = discord.Embed(
            title = ctx.message.guild.name,
            color = 0x0000ff,
            timestamp = datetime.datetime.now()
        )
        embed.set_thumbnail(url = ctx.message.guild.icon )
        #embed.add_field(name = "ε»Ίη«δΌΊζζι", value = f"<t:{int(ctx.message.guild.created_at.timestamp())}:f>\n<t:{int(ctx.message.guild.created_at.timestamp())}:R>")
        embed.add_field(name = "δΌΊζε¨ζζθ", value = f"<@{ctx.message.guild.owner_id}>")
        #embed.add_field(name = "δΌΊζδΈ»θ¦θͺθ¨", value = " ")
        #embed.add_field(name = "ζε­ι »ιζΈι", value = f"`{len(ctx.message.guilds.text_channels)}` ε")
        #embed.add_field(name = "θͺι³ι »ιζΈι", value = f"`{len(ctx.message.guilds.voice_channels)}` ε")
        embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.reply(mention_author = False, embed = embed)

    @commands.command()
    async def nt(self, ctx):
    
        today = datetime.datetime.now()
        dt = today.strftime(" ``%m`` / ``%d`` / ``%Y``"+" "+"``%H`` : ``%M`` : ``%S``")
        embed = discord.Embed(title= dt , color=0xff0000)
        embed.set_author(name="π°οΈ ηΎε¨ζι π°οΈ")
        
        time = await ctx.send(embed = embed)
        await ctx.message.delete()
        await asyncio.sleep(10)
        await time.delete()
        
            


    @commands.command()
    async def ζ³‘ιΊ΅(self, ctx):
#        button2 = Button(label = "ε?ζ", style = discord.ButtonStyle.green, emoji = "π½οΈ")
        secondint = 180

#        async def button_callback(interaction):
#            await interaction.response.delete_message()

#        button2.callback = button_callback

#        view = View()
#        view.add_item(button2)

        embed = discord.Embed(title=f"ε©ι€ζι : `{secondint}`", color=0xff0000, timestamp = datetime.datetime.now())
        embed.set_author(name="β±οΈ ζ³‘ιΊ΅θ¨ζε¨ β±οΈ")
        message = await ctx.send(embed = embed)
            
        while True:
            secondint -= 1
            if secondint == 0:
                break

            embed2 = discord.Embed(title=f"ε©ι€ζι : `{secondint}`", color=0xff0000, timestamp = datetime.datetime.now())
            embed2.set_author(name="β±οΈ ζ³‘ιΊ΅θ¨ζε¨ β±οΈ")

            msg = await message.edit(embed = embed2)
            await asyncio.sleep(1)
        fin = await ctx.send(f"{ctx.author.mention} δ½ ζ³‘ιΊ΅ε―δ»₯εδΊ!!" )
        await ctx.message.delete()
        await msg.delete()
        await asyncio.sleep(60)
        await fin.delete()
    

    @commands.command()
    async def say(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)


    @commands.command()
    async def clean(self, ctx, num:int):
        if num <= 1:
            embed=discord.Embed(title=" ββ θ¨ζ―ζΈιεΏι ηΊ `ζ­£εΌ`\nθΌΈε₯ `>command` ζ₯θ©’ηΎζζδ»€", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="β οΈ ηΌηι―θͺ€ β οΈ")
            embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
            msg = await ctx.send(embed = embed)
            await asyncio.sleep(3)
            await ctx.message.delete()
            await asyncio.sleep(2)
            await msg.delete()
        else:
            await ctx.channel.purge(limit=num+1)
            embed=discord.Embed(title=f"ε·²εͺι€ `{num}` εθ¨ζ―", color=0xff0000, timestamp = datetime.datetime.now())
            embed.set_author(name="π η³»η΅±ιη₯ π")
            embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await msg.delete()


    @commands.command()
    async def command(self, ctx):
        embed=discord.Embed(title="π β ζδ»€ε°ε", color=0xfbff00, timestamp = datetime.datetime.now())
        
        embed.add_field(name=">ζ³‘ιΊ΅", value="η?ζ³‘ιΊ΅ζεΉ«δ½ θ¨ζ(180η§)", inline=True)
        embed.add_field(name=">timer [η§ζΈ]", value="θ¨ζε¨(η§)", inline=True)
        embed.add_field(name=">nt", value="ηΎε¨ζι", inline=True)
        embed.add_field(name=">say [ε§ε?Ή]", value="θ?ζ©ε¨δΊΊθͺͺθ©±", inline=True)
        embed.add_field(name=">daily", value="η°½ε° (ε€©)", inline=True)
        embed.add_field(name=">m", value="ζ₯θ©’ι’ε", inline=True)
        embed.add_field(name=">lm [@mention]", value="ζ₯θ©’εΆδ»η¨ζΆηι’ε", inline=True)
        embed.add_field(name=">withdraw [ιι‘]", value="ζζ¬Ύ", inline=True)
        embed.add_field(name=">deposit [ιι‘]", value="ε­ζ¬Ύ", inline=True)
        embed.add_field(name=">send [@mention] [ιι‘]", value="θ½εΈ³", inline=True)
        embed.add_field(name=">abb", value="1A2B", inline=True)
        embed.add_field(name=">slots [ζΌι] [εη]", value="ζιΈζ©", inline=True)
        embed.add_field(name=">guess", value="η΅ζ₯΅ε―η’Ό", inline=True)

        embed.add_field(name=">clean [ζΈι]", value="ζΈι€θ¨ζ―", inline=False)
        embed.add_field(name=">avatar", value="η¨ζΆι ­θ²Όζεεθ½", inline=True)
        embed.add_field(name=">profile", value="η¨ζΆεδΊΊη°‘δ»", inline=True)
        embed.add_field(name=">sp", value="δΌΊζε¨η°‘δ»", inline=True)
        embed.add_field(name=">ping", value="ζͺ’θ¦ζ©ε¨δΊΊε»Άι²", inline=False)
        embed.add_field(name=">info", value="ζͺ’θ¦ζ©ε¨δΊΊθ³θ¨", inline=False)
        embed.add_field(name=">yin", value="ζͺ’θ¦ζ©ε¨δΊΊε΅δ½θθ³θ¨", inline=False)
        embed.set_footer(text = "YINLA", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="ζ©ε¨δΊΊθ³θ¨", color=0x16a5fe, timestamp = datetime.datetime.now())
        embed.set_author(name="YINLA", url="https://discord.gg/We6enK7wb3", icon_url="https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        embed.add_field(name="π β θͺηζ₯ζ", value="`2022/02/09`", inline=True)
        embed.add_field(name="π β ζ­£εΌεη¨", value="`????/??/??`", inline=True)
        embed.add_field(name="π₯οΈ β η¨εΌ", value="`PYTHON`", inline=True)
        embed.add_field(name="π β ζδ»€", value="`>`", inline=True)
        embed.set_footer(text = "YINLA | YinCheng#8104 θ£½", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def yin(self, ctx):
        embed=discord.Embed(title="ζ©ε¨δΊΊε΅δ½θθ³θ¨", color=0xffffff, timestamp = datetime.datetime.now())
        embed.set_author(name="Yin Cheng", url="https://allmy.bio/yincheng", icon_url="https://avatars.githubusercontent.com/u/99303523?v=4" )
        embed.add_field(name="IG", value="\_yincheng\_", inline=False)
        embed.add_field(name="Discord", value="YinCheng#8104", inline=True)
        embed.add_field(name="Twitter", value="@Yin_Cheng0106", inline=False)
        embed.add_field(name="Twitch", value="θ€ε¦(yincheng0106)", inline=True)
        embed.set_footer(text = "YINLA | YinCheng#8104 θ£½", icon_url= "https://cdn.discordapp.com/avatars/940778743637606451/d8771ac9d0903242122e6bb89161f071.png")
        await ctx.send(embed=embed)



#    @commands.command()
#    async def test(self, ctx):
#        embed = discord.Embed(title = f"real time embed test", color = discord.Color.green())
#        embed.add_field(name = 'Test', value = 'Hello this is a test')

#        update = await ctx.send(embed = embed)

#        new_em = discord.Embed(title = f"real time embed test", color = discord.Color.green())
#        new_em.add_field(name = 'Test', value = 'This text has changed')
#        update = await ctx.send(embed = new_em)
#        await update.edit(embed= new_em)

def setup(bot):
    bot.add_cog(Main(bot))
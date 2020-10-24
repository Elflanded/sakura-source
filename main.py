import discord
from discord.ext import commands, tasks
import os
import B
import time
from itertools import cycle
import praw
import random
import aiohttp
import json
from discord.utils import get

key=os.getenv('key')

wkey=os.getenv('wkey')

status = cycle(['-help', 'version | 0.0.5', 'By: Elflanded#0001'])



client = discord.Client()

client = commands.Bot(command_prefix = '-')
client.remove_command('help')



@client.command()
@commands.has_permissions(kick_members=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def kick(ctx, user : discord.Member,*,reason):
    await user.kick(reason=reason)
    embed = discord.Embed(title="Kick", description=f'{user} kicked for {reason}', color=0xE75480)
    await ctx.send(embed=embed) 

@client.command()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def ban(ctx, user : discord.Member,*,reason):
    await user.ban(reason=reason)
    embed = discord.Embed(title="Ban", description=f'{user} was struck by the ban hammer {reason}', color=0xE75480)
    await ctx.send(embed=embed) 



@client.command()
async def support(ctx):
  await ctx.send('Support server: discord.gg/sDaP9NU')


  

@client.event
async def on_command_error(ctx, error):
  await ctx.send(f'An error has occured, if you think this is a mistake, try `-support` ```Console Log: {error}```')
  
@tasks.loop(seconds=2)
async def change_status():
   await client.change_presence(activity=discord.Game(next(status)))


@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(title="Help", description="Prefix: -", color=0xE75480) 
    
    embed.set_thumbnail(url="https://images.unsplash.com/photo-1554298819-74ec8c6acac6?ixlib=rb-1.2.1&w=1000&q=80")

    embed.add_field(name="Moderation", value="Displays moderation commands.", inline=False)

    embed.add_field(name="Reddit", value="Displays reddit commands.", inline=False)

    embed.add_field(name="Utility", value="Displays utility commands.", inline=False)
    
    
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
@commands.cooldown(1, 7, commands.BucketType.user)
async def moderation(ctx):
    embed = discord.Embed(title="Help-Moderation", description="Help Menu for Moderation", color=0xE75480)
    
    
    

    embed.add_field(name="Kick", value="Kicks a user from the server.")

    embed.add_field(name="Ban", value="Bans a user from the server.")
    
    
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def reddit(ctx):
    embed = discord.Embed(title="Help-Reddit", description="Help Menu for Reddit", color=0xE75480)
    
    
    

    embed.add_field(name="Meme", value="Sends a post from r/dankmemes.")

    embed.add_field(name="Minecraft", value="Sends a post from r/minecraft.")

    embed.add_field(name="Memes", value="Sends a post from r/memes.")
    
    
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def utility(ctx):
    embed = discord.Embed(title="Help-Utility", description="Help Menu for Utility", color=0xE75480)
    
    
    

    embed.add_field(name="support", value="Sends an invite to the support server.")

    
    
    await ctx.send(embed=embed)

@client.command(aliases=['memes1'])
async def meme(ctx):
    embed = discord.Embed(title="r/Dankmemes", description=None, color=0xE75480)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed, content=None)


@client.command(aliases=['mc'])
async def minecraft(ctx):
    embed = discord.Embed(title="r/Minecraft", description=None, color=0xE75480)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/minecraft/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed, content=None)

@client.command(aliases=['me'])
async def memes(ctx):
    embed = discord.Embed(title="r/Memes", description=None, color=0xE75480)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed, content=None)


@client.command(aliases=['funny2'])
async def funny(ctx):
    embed = discord.Embed(title="r/Funny", description=None, color=0xE75480)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/funny/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed, content=None)




  
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    embed = discord.Embed(title="Role Granted", description=f'{user.mention} was given {role.mention} by {ctx.author.mention}', color=0x90c4ff)
    await ctx.send(embed=embed) 



@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member = None, *, reason):
    guild = ctx.guild
    if not get(ctx.guild.roles, name="Muted"):  # Create muted role if it does not exist.
        role_perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=role_perms)
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(muted_role, reason=reason)


    embed = discord.Embed(title="Mute", description=f'{member.mention} was muted by {ctx.author.mention} for {reason}', color=0xE75480)
    await ctx.send(embed=embed) 
  
@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member = None, *, reason):
    guild = ctx.guild
    if not get(ctx.guild.roles, name="Muted"):  # Create muted role if it does not exist.
        role_perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=role_perms)
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role, reason=reason)


    embed = discord.Embed(title="Unmute", description=f'{member.mention} was unmuted by {ctx.author.mention} for {reason}', color=0xE75480)
    await ctx.send(embed=embed) 



with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx,user:discord.User,*reason:str):
  if not reason:
    await ctx.send("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
     await ctx.send(f"{user.name} has never been reported")  

    

B.b()
client.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands, tasks
import os
import B
import time
key=os.getenv('key')

wkey=os.getenv('wkey')



client = discord.Client()

client = commands.Bot(command_prefix = '-')
client.remove_command('help')



@client.command()
@commands.has_permissions(kick_members=True)
@commands.cooldown(1, 7, commands.BucketType.user)
async def kick(ctx, user : discord.Member,*,reason):
    await user.kick(reason=reason)
    embed = discord.Embed(title="Kick", description=f'{user} kicked for {reason}', color=0xE75480)
    await ctx.send(embed=embed) 

@client.command()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 7, commands.BucketType.user)
async def ban(ctx, user : discord.Member,*,reason):
    await user.ban(reason=reason)
    embed = discord.Embed(title="Ban", description=f'{user} was struck by the ban hammer {reason}', color=0xE75480)
    await ctx.send(embed=embed) 



@client.event
async def on_command_error(ctx, error):
  await ctx.send(f'An error has occured, if you think this is a mistake, try `-support` ```Console Log: {error}```')
  


@client.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(title="Help", description="Help Menu", color=0xE75480)
    
    
    embed.add_field(name="Help", value="Displays this menu.")

    embed.add_field(name="Kick", value="Kicks a user from the server.")

    embed.add_field(name="Ban", value="Bans a user from the server.")
    
    
    await ctx.send(embed=embed)


B.b()
client.run(os.getenv('TOKEN'))

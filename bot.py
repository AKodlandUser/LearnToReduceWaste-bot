import discord
from discord.ext import commands

description = '''In this bot, you can learn 
how to classify where you throw all your waste. The downside, 
this information is only useful in Spain.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def how(ctx):
    await ctx.send(f'You have to write using ?.\n?yellow gives you information on the yellow bin.\n?blue gives you information on the blue bin.\n?brown gives you information on the brown bin.\n?green gives you information on the green bin.\n?gray gives you information on the gray bin.')

@bot.command()
async def yellow(ctx):
    with open('M2L2\images\conetenedoramarillo.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(f'On the yellow bin, you have to throw plastics, cans and milk cartons.', file=picture)

@bot.command()
async def blue(ctx):
    with open('M2L2\images\contenedorazul.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(f'On the blue bin, you have to throw cartboard and paper.', file=picture)

@bot.command()
async def brown(ctx):
    with open('M2L2\images\contenedormarron.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(f'On the brown bin, you have to throw any sorts of organic waste, such as animal bones, leftover food, fruit peel, and baby diapers.', file=picture)

@bot.command()
async def green(ctx):
    with open('M2L2\images\contenedorverde.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(f'On the green bin, you have to throw any type of glass waste, such as glass bottles or glass cups.', file=picture)

@bot.command()
async def gray(ctx):
    with open('M2L2\images\contenedorgris.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(f'On the gray bin, you have to throw any other type of waste not mentioned on the explanaitions for the other bins, such as baby pacifiers, or used napkins.', file=picture)


bot.run('Add your token.')

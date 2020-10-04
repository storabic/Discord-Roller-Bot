import discord
from discord.ext import commands
from config import settings
import random

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def roll(ctx, arg):
    author = ctx.message.author
    random.seed()
    help_str = 'Введите натуральное число n, чтобы получить случайное число от 1 до n\nВведите два целых числа n m, чтобы получить случайное число от n до m'
    try:
        if(len(arg) > 100):
            await ctx.send(help_str)
            return
        x = list(map(int, arg.split(' ')))
        if (len(x) == 1):
            ans = random.randint(1, x[0])
        else:
            ans = random.randint(x[0], x[1])
        await ctx.send(f'{author.mention} рольнул {ans}')
    except:
        await ctx.send(help_str)
bot.run(settings['token'])

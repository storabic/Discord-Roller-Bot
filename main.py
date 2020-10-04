import discord
import random
from discord.ext import commands
token = 'YOURTOKEN'
bot = commands.Bot(command_prefix = '!')
@bot.command(pass_context=True)
async def roll(ctx, arg):
    random.seed()
    ans = 'Введите натуральное число n, чтобы получить случайное число от 1 до n\nВведите два целых числа n m, чтобы получить случайное число от n до m'
    try:
        x = list(map(int, arg.split(' ')))
        if (len(x) == 1):
            ans = random.randint(1, x[0])
        else:
            ans = random.randint(x[0], x[1])
    except:
        pass
    await ctx.send(ans)
bot.run(token)

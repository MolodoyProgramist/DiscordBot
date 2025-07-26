import discord 
from discord.ext import commands

url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

TOKEN = 'MTM5NjI1MDE0NjcxNDQxOTMwMQ.GqoHT3.tKmoWwCRn6R1IMOIIaJQZhPNAeFmx5N6MhC1z4'
PREFIX = '/'
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)  # <-- Здесь отключаем стандартную help

@bot.command()
async def hello(ctx):
    await ctx.reply(
        'Привет!\n'
        'Я — бот, созданный моим крутым разработчиком.'
        'Если хочешь помочь — просто скажи!'
        'Буду рад помочь тебе и сделать сервер лучше.'
        'Заходи, общайся, не стесняйся! 😉'
        )





@bot.command()
async def calculator(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.reply(f'Результат: {result}')
    except Exception as e:
        await ctx.reply(f'Ошибка: {e}')
    

bot.run(TOKEN)

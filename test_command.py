import discord
from discord import app_commands
from discord.ext import commands

# Создаем бот с использованием команды prefix и слэш-команды
class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Регистрация команд при запуске бота
        await self.tree.sync()

# Создаем инстанс бота
bot = MyBot(command_prefix="!", intents=discord.Intents.default())

#@bot.event
#async def on_ready():
#    print(f"Logged in as {bot.user}")

# Определение slash-команды
@bot.tree.command(name="hello", description="Says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, world!")

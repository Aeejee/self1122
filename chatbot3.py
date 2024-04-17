import discord
from discord.ext import commands
from colorama import Fore, Style
import asyncio  # Make sure to import asyncio

token = 'MTIxMjg5MDU4NjMxMTMwMzE4OA.G6dO0M.TBGVIfa08OotVr23QafljncLO5GLNjSibC3ylg'




blue = f'{Fore.BLUE}{Style.BRIGHT}'
end = f'{Fore.RESET}{Style.RESET_ALL}'
count = 0

forward_channel_id = 1213245888122847333

@bot.event
async def on_message(message: discord.Message):
    global count
    if message.guild.id == 1186719053197365349:
        if message.author.id == 1172042282996867155:
            if message.content:
                channel = bot.get_channel(forward_channel_id)
                async with channel.typing():  # Start typing simulation
                    await asyncio.sleep(1)  # Simulate delay while typing
                # Typing stops when the block ends
                await channel.send(message.content)  # Send message after typing simulation
                count += 1
                print(f"{blue}Forwarded message #{count} this session{end}")
    await bot.process_commands(message)

bot.run(token)

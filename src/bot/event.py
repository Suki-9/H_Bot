import discord
from bot import client, tree
from modules import logger, config
from typing import List

SENSITIVE_WORDS: List[str] = config.get('SENSITIVE_WORDS')

@client.event
async def on_ready():
  logger.info('h-bot.event', 'on_ready')
  await tree.sync()

@client.event
async def on_message(message):
  if message.author.bot:
      return

  logger.info('h-bot.event', 'on_message')

  text = message.content

  for word in SENSITIVE_WORDS:
    if word in text:
      await message.reply('えっちなのはダメッ！死刑')
      return
  
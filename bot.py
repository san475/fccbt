#!/usr/bin/python3

import discord
import asyncio
from discord.ext.commands import Bot

import signal
import sys
import ast

#groupFile = open('groups.txt', 'r+')
client = discord.Client()
#ctxclient = Bot(description="My Cool Bot", command_prefix="!", pm_help = False, )

def main():
	client.run('NzIwODQxNzY5ODA1MjgzMzYw.XuL3cw.X2IEBRx-EIYjsNl7zZiEqJHvNZo')

#@ctxclient.command(pass_context=True)
#async def whoami(ctx):
	#if ctx.message.author.server_permissions.administrator:
		#msg = "You're an admin {0.author.mention}".format(ctx.message)  
		#await client.send_message(ctx.message.channel, msg)
	#else:
		#msg = "You're an average joe {0.author.mention}".format(ctx.message)  
		#await client.send_message(ctx.message.channel, msg)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	#if str(message.author) == 'radicalfeel#7389':
	#await message.edit(content=message.content + " :alexislife:")
	#await message.channel.send('fuck you alexis')
	#if str(message.author) == 'san475#3138':
		#await message.channel.send("/tts The king has spoken")
	#await message.edit(content=message.content + " :jordanmoon:")

	if message.content.startswith('$hello'):
		await message.channel.send('Hello')
	if message.content.startswith('$jordanxplode'):
		await message.channel.send('https://cdn.discordapp.com/attachments/678702504514551841/720849812068499456/video0.mov')
	if message.content.startswith('$groups'):
		await message.channel.send('Printing group dictionary')
		groupFile = open('groups.txt', 'r+')
		string = groupFile.read()
		if string:
			groupDict = ast.literal_eval(string)
			await message.channel.send(string)
		await message.channel.send(string)
		groupFile.close()

	if message.content.startswith('$addmeto'):
		group = message.content[8:]
		print('You are adding yourself to the group: ' + group)
		groupFile = open('groups.txt', 'r+')

		string = groupFile.read()
		groupFile.seek(0)

		groupDict = {}
		if(string):
			# convert: string -> dictionary
			groupDict = ast.literal_eval(string)
		if group in groupDict:
			groupDict[group].append(message.author.name)
		else:
			await message.channel.send('That group doesn\'t exist, contact an admin!')

		groupFile.write(str(groupDict))

		groupFile.truncate()
		groupFile.close()


	if message.content.startswith('$write'):
		logFile = open('log.txt', 'r+')
		logFile.write(message.content[6:])
		logFile.write(str(message.author.name))
		logFile.close()


def joinGroup(user, group):
	return




main()

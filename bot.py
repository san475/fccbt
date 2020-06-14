#!/usr/bin/python3

import discord
import asyncio
from discord.ext.commands import Bot

from time import sleep
import signal
import sys
import ast

#groupFile = open('groups.txt', 'r+')
client = discord.Client()
ctxclient = Bot(description="My Cool Bot", command_prefix="!", pm_help = False, )

def main():
	#client.run('NzIwODQxNzY5ODA1MjgzMzYw.XuUZoA.dhPiRyEGzPPVB3BdRModJuxjTsQ')
	ctxclient.run('NzIwODQxNzY5ODA1MjgzMzYw.XuWBlg.DVu3KWLETvEQTpWabaz5NnkCE0Q')

@ctxclient.event
async def on_ready():
	print('We have logged in as {0.user}'.format(ctxclient))


@ctxclient.command(pass_context=True)
async def whoami(ctx):
	#Get the roles for the server
	roles = ctxclient.guilds[0].roles
	msg = "You're an average joe {0.author.mention}".format(ctx.message) 

	#Loop roles and check if the user is in that role and the role is an admin
	for role in roles:
		if (role.permissions.administrator and ctx.message.author in role.members):
			msg = "You're an admin {0.author.mention}".format(ctx.message)  
			break

	#await ctxclient.send_message(ctx.message.channel, msg)
	await ctx.message.channel.send(msg)








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

	## ANOTHER ONE TO REFACTOR
	if message.content.startswith('$hello'):
		sleep(.5)
		await message.channel.send('Hello')
	if message.content.startswith('$jordanxplode'):
		await message.channel.send('https://cdn.discordapp.com/attachments/678702504514551841/720849812068499456/video0.mov')
	## ANOTHER ONE TO REFACTOR
	if message.content.startswith('$groups'):
		await message.channel.send('Printing group dictionary')
		groupFile = open('groups.txt', 'r+')
		string = groupFile.read()
		if string:
			groupDict = ast.literal_eval(string)
			await message.channel.send(str(groupDict))
		#await message.channel.send(string)
		groupFile.close()

	## ANOTHER ONE TO REFACTOR
	if message.content.startswith('$addgroup'):
		group = message.content[9:].strip()
		await message.channel.send('You are adding the group: ' + group)
		if message.author.name not in ['san475', 'Chronite', 'Castronaut', 'Tylope', 'Mako']:
			await message.channel.send('You\'re not in the white-list, bug off!')
		else:
			groupFile = open('groups.txt', 'r+')
			string = groupFile.read()
			groupFile.seek(0)

			groupDict = {}

			if(string):
# convert: string -> dictionary
				groupDict = ast.literal_eval(string)
			if group in groupDict:
				await message.channel.send('That group already exists...')
			else:
				groupDict[group] = []
				await message.channel.send('Congrats, you just created the group: ' + group + '!')

			groupFile.write(str(groupDict))

			groupFile.truncate()
			groupFile.close()

	## ANOTHER ONE TO REFACTOR
	if message.content.startswith('$addmeto'):
		group = message.content[8:].strip()
		await message.channel.send('You are adding yourself to the group: ' + group)

		groupFile = open('groups.txt', 'r+')
		string = groupFile.read()
		groupFile.seek(0)

		groupDict = {}

		if(string):
# convert: string -> dictionary
			groupDict = ast.literal_eval(string)
		if group not in groupDict:
			await message.channel.send('That group doesn\'t exist, contact an admin! <@260568153254395907>')
		elif message.author.name in groupDict[group]:
			await message.channel.send('You\'re already in the group ' + group + ' silly <:jordanmoon:720783841584742501>')
		else:
			groupDict[group].append(message.author.name)

		groupFile.write(str(groupDict))

		groupFile.truncate()
		groupFile.close()


	if message.content.startswith('$write'):
		logFile = open('log.txt', 'r+')
		logFile.write(message.content[6:])
		logFile.write('  :  ' + str(message.author.name))
		logFile.close()


def joinGroup(user, group):
	return




main()

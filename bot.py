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
	ctxclient.run('NzIwODQxNzY5ODA1MjgzMzYw.XuWVNw.Wz_EC0ADlMK6io3B1gEbA99KQyE')

@ctxclient.event
async def on_ready():
	print('We have logged in as {0.user}'.format(ctxclient))


#TODO DELETE
@ctxclient.command(pass_context=True)
async def roles(ctx):
	print (ctxclient.guilds[0].roles[::-1])


def isAdmin(user):
	#Get the roles for the server
	roles = ctxclient.guilds[0].roles[::-1]

	#Loop roles and check if the user is in that role and the role is an admin
	for role in roles:
		if (role.permissions.administrator and user in role.members):
			return True
	return False

@ctxclient.command()
async def whoami(ctx):
	msg = "You're an average joe {0.author.mention}".format(ctx.message) 

	if ctx.message.author.id == 257558209689026562:
		msg = 'fuck off alexis <:alexislife:720780743642578975>'
	elif isAdmin(ctx.message.author):
		msg = "You're an admin {0.author.mention}".format(ctx.message)  

	await ctx.message.channel.send(msg)


@ctxclient.command(case_insensitive=True) #TODO this doesnt work???
async def groupadd(ctx, group):
	#Append underscore to bot roles
	if not group.endswith('_'):
		group += '_'

	#Ensure that the user is an admin and the role does not already exist
	if isAdmin(ctx.message.author) and not any((x for x in ctxclient.guilds[0].roles if x.name == group)):
		newrole = await ctxclient.guilds[0].create_role(name=group)
		await ctx.message.channel.send('Created new role: ' + newrole.mention)
	else:
		await ctx.message.channel.send('You are not an admin or the group already exists!')




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

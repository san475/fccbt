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
	# get token from file
	# Make sure to have file with up-to-date token in it as token.txt
	tokenFile = open('token.txt', 'r')
	token = tokenFile.read()
	tokenFile.close()
	ctxclient.run(token)

@ctxclient.event
async def on_ready():
	print('We have logged in as {0.user}'.format(ctxclient))

#Returns true if the user is an admin
def isAdmin(user):
	#Get the roles for the server
	roles = ctxclient.guilds[0].roles[::-1]

	#Loop roles and check if the user is in that role and the role is an admin
	for role in roles:
		if (role.permissions.administrator and user in role.members):
			return True
	return False

#Returns true if the role exists in the server
def roleExists(role):
    return any((x for x in ctxclient.guilds[0].roles if x.name == role))

@ctxclient.command()
async def whoami(ctx):
	msg = "You're an average joe {0.author.mention}".format(ctx.message) 

	if ctx.message.author.id == 257558209689026562:
		msg = 'fuck off alexis <:alexislife:720780743642578975>'
	elif isAdmin(ctx.message.author):
		msg = "You're an admin {0.author.mention}".format(ctx.message)  

	await ctx.message.channel.send(msg)

@ctxclient.command(case_insensitive=True) #TODO this doesnt work???
async def groupdel(ctx, group):
	#Append underscore to bot roles
	if not group.endswith('_'):
		group += '_'
	#Ensure that the user is an admin and the role does already exist
	if isAdmin(ctx.message.author) and roleExists(group):
		#roleToDelete = await ctxclient.guilds[0].create_role(name=group)
		for role in ctxclient.guilds[0].roles:
			if role.name == group:
				await role.delete()
				await ctx.message.channel.send('The role was deleted.')
				return
	else:
		await ctx.message.channel.send('Either you\'re not an admin, or the group doesn\'t exist. I\'ll let you figure it out.. <:ryanhole:720781729387905052>')

@ctxclient.command(case_insensitive=True) #TODO this doesnt work???
async def groupadd(ctx, group):
	#Append underscore to bot roles
	if not group.endswith('_'):
		group += '_'
	#Ensure that the user is an admin and the role does not already exist
	if isAdmin(ctx.message.author) and not roleExists(group):
		newrole = await ctxclient.guilds[0].create_role(name=group)
		await ctx.message.channel.send('Created new role: ' + newrole.mention)
	else:
		await ctx.message.channel.send('You are not an admin or the group already exists!')


@ctxclient.command()
async def addmeto(ctx, group):
	#Append underscore to bot roles
	if not group.endswith('_'):
		group += '_'

	if not roleExists(group):
		await ctx.message.channel.send('That role does not exist! Contact an admin to add it or check your spelling :P')
	else:
		#Get the actual role object
		role = next((x for x in ctxclient.guilds[0].roles if x.name == group))
		await ctx.message.author.add_roles(role)
		await ctx.message.channel.send('You have been added to ' + group + '!')


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

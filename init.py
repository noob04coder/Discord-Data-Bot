# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

import discord
import time
import json

from gsheet import *

client = discord.Client()
sheet = gsheet()
user_data = json.loads(./config.json)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return    
    
    # Restrict the command to a channel
    # Change CHANNELID to a channel id or None
    CHANNELID = None  #in integer form

    if CHANNELID is not None and message.channel.id != CHANNELID and message.content.startswith('!s '):
        await message.channel.send(':x: Please send address in <#'+str(CHANNELID)+'> only')
        time.sleep(3)
        await message.channel.purge(limit=2)
        return
    
    # Restrict the command to a role
    # Change REQUIREDROLE to a role id or None 
    REQUIREDROLE = None  #in integer form

    if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=REQUIREDROLE) is None and message.content.startswith('!s '):
        await message.channel.send(':x: You don\'t have the required role!')
        time.sleep(3)
        await message.channel.purge(limit=2)
        return
                                                      
    # Command to insert data to excel
    
    if message.content.startswith('!s '):
      text = message.content[3:5:]
      slice_text=message.content[3:5:]
      if slice_text == "0x" and len(message.content)==45:
        SPREADSHEET_ID = '' # Add ID here
        RANGE_NAME = 'A1'
        FIELDS = 1 # Amount of fields/cells

        # Code
        msg = message.content[3:]
        result = [x.strip() for x in msg.split(',')]
        if len(result) == FIELDS:
            # Add
            #print(message.created_at)
            DATA = [message.author.name] + [str(message.author.id)] + [str(message.created_at)] + result
            sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
            await message.channel.send(':white_check_mark: Your data has been successfully submitted!')
            time.sleep(3)
            await message.channel.purge(limit=2)
            if REQUIREDROLE is not None : # allows only one successful message from a user (requires RequiredRole to be enabled)
                role_remove= discord.utils.get(message.author.roles, id=REQUIREDROLE)
                await message.author.remove_roles(role_remove)
      else:
            # Needs more/less fields
            #await message.channel.send(':x: You need to add {0} fields, meaning it can only have {1} comma.'.format(FIELDS,FIELDS-1))
            await message.channel.send(':x: Please enter ETH address only' )
            time.sleep(3)
            await message.channel.purge(limit=2)
    
    # Whois
    # Please dont remove the copyright and github repo
    elif len(message.mentions) > 0:
        for muser in message.mentions:
            if muser.id == client.user.id:
                if any(word in message.content for word in ['whois','who is','Help','help','info']):
                    await message.channel.send('This bot was made by hugonun(https://github.com/hugonun/).\nSource code: https://github.com/hugonun/discord2sheet-bot')


client.run('') # Add bot token here

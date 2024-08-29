import requests
import json
import time

token = 'TOKEN'
message = 'MESSAGE'


def get_dm_channels(token):
    url = 'https://discord.com/api/v9/users/@me/channels'
    headers = {
        'Authorization': token
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch DM channels: {response.status_code} - {response.text}')
        return []


def send_message(token, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    data = {
        'content': message
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f'Message sent to channel {channel_id}')
    else:
        print(f'Failed to send message to channel {channel_id}: {response.status_code} - {response.text}')

dm_channels = get_dm_channels(token)
while(True):
    for channel in dm_channels:
        send_message(token, channel['id'], message)
        #time.sleep(1)




# Function to get the list of guilds (servers)
'''def get_guilds(token):
    url = 'https://discord.com/api/v9/users/@me/guilds'
    headers = {
        'Authorization': token
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch guilds: {response.status_code} - {response.text}')
        return []

# Function to get the list of members in a guild
def get_guild_members(token, guild_id):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/members'
    headers = {
        'Authorization': token
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch members for guild {guild_id}: {response.status_code} - {response.text}')
        return []

# Function to create a DM channel
def create_dm_channel(token, user_id):
    url = f'https://discord.com/api/v9/users/@me/channels'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    data = {
        'recipient_id': user_id
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f'Failed to create DM channel for user {user_id}: {response.status_code} - {response.text}')
        return None

# Function to send a message to a specific channel
def send_message(token, channel_id, message):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    data = {
        'content': message
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f'Message sent to channel {channel_id}')
    else:
        print(f'Failed to send message to channel {channel_id}: {response.status_code} - {response.text}')

# Get the list of guilds
guilds = get_guilds(token)

# Iterate through each guild and send a message to each member
for guild in guilds:
    guild_id = guild['id']
    members = get_guild_members(token, guild_id)
    for member in members:
        user_id = member['user']['id']
        dm_channel_id = create_dm_channel(token, user_id)
        if dm_channel_id:
            send_message(token, dm_channel_id, message)'''

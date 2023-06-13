import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Login As：', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "test" or message.content == "hi":
        await message.channel.send('Hi')

    if message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

client.run("MTExNzc0MDQ5NjUzNDY1MDkwMQ.GI9T58.9QtUAneOYEJKD46rr2dfpkqklWQR1vIEWilxCQ")

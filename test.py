import discord
import random
from discord.ext import commands
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has been spawned')

@client.event
async def on_member_remove(member):
    print(f'{member} has left')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def highfive(ctx):
    await ctx.send('highfive')

@client.command(aliases=['8ball','text'])
async def _8ball(ctx, *,question):
    responses = ['Yes',
                'Maybe',
                'No',
                'I dont think so',
                'Really?',
                'Hell no',
                'Absolutely',
                'Its possible',
                'Of course',
                'Of course not',
                'Obviously',
                'Not a chance',
                'Never',
                'Ask yourself',
                'Nah, Im Bored'
                'There is a little chance']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')



@client.command()
async def clear(ctx,amount):
    amount=int(amount)
    actual_amount=amount+1
    await ctx.channel.purge(limit=actual_amount)
    await ctx.send(f'{amount} message cleared')

@client.command()
async def spam(ctx,msg,amount):
    amount=int(amount)
    if amount>50:
        await ctx.send("I am very lazy you know")
    else:
        for i in range(0,amount):
            await ctx.send(msg)

@client.command()
async def highlow(ctx):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    add = dice1 + dice2
    await ctx.send(f'You got {dice1} and {dice2} that is {add}')
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    add2 = dice1 + dice2
    await ctx.send(f'Bot got {dice1} and {dice2} that is {add2}')
    if add2>=add:
        await ctx.send('Bot wins')
    else:
        await ctx.send('You win')

@client.command()
async def guess(ctx):
    await ctx.send('think a number from  - ')
    await ctx.send('press y if you see your number and n if you dont see you number')
    enter=str(input("1,3,5,7"))
    if enter is "y":
        total = total + 1
    elif enter is "n":
        await ctx.send("soka")
    else:
        await ctx.send("wrong input")
    
    enter=str(input("2,3,6,7"))
    if enter is "y":
        total = total + 2
    elif enter is "n":
        await ctx.send("soka")
    else:
        await ctx.send("wrong input")
    
    enter=str(input("4,5,6,7"))
    if enter is "y":
        total = total + 4
    elif enter is "n":
        await ctx.send("soka")
    else:
        await ctx.send("wrong input")
    
    print(f'your number is{total}')
client.run('NTg3NzA3ODYwMDE2NjkzMjU4.XQJ7Bg.BgoZHKatBm5ctjAplPt45tFTSX0')
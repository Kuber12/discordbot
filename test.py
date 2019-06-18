import discord
import random
from discord.ext import commands
client = commands.Bot(command_prefix = 'do ',case_insensitive=True)

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
async def hello(ctx):
    await ctx.send('yo')

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
                'Ask your mom',
                'Nah, Im bored try later',
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
async def bank(ctx):
    cards=['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
    suits=[' of hearts',' of clubs',' of diamonds',' of spades']
    rcard=random.choice(cards)
    rsuit=random.choice(suits)
    finalres=rcard + rsuit
    await ctx.send(finalres)
client.run('NTg3NzA3ODYwMDE2NjkzMjU4.XQJ7Bg.BgoZHKatBm5ctjAplPt45tFTSX0')
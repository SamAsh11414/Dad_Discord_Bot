# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

import random


Joke = ("What rock group has four men that don't sing? Mount Rushmore.", "When I was a kid, my mother told me I could be anyone I wanted to be. Turns out, identity theft is a crime.", "What concert costs just 45 cents? 50 Cent featuring Nickelback!", "What do you call a mac 'n' cheese that gets all up in your face? Too close for comfort food!", "Why couldn't the bicycle stand up by itself? It was two tired!", "Did you hear about the restaurant on the moon? Great food, no atmosphere!", "It's inappropriate to make a 'dad joke' if you're not a dad. It's a faux pa.", "Did you hear about the circus fire? It was in tents.", "Can February March? No, but April May!", "How do lawyers say goodbye? We'll be suing ya!", "Wanna hear a joke about paper? Never mind—it's tearable.", "What's the best way to watch a fly fishing tournament? Live stream.", "Spring is here! I got so excited I wet my plants.", "I could tell a joke about pizza, but it's a little cheesy.", "Don't trust atoms. They make up everything!", "When does a joke become a dad joke? When it becomes apparent.", "I wouldn't buy anything with velcro. It's a total rip-off.", "What’s an astronaut’s favorite part of a computer? The space bar.", "I don't play soccer because I enjoy the sport. I'm just doing it for kicks!", "Why are elevator jokes so classic and good? They work on many levels.", "Why do bees have sticky hair? Because they use a honeycomb.", "What do you call a fake noodle? An impasta.", "Which state has the most streets? Rhode Island.", "What did the coffee report to the police? A mugging.", "What did the fish say when he hit the wall? Dam.", "Is this pool safe for diving? It deep ends.")
Jokes = random.choice(Joke)

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Dad bot is in " + str(guild_count) + " servers.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "Dad tell me a joke":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		Jokes = random.choice(Joke)
		await message.channel.send(Jokes)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("Nzc4NDA4MDQ2NjY5NTk0Njg0.X7Ri_A.MkmvAzBHOeH8WV-LqD8Vg5bcQa8")

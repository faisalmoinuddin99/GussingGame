import random

name = input("Please! Enter your name: ")
greet = f"Welcome {name}."
print(greet)
maxChance = 5
coins = 0
luckyNumber = random.randint(1,20)
chance = 1
print(luckyNumber)
for chance in range(maxChance+1):
    userGuess = int(input(f"So {name} guess your lucky number: "))
    if userGuess < luckyNumber:
        print("Not even closer")
        coins = coins + 1
    elif userGuess > luckyNumber:
        print("ohoho!!! You surpass the lucky number...")
    elif userGuess == luckyNumber:
        print(f"woohoo {name}!! You made it, {luckyNumber} is your lucky number.")
        coins = coins + 1
        break


print(f"Number of attempts {chance}, Your credit Coins = {coins}")



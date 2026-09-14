import random
n = random.randint(1, 100)
a = -1
guesses = 0
while (a!=n):
    a = int(input("Guess the number: "))
    if (a < n):
        print("Higher number please")
        guesses +=1
    elif (a > n):
        print("Lower number please")
        guesses +=1

print(f"You guess the number {n} correctly in {guesses} number of guesses")

with open("Lowguess.txt", "r+") as f:
    b = f.read()
    bnew = int(b)
    if (bnew>guesses):
        f.write(f"{guesses}")
    


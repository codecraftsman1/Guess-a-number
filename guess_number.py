import random
number = random.randrange(1,100)
ans = int(input("Enter a number: "))

while number!=ans:
    if ans>number:
        print("Too high")
    elif ans<number:
        print("Too low")
    elif ans==number:
        break
    else:
        print("INVALID INPUT")
    ans = int(input("Enter a number: "))

print("Correct guess")
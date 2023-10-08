
secret_number=9
guess_count=0
guess_limit=3

while guess_count<guess_limit:
    Guess=int(input("Enter guess: "))
    guess_count+=1
    if Guess==secret_number:
        print("You win!")
        break
else:
    print("You loose!")
import random

  
total = 0

for roll in range(3):
    cont = input("klicka var du vill")
    dice1 =  random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total =  dice1 + dice2 + total
    print("Du slog ", dice1 , "och ", dice2)
    print("Din poäng är: ", total)
    if dice1 == dice2:
        print("Du slog två av samma")
        print("Du förlorade din poäng är noll")
        total = 0
        break
import random as k

while True:
  d=input("rock,paper,scissors?? (r/p/s):: ").lower()
  choice=("r","p","s")
  if d not in choice:
    print("Invalid input")
    continue
    
  emo={"r":"✊",
      "p":"📃",
      "s":"✂️"
      }

  comp=k.choice(choice)
  print(f"you choose {emo[d]}")
  print(f"computer choose {emo[comp]}")

  if d==comp:
    print("Tie!!")
  elif ((d=="r" and comp=="s") or (d=="p" and comp=="r") or (d=="s" and comp=="p")):
    print("You win!")
  else:
    print("You lose!")
    
  q=input("wanna continue? (y/n):: ").lower()
  if q!= "y":
    print("thanks for playing!!") 
    break

  #heloooo
  ###wwww
import random
chance=6
pasition=0
words =["office","panda","cabin","ginger"]
random_words=random.choice(words)

space=["_"]* len(random_words)
print((" ").join(space))



while "_" in space:
  user_char=input("please guess a lrtter agin: ").lower()
  if user_char in random_words:
    for position in range(len(random_words)):
    
      if user_char == random_words[position]:
        space[position]=user_char
  elif user_char != random_words[pasition]:
      chance=chance-1
      
 
        
  print((" ").join(space))
  print(f"you have {chance} chance left")
  
  if chance==6:
    print("""
  +---+
  |   |
      |
      |
      |
      |
=========
    """)
    
  elif chance==5:
    print("""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """)
  elif chance==4:
      print("""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
      """)
  elif chance==3:
        print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
        """)
  elif chance==2:
    print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
  """)
  elif chance==1:
    print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
  """)
  elif chance==0:
      print("""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    YOU LOSE
    """)
      break  
else:
  print("""

██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
""")

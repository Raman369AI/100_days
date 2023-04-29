import art
import game_data
import random
print(art.logo1)
score=0
A=random.choice(game_data.data)
B=random.choice(game_data.data)

while True:
    print(f"compare A {A['name']} a {A['description']} 'in' {A['country']} \n {art.vs}")

    print(f"against B {B['name']} a {B['description']} 'in' {B['country']}")
    choice=input("Enter who you think has more followers").upper()
    if choice=='A' and A['follower_count']>B['follower_count']:
      score+=1
      print ("You win")
      print(f"score is {score}")
      A=A
      B=random.choice(game_data.data)
    elif choice=='B' and B['follower_count']>A['follower_count']:
      score+=1
      print ("You win")
      print(f"score is {score}")
      A=B
      B=random.choice(game_data.data)
    elif choice=='A' and A['follower_count']<B['follower_count']:
      score+=0
      print ("You lose")
      print(f"score is {score}")
      break
    elif choice=='B' and A['follower_count']>B['follower_count']:
      score+=0
      print ("You lose")
      print(f"score is {score}")
      break
    else:
      pass
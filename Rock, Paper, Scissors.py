from random import randint
yourScore = 0
opponentScore = 0

for x in range(5):
   randomizer = randint(1, 3)
   opponentCondition = ''
   if randomizer == 1:
       opponentCondition = 'ROCK'
   if randomizer == 2:
       opponentCondition = 'SCISSORS'
   if randomizer == 3:
       opponentCondition = 'PAPER'

   you = input("Input your choice: ").upper()
   opponent = ("Opponent: " + opponentCondition)
   print(opponent)

   if you == "ROCK" and opponentCondition == "PAPER":
       print("PAPER covers ROCK. Your Loss")
       print('')
       opponentScore = opponentScore + 1
   if you == "PAPER" and opponentCondition == "SCISSORS":
       print("SCISSORS cuts PAPER. Your Loss")
       print('')
       opponentScore = opponentScore + 1
   if you == "SCISSORS" and opponentCondition == "ROCK":
       print("ROCK crushes SCISSORS. Your Loss")
       print('')
       opponentScore = opponentScore + 1
   if you == "PAPER" and opponentCondition == "ROCK":
       print("PAPER covers ROCK. Nice Job")
       print('')
       yourScore = yourScore + 1
   if you == "SCISSORS" and opponentCondition == "PAPER":
       print("SCISSORS cuts PAPER. Nice Job")
       print('')
       yourScore = yourScore + 1
   if you == "ROCK" and opponentCondition == "SCISSORS":
       print("ROCK crushes SCISSORS. Nice Job")
       print('')
       yourScore = yourScore + 1
   if you == opponentCondition:
       print("Same stuff. Keep going")
       print('')

print("Your Score: " + str(yourScore))
print("Opponent's Score: " + str(opponentScore))
print('')

if yourScore > opponentScore:
   print("You win! Nice job!")
elif yourScore == opponentScore:
   print("Welp...a draw")
else:
   print("The computer won. Skill issue")
  


import player
import check_input
def take_turn(playerObj):
  
  playerObj.roll_dice()

  """ print the vales of each dice """
  print(playerObj)


  """ After rolling the dice we will check if the player was able to get points """
  pair = playerObj.has_pair()
  three = playerObj.has_three_of_a_kind()
  series = playerObj.has_series()

  if three:
    print("You got 3 of a kind!")

  elif pair:
    print("You got a pair!")
  
  
  elif series:
    print("You got a series of 3!")

  else:
    print("Aww.  Too Bad.")  


  """ prints the score """
  points = playerObj.get_points()
  print(f"Score = {points}")

  return points


def main():
  playerObj = player.Player()



  print("-Yahtzee-")
  while True:
    points = take_turn(playerObj)

    playagain =  check_input.get_yes_no("Play again? (Y/N): ")
    
    if playagain == False:
      break

  print("Game Over. 💥") 
  print(f"Final score = {points}")




main()
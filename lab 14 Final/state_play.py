import state_asleep
import puppy_state

class StatePlay(puppy_state.PuppyState):
    
    def play(self,puppy):
        
        if(puppy.plays == 3):
            """ if the dog plays 3 times, then it gets exausted and goes to sleep state """
            print("The puppy played so much and fell asleep")
            """ Since the state is going to asleep, then we reset the amount of play and feed of the puppy """
            puppy.reset()
            puppy.change_state(state_asleep.StateAsleep())
        else:
            """ if the dog still didnt reach 3 times playing he will continue playing """
            print("You throw the ball again and the puppy excitedly chases it.")
            puppy.inc_plays()
    def feed(self,puppy):
        """ if the puppy is playing, he cant return to the eating state """
        print("The puppy is too busy playing with the ball to eat right now.")


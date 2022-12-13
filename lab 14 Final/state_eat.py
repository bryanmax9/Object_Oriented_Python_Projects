import state_asleep
import puppy_state
import state_play

class StateEat(puppy_state.PuppyState):

    def play(self,puppy):

        print("The puppy looks up from its food and chases the ball you threw.")
        puppy.change_state(state_play.StatePlay())
        puppy.inc_plays()
    def feed(self,puppy):

        if (puppy.feeds == 3):
            """ if user makes the pet eat a 3 times, then it goes asleep """
            print("The puppy ate so much and fell asleep")
            puppy.change_state(state_asleep.StateAsleep())
            puppy.inc_feeds()
            """ if falls asleep, play and feed resets """
            puppy.reset()
        else:
            """ else, the puppy will eat """
            print("The puppy eats some more food.")
            puppy.inc_feeds()

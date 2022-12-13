import state_eat
import puppy_state

class StateAsleep(puppy_state.PuppyState):
    
    def play(self,puppy):
        print("The puppy is asleep. It doesn't want to play right now.")
    def feed(self,puppy):

        print("The puppy wakes up and comes running to eat.")
        puppy.inc_feeds()
        puppy.change_state(state_eat.StateEat())

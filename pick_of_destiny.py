# Pick of Destiny
# Let destiny choose
# Does it say yes or no ?
# created by ap33k4b00 - Franco Ramirez

import random
from datetime import datetime

class Destiny:
    # Amount of tries for trying to match your current time with destiny's
    tries = 0

    # Lists to store hour, minute and second of your current time and destiny's time
    current_time = []
    destiny_time = []

    def get_coin_side(self):
        # Another bump on the road, you may say
        # this will give you a coin side, something more to make sure destiny has more to work with
        coin = ['heads', 'tails']
        coin_side = coin[random.randint(0, 1)]
        return coin_side

    def getting_user_time(self):
        time = datetime.now()
        current_hour = time.strftime("%H")
        current_minute = time.strftime("%M")
        current_second = time.strftime("%S")

        # Adding your current time 
        self.current_time.append(current_hour)
        self.current_time.append(current_minute)
        self.current_time.append(current_second) 

    def change_destiny(self):
        # Destiny giving a random time
        # Adding it to destiny's time until it finally matches your current time
        for i in range(3):
            if i == 0:
                hour = random.choice(range(0, 24))
                if hour < 10:
                    self.destiny_time.append("0" + str(hour))
                else:
                    self.destiny_time.append(str(hour))
            elif i == 1:
                minute = random.choice(range(0, 60))
                if minute < 10:
                    self.destiny_time.append("0" + str(minute))
                else:
                    self.destiny_time.append(str(minute))
            else:
                second = random.choice(range(0, 60))
                if second < 10:
                    self.destiny_time.append("0" + str(second))
                else:
                    self.destiny_time.append(str(second))

    def start(self):
        self.getting_user_time() 
        coin_side = self.get_coin_side()

        while True:
            self.tries += 1
            self.change_destiny()
            # Matching your time with destiny's
            if self.current_time == self.destiny_time:
                print(f"This took {self.tries} tries!") # Amount of tries it took
                if coin_side == "heads":    # After times match and heads is your coin side, Destiny says yes!
                    print("Destiny says yes!")
                    # Shows match
                    print(self.current_time)
                    print(self.destiny_time)
                    break
                else:   # After times match and tails is your coin side, Destiny says no!
                    print("Destiny says no!")
                    # Shows match
                    print(self.current_time)
                    print(self.destiny_time)
                    break
            else:   # If no match, loop will continue
                print("processing...")
                self.destiny_time.clear() # Clears list every time no match happens
                continue

if __name__ == '__main__':
    destiny = Destiny()
    # Program start
    destiny.start()
#=================================================================#
#
# Tuning Machine, 
#   used to fix the Time Stream
#   
#       Crafter: jAAkiT      
#       
#=================================================================#

class Tuner:

    def __init__(self, freq=0):
        self.freq = freq
        self.history = {}
        self.update_history(self.freq)

    def tune_up(self, steps):
        self.freq += steps
        self.update_history(self.freq)

    def tune_down(self, steps):
        self.freq -= steps
        self.update_history(self.freq)

    def update_history(self, freq):
        if self.history.get(freq) == None:
            self.history[freq] = 1
        else: 
            self.history[freq] += 1
            print("First duplicate freq is: ",  freq)
            exit()

    def print_history(self):
        for entry in self.history:
            print("freq: ", entry)

    def auto_tune(self, instructions):
        for instruction in instructions:
            self.tune_up(instruction[1]) if instruction[0] == "+" else self.tune_down(instruction[1]) 
                

file = open("input.txt", "r")
commands = []
for line in file:
    operator = str(line[0])
    number = int(line[1:])
    commands.append([operator, number])

tuner = Tuner()
# tuner.tune_up(6)
# tuner.tune_up(1)
# tuner.tune_down(6)
# tuner.tune_up(5)
# tuner.print_history()

while True:
    tuner.auto_tune(commands)



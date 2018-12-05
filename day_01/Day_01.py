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
        self.updateHistory(self.freq)

    def tuneUp(self, steps):
        self.freq += steps
        self.updateHistory(self.freq)

    def tuneDown(self, steps):
        self.freq -= steps
        self.updateHistory(self.freq)

    def updateHistory(self, freq):
        if self.history.get(freq) == None:
            self.history[freq] = 1
        else: 
            self.history[freq] += 1
            print("First duplicate freq is: ",  freq)
            exit()

    def printHistory(self):
        for entry in self.history:
            print("freq: ", entry)

    def autoTune(self, instructions):
        for instruction in instructions:
            self.tuneUp(instruction[1]) if instruction[0] == "+" else self.tuneDown(instruction[1]) 
                


file = open("input.txt", "r")
commands = []
for line in file:
    operator = str(line[0])
    number = int(line[1:])
    commands.append([operator, number])

tuner = Tuner()
# tuner.tuneUp(6)
# tuner.tuneUp(1)
# tuner.tuneDown(6)
# tuner.tuneUp(5)
# tuner.printHistory()

while True:
    tuner.autoTune(commands)



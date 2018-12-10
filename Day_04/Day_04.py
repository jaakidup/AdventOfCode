#=================================================================#
#
# North Pole Guard Watch Machine,
#   used to watch guard sleeping patterns
#
#       Crafter: jAAkiT
#
#=================================================================#


class Guard:

    def __init__(self, id):
        self.id = id
        self.times = [0] * 60
        self.sleep_time = 0
        self.max_asleep = 0
        self.time_most_asleep = 0
        self.total = 0

    def go_to_sleep(self, sleep_time):
        self.sleep_time = sleep_time

    def wake_up(self, up_time):
        for time in range(up_time - self.sleep_time):
            self.times[self.sleep_time + time] += 1
        self.sleep_time = 0
        self.calculate_times()

    def calculate_times(self):
        self.max_asleep = max(self.times)
        self.time_most_asleep = self.times.index(self.max_asleep)
        sum = 0 
        for i in self.times:
            sum += i
        self.total = sum


class Schedule:

    def __init__(self):
        self.guards = {}

    def add_guard(self, guard):
        if self.guards.get(guard.id):
            pass
        else:
            self.guards[guard.id] = guard

    def is_guard(self, id):
        return self.guards.get(id)


# ============ #
#   Run
#


input = []
schedule = Schedule()


f = open("./input.txt")

for line in f:
    input.append(line)

input.sort()


id = int()
start = None
end = None

for entry in input:

    if entry.split()[3][0] == "#":
        id = int(entry.split()[3][1:])
        schedule.add_guard(Guard(id))

    if entry.split()[3] == "asleep":
        time = int(entry.split()[1][-3:-1])
        if schedule.is_guard(id):
            schedule.guards[id].go_to_sleep(time)

    if entry.split()[3] == "up":
        time = int(entry.split()[1][-3:-1])
        schedule.guards[id].wake_up(time)



# ============================ #
#   {part Un}
# ============================ #


who, most, what_time, laziest = 0, 0, 0, 0

for id in schedule.guards:
    if schedule.guards[id].total > most:
        most = schedule.guards[id].total
        laziest, time = id, schedule.guards[id].time_most_asleep

print("{ part Un }", laziest * time)


# ============================ #
#   {part Deux}
# ============================ #

who, most, what_time = 0, 0, 0
for id in schedule.guards:
    max = schedule.guards.get(id).max_asleep
    if max > most:
        who, most, what_time = id, max, schedule.guards[id].time_most_asleep 

print("{ part Deux }", who * what_time)


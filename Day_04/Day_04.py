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

    def go_to_sleep(self, sleep_time):
        self.sleep_time = sleep_time

    def wake_up(self, up_time):
        print("wake up")
        for time in range(up_time - self.sleep_time):
            self.times[self.sleep_time + time] += 1
        self.sleep_time = 0
        print("recalculate sleep time")
        # self.calculate_times()

    def calculate_times(self):
        self.max_asleep = max(self.times)
        self.time_most_asleep = self.times.index(self.max_asleep)


class Schedule:

    def __init__(self):
        self.guards = []

    def add_guard(self, guard):
        if guard in self.guards:
            print("guard", id, " already in schedule")
        else:
            print("adding guard ", guard.id, "to schedule")
            # self.guards.append(guard)
            self.guards.insert(int(guard.id), guard)
            print(self.guards.index(guard))
            print("guard", id, "successfully added to schedule at index", self.guards.index(guard))

    def is_guard(self, id):
        # checks to see if guard(id) is registered on schedule
        if len(self.guards) == 0:
            return False
        for guard in self.guards:
            if guard.id == id:
                return True
        return False


# schedule = Schedule()
# guard1, guard2, guard3, guard4, guard5, guard6  = Guard(1),Guard(2),Guard(3),Guard(4),Guard(5),Guard(6)
# schedule.add_guard(guard1)
# schedule.add_guard(guard2)
# schedule.add_guard(guard3)
# schedule.add_guard(guard4)
# schedule.add_guard(guard5)
# schedule.add_guard(guard6)


# schedule.guards[1].go_to_sleep(7)
# schedule.guards[1].wake_up(45)
# schedule.guards[1].go_to_sleep(16)
# schedule.guards[1].wake_up(17)
# schedule.guards[1].go_to_sleep(15)
# schedule.guards[1].wake_up(34)

# # start, end = 58, 59
# # for time in range(end - start):
# #     schedule.guards[1].times[start + time] += 1

# print(schedule.guards[1].times)
# print(schedule.guards[1].most_asleep())


# ======================================================== #
# ======================================================== #
input = []
schedule = Schedule()

f = open("./input.txt")
# f = open("/home/jaaki/python/adventOfCode/Day_04/input.txt")


for line in f:
    input.append(line)

input.sort()


id = int()
start = None
end = None

for entry in input:
    # print(entry.split()[3][0])

    if entry.split()[3][0] == "#":
        id = int(entry.split()[3][1:])
        # print("guard ", id, " begins shift")
        schedule.add_guard(Guard(id))

    if entry.split()[3] == "asleep":
        time = int(entry.split()[1][-3:-1])
        print("guard ", id, " falls asleep at", time)
        if schedule.is_guard(id):
            print("guard ", id, " found")
            print(schedule.guards[id])
            # schedule.guards[id].go_to_sleep(time)
        print("ok")
        # else:
        #     print("guard not found")

    if entry.split()[3] == "up":
        print("guard ", id, " wakes up at", time)
        time = int(entry.split()[1][-3:-1])
        schedule.guards[id].wake_up(time)


# for guard in schedule.guards:
#     print(guard)

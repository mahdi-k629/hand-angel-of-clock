class angel():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    def calculate(self):
        hour_hand = (30 * self.hour) + (0.5 * self.minute)
        minute_hand = (0 * self.hour) + (6 * self.minute)
        res = 0
        if minute_hand > hour_hand:
            res = minute_hand - hour_hand
        else:
            res = hour_hand - minute_hand
        return res if res < 180 else 360 - res

hour = int(input("Enter Hour (1 - 12): "))
minute = int(input("Enter Minute(0 - 59): "))
angel = angel(hour, minute)
print(angel.calculate())
class MyCalendarThree:

    def __init__(self):
        self.k = {}
        self.b = 0

    def book(self, start, end):
        for i in range(start, end):
            if i in self.k:
                self.k[i] += 1
            else:
                self.k[i] = 1
            self.b = max(self.b, self.k[i])
        return self.b


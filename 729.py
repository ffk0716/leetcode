class MyCalendar:
    def __init__(self):
        self.k = set()
    def book(self, start, end):
        for s in self.k:
            if not (s[1] <= start or end <= s[0]):
                return False
        self.k.add((start, end))
        return True

# Your MyCalendarThree object will be instantiated and called as such:
#obj = MyCalendar()
#print(obj.book(10,20))
#print(obj.book(15,200))

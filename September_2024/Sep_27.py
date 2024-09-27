class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # Check for triple booking
        for i, j in self.overlaps:
            if start < j and end > i:
                return False

        # Check for double booking
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))

        self.calendar.append((start, end))
        return True

class MyCalendar:

    def __init__(self):
        # List to store all the booked intervals
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlap with any existing booking
        for s, e in self.bookings:
            # If the new event overlaps with any existing event, return False
            if start < e and s < end:
                return False
        
        # If no overlap, add the event to the bookings and return True
        self.bookings.append((start, end))
        return True

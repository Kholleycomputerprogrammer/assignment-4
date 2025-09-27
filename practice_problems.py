# Problem 1: Duplicate Tracker
def has_duplicates(product_ids):
    """
    A set is used to track seen product IDs because it provides average time complexity for lookups and insertions.
    This allows us to efficiently check for duplicates as we iterate through the list.
    """
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False


# Problem 2: Order Manager
from collections import deque

class TaskQueue:
    """
    A ddouble-ended queue is ideal here because it allows time complexity for both appending to the end
    and popping from the front, which matches the required operations for a task queue.
    """
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)  

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()  
        return None


# Problem 3: Unique Value Counter
class UniqueTracker:
    """
    A set is used to store unique values because it automatically handles duplicates and supports insertion and lookup.
    This makes it efficient to track and count unique values in a stream.
    """
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)  

    def get_unique_count(self):
        return len(self.unique_values)  

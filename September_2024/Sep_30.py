class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increment_list = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        idx = len(self.stack) - 1
        # Apply the increment to the top element
        result = self.stack.pop() + self.increment_list[idx]
        
        if idx > 0:
            # Transfer the increment to the next element below
            self.increment_list[idx - 1] += self.increment_list[idx]
        
        # Reset the increment value for this index
        self.increment_list[idx] = 0
        
        return result

    def increment(self, k: int, val: int) -> None:
        # Increment the bottom k elements by val
        # We only store the increment at the k-1 index, and apply it lazily
        if self.stack:
            limit = min(k, len(self.stack)) - 1
            self.increment_list[limit] += val

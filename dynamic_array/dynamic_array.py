class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def get(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        return self.array[index]

    def set(self, index: int, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        self.array[index] = value

    def add(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def remove(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1  

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty array.")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def __str__(self):
        return str(self.array[:self.size])

# Example usage:
if __name__ == "__main__":
    arr = DynamicArray(2)
    arr.add(1)
    arr.add(2)
    print(arr) 

    arr.add(3)
    print(arr)

    arr.remove(1)
    print(arr)

    print(arr.get(0))
    arr.set(0, 10)
    print(arr)

    print(arr.pop())
    print(arr)
    print(arr.is_empty())
    arr.pop()
    print(arr.is_empty())

    
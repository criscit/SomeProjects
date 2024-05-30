

class NoSuchElementException(Exception):
    pass


class WretchedPriorityQueue:
    def __init__(self):
        self.inner_array = [None] * 50
        self.size = 0

    def add(self, x: int):
        if self.size == 0:
            self.size += 1
            self.inner_array[0] = x
            return

        if self.size == len(self.inner_array):
            self.double_array()

        temp = x
        for i in range(self.size):
            if x <= self.inner_array[i]:
                temp, self.inner_array[i] = self.inner_array[i], x
                for b in range(i, self.size - 1):
                    temp, self.inner_array[b + 1] = self.inner_array[b + 1], temp

                break

        self.inner_array[self.size] = temp
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise NoSuchElementException("The queue is empty")

        ret_value = self.inner_array[0]
        if self.size - 1 >= 0:
            self.inner_array = self.inner_array[1:] + [None]

        self.size -= 2
        return ret_value

    def peek(self) -> int:
        if self.is_empty():
            raise NoSuchElementException("The queue is empty")
        return self.inner_array[0]

    def is_empty(self):
        return self.size == 0

    def double_array(self):
        new_arr = self.inner_array[:] + [None] * len(self.inner_array)
        self.inner_array = new_arr

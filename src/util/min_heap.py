import numpy as np


class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.items = np.empty(self.capacity, dtype=np.int)

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) / 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        temp = self.items[index_one]
        self.items[index_one] = self.items[index_two]
        self.items[index_two] = temp

    def ensure_extra_capacity(self):
        copy = self.items

    def peek(self):
        if self.size == 0:
            raise UnboundLocalError("Empty")
        return self.items[0]

    # extracts top-most element
    def poll(self):
        if self.size == 0:
            raise UnboundLocalError("Empty")
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item):
        # ensure capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index


def main():
    heap = MinHeap(10)
    heap.add(9)
    heap.add(3)
    heap.add(5)
    heap.add(1)
    print(heap.items)

main()
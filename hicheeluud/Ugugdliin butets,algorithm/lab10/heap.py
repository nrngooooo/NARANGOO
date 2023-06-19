class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent(i) >= 0

    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_heap(self):
        # calculate the number of levels in the heap
        num_levels = 0
        num_nodes = 1
        while num_nodes <= len(self.heap):
            num_levels += 1
            num_nodes *= 2

        # print the nodes level by level
        level = 0
        while level < num_levels:
            level_nodes = 2 ** level
            start_index = 2 ** level - 1
            end_index = min(start_index + level_nodes, len(self.heap))
            for i in range(start_index, end_index):
                print(self.heap[i], end=" ")
            print()
            level += 1

    def insert(self, key):
        self.heap.append(key)
        self.heap_up(len(self.heap) - 1)

    def heap_up(self, i):
        while self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)


max_heap = MaxHeap()

array = [45, 99, 63, 27, 29, 57, 42, 35, 12, 24]

for i in array:
    max_heap.insert(i)

print("Current heap:")
max_heap.print_heap()

max_heap.insert(50)
print("After adding 50:")
max_heap.print_heap()

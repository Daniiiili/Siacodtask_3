import time
import matplotlib.pyplot as plt
import heapq
from bisect import insort
import random


class PriorityQueueHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x, p):
        heapq.heappush(self.heap, (-p, x))

    def extract_max(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None


class PriorityQueueLinkedList:
    def __init__(self):
        self.list = []

    def insert(self, x, p):
        insort(self.list, (-p, x))

    def extract_max(self):
        if self.list:
            return self.list.pop(0)[1]
        return None


def measure_time_high_precision(queue_type, n, operations):
    pq = queue_type()
    insert_times = []
    extract_times = []

    for _ in range(operations):
        x = random.randint(1, 1000)
        p = random.randint(1, 1000)

        start_time = time.perf_counter()
        pq.insert(x, p)
        insert_times.append(time.perf_counter() - start_time)

        start_time = time.perf_counter()
        pq.extract_max()
        extract_times.append(time.perf_counter() - start_time)

    return insert_times, extract_times


n = 1000
operations = 100000

heap_insert_times, heap_extract_times = measure_time_high_precision(PriorityQueueHeap, n, operations)
list_insert_times, list_extract_times = measure_time_high_precision(PriorityQueueLinkedList, n, operations)

avg_heap_insert = sum(heap_insert_times) / len(heap_insert_times)
avg_heap_extract = sum(heap_extract_times) / len(heap_extract_times)
avg_list_insert = sum(list_insert_times) / len(list_insert_times)
avg_list_extract = sum(list_extract_times) / len(list_extract_times)

print("Средние времена выполнения:")
print(f"Heap - Insert: {avg_heap_insert:.10f}, ExtractMax: {avg_heap_extract:.10f}")
print(f"LinkedList - Insert: {avg_list_insert:.10f}, ExtractMax: {avg_list_extract:.10f}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(range(operations), heap_insert_times, label="Heap (Insert)", alpha=0.7)
plt.plot(range(operations), list_insert_times, label="Linked List (Insert)", alpha=0.7)
plt.title("Время выполнения операции Insert")
plt.xlabel("Операция")
plt.ylabel("Время (секунды)")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(range(operations), heap_extract_times, label="Heap (ExtractMax)", alpha=0.7)
plt.plot(range(operations), list_extract_times, label="Linked List (ExtractMax)", alpha=0.7)
plt.title("Время выполнения операции ExtractMax")
plt.xlabel("Операция")
plt.ylabel("Время (секунды)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

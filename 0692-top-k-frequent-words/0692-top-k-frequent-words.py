
class Solution:
    def min_heapify_up(self, heap):
        end = len(heap)-1

        while end != 0:
            parent = (end-1)//2

            if (heap[parent][1] > heap[end][1] or(heap[parent][1] == heap[end][1] and heap[parent][0] < heap[end][0])):
                heap[parent], heap[end] = heap[end], heap[parent]
                end = parent
            else:
                break

    def min_heapify_down(self, heap, i):
        curr = i
        n = len(heap)

        while True:
            left = curr*2+1
            right = curr*2+2

            if left >= n:
                break

            if right >= n:
                if (heap[left][1] < heap[curr][1] or
                    (heap[left][1] == heap[curr][1] and
                     heap[left][0] > heap[curr][0])):

                    heap[left], heap[curr] = heap[curr], heap[left]
                    curr = left
                else:
                    break
            else:
                if (heap[left][1] < heap[right][1] or
                    (heap[left][1] == heap[right][1] and
                     heap[left][0] > heap[right][0])):

                    if (heap[curr][1] > heap[left][1] or
                        (heap[curr][1] == heap[left][1] and
                         heap[curr][0] < heap[left][0])):

                        heap[curr], heap[left] = heap[left], heap[curr]
                        curr = left
                    else:
                        break
                else:
                    if (heap[curr][1] > heap[right][1] or
                        (heap[curr][1] == heap[right][1] and
                         heap[curr][0] < heap[right][0])):

                        heap[curr], heap[right] = heap[right], heap[curr]
                        curr = right
                    else:
                        break

    def topKFrequent(self, words, k):
        freq = {}

        heap = []

        for i in words:
            freq[i] = freq.get(i, 0)+1

        for key, val in freq.items():
            temp = (key, val)

            if len(heap) == k:
                if (heap[0][1] < temp[1] or
                    (heap[0][1] == temp[1] and
                     heap[0][0] > temp[0])):

                    heap[0] = temp
                    self.min_heapify_down(heap, 0)
                else:
                    continue
            else:
                heap.append(temp)
                self.min_heapify_up(heap)

        result = list(map(
            lambda x: x[0],
            sorted(heap, key=lambda x: (-x[1], x[0]))
        ))

        return result
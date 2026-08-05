class KthLargest:

    def min_heapify_down(self, nums, i):
        n = len(nums)
        curr = i

        while True:
            left = curr * 2 + 1
            right = curr * 2 + 2

            if left >= n:
                break

            if right >= n:
                if nums[curr] > nums[left]:
                    nums[curr], nums[left] = nums[left], nums[curr]
                    curr = left
                else:
                    break
            else:
                if nums[left] < nums[right]:
                    if nums[curr] > nums[left]:
                        nums[curr], nums[left] = nums[left], nums[curr]
                        curr = left
                    else:
                        break
                else:
                    if nums[curr] > nums[right]:
                        nums[curr], nums[right] = nums[right], nums[curr]
                        curr = right
                    else:
                        break

    def insert(self, heap):
        current = len(heap) - 1

        while current != 0:
            parent = (current - 1) // 2

            if heap[parent] > heap[current]:
                heap[parent], heap[current] = heap[current], heap[parent]
                current = parent
            else:
                break

    def __init__(self, k: int, nums):
        self.k = k
        self.heap = []

        for num in nums:

            if len(self.heap) < k:
                self.heap.append(num)
                self.insert(self.heap)

            elif num > self.heap[0]:
                self.heap[0] = num
                self.min_heapify_down(self.heap, 0)

    def add(self, val: int):

        if len(self.heap) < self.k:
            self.heap.append(val)
            self.insert(self.heap)

        elif val > self.heap[0]:
            self.heap[0] = val
            self.min_heapify_down(self.heap, 0)

        return self.heap[0]
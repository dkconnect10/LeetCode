class Solution:
    def heapify_down(self, nums, i):
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

        return nums

    def build(self, nums):
        n = len(nums)
        nonleaf_node = n // 2 - 1

        for i in range(nonleaf_node, -1, -1):
            self.heapify_down(nums, i)

        return nums

    def delete(self, nums):
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop()

        if nums:
            self.heapify_down(nums, 0)

        return nums

    def kWeakestRows(self, mat, k):
        heap = []
        result = []

        for i in range(len(mat)):
            count = 0

            for value in mat[i]:
                if value == 1:
                    count += 1
                else:
                    break

            heap.append((count, i))

        self.build(heap)

        while k:
            result.append(heap[0][1])
            self.delete(heap)
            k -= 1

        return result
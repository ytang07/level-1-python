import heapq

class MedianFinder_MaxMin:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    # add a number to a constantly changing two heap structure
    def addNum(self, num: int) -> None:
        # first entry goes into min heap
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return
        # second entry - if this number is greater than the first
        # entry in min heap then we move it to the min heap and
        # move the negative of the current min heap head to the max heap
        # else, we push the negative value to the max heap
        if not self.max_heap:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            return
        # if the length of the heaps are the same
        if len(self.max_heap) == len(self.min_heap):
            # if the number is greater than the current
            # greatest number in the max heap, we put it on the
            # max heap, otherwise, we push it on the min heap
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        # if the length of the max heap is greater than the length
        # of the min heap
        elif len(self.max_heap) > len(self.min_heap):
            # if the number is less than the min of the max heap
            # push the min of the max heap onto the min heap and
            # push the negative of the number onto the max heap
            # otherwise, push the number onto the min heap
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        # finally if the min heap is greater than the length
        # of the max heap
        else:
            # if the number is greater than the max of the min heap
            # put the min heap max onto the max heap
            # push the number onto the min heap
            # otherwise push the negative of the number onto the max heap
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
    # find the median
    def findMedian(self) -> float:
        # if the length of the heaps are the same
        if len(self.max_heap) == len(self.min_heap):
            # return the average of the min of the max heap
            # and the max of the min heap
            return (-self.max_heap[0] + self.min_heap[0])/2
        # if the length of the max heap is greater than
        # the length of the min heap
        elif len(self.max_heap) > len(self.min_heap):
            # return the min of the max heap
            return -self.max_heap[0]
        # if the length of the min heap is greater
        # than the length of the max heap
        else:
            # return the max of the min heap
            return self.min_heap[0]
        
class MedianFinder_Counting:

    def __init__(self):
        self.nums = []
        self.count = [0]*211

    # add a number to the list
    # update the count list index num+105
    def addNum(self, num: int) -> None:
        # print(f"pre adding {num}: {self.count[num+105]}")
        self.count[num+105] += 1
        self.nums.append(num)
        # print(f"post adding {num}: {self.count[num+105]}")

    def counting_sort(self) -> list:
        # turn count into an aggregated count
        agg = self.count.copy()
        for i in range(1, 211):
            agg[i] += agg[i-1]
        
        # start creating sorted list
        i = len(self.nums)-1
        sorted_list = [0]*len(self.nums)
        # counting sort placement algorithm
        while i >= 0:
            sorted_list[agg[self.nums[i]+105]-1] = self.nums[i]
            agg[self.nums[i]+105] -= 1
            i -= 1
        return sorted_list

    # call counting sort
    # find the median
    def findMedian(self) -> float:
        sorted_list = self.counting_sort()
        num = len(sorted_list)
        if num % 2 == 0:
            return (sorted_list[num//2-1] + sorted_list[num//2])/2
        else:
            return sorted_list[(num-1)//2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

heap_version = MedianFinder_MaxMin()
counting_version = MedianFinder_Counting()

def add_both(num):
    heap_version.addNum(num)
    counting_version.addNum(num)

def get_medians():
    print(heap_version.findMedian())
    print(counting_version.findMedian())

if __name__ == "__main__":
    add_both(5)
    add_both(3)
    add_both(6)
    add_both(-10)
    add_both(2)
    add_both(88)
    get_medians()
    add_both(12)
    add_both(-1)
    add_both(-2)
    add_both(-74)
    get_medians()
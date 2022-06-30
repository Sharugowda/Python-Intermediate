
from heapq import heappop, heappush
from typing import List


class Heap_Solution:
    """
    Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

    Input: arr = [5,5,4], k = 1
    Output: 1
    Explanation: Remove the single 4, only 5 is left.

    Input: arr = [4,3,1,1,3,3,2], k = 3
    Output: 2
    Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
    
    """
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if len(arr) <= k:
            return 0
        
        dict = {}
        for number in arr:
            if number not in dict:
                dict[number] = 0
            dict[number] +=1
        
        print(dict)
        
        minHeap = []
        
        for number, amount in dict.items():
            heappush(minHeap, (amount, number))
        
        print(minHeap)
        
        while k > 0 and len(minHeap) > 0:
            print("----------------------------")
            print(k)
            
            amount, number = heappop(minHeap)
            print(f"{amount} : {number}")
            print(f"minHeap: {minHeap}")
            k -= amount
            print(f"k: {k}")
        length = len(minHeap)
        
        print(length)
        
        return length if k >=0 else length +1


funtion_input =  Heap_Solution()
arr=[5,5,4]
k=1
answer = funtion_input.findLeastNumOfUniqueInts(arr,k)
print(f"answer: {answer}")
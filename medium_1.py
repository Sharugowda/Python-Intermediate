
from heapq import heappop, heappush
from typing import List


class Heap_Solution:
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
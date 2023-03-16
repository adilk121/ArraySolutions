import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a min-heap to store the next smallest element
        heap = []
        
        # Push the first element of each list into the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        # Create a dummy node to hold the merged list
        dummy = ListNode(0)
        curr = dummy
        
        # Keep popping the minimum element from the heap and inserting the next element of the list into the heap
        while heap:
            val, i = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return dummy.next

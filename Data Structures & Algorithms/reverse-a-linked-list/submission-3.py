# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We got linkedlist and got some nodes and we are going to take each of this list and reverse them and 
        # We will have a new head and we will return that
        # We can do this in 2 ways: Iterative and Recursive way

        # As example we can take 1 to and 3 pointing to the right  
        # We can use two pointer instead of 2 pointing 
        # What are the 2 pointers going to be? 
        # We can initialize the first pointer current at the first node which is our head 
        # for our example case we set the current at 1
        # Then maintain prev pointer and initalially is set to null 
        # In the first example it is going to be null because nothing is there before 1
        # then for the first node 1 we will take the pointer pointing it at 2 
        # and reverse it so it points at null
        # Now are going to shift the pointers we will take the prev pointer and make it current 
        # then take the current shiftt to next node 
        # Since we break the link now we need to save it before we shift 
        # now the current is 2 and prev is 1 then reverse the pointer and shift the prev and 
        # Finally prev is going to be at 3 and current is going to be null we reach the end of our list 
        # So How we retuirn to the head?
        # Luckily for us prev is equal to the new head so that will be our result

        # Solution 1: Iterative Approach(optimal)

        prev, curr = None, head

        while curr:
            nxt = curr.next # temp variable so we can save that
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        # This is the most optimal solution 
        # Time complexity is O(n) and memory is O(1) becuase we are using pointer no other DSA

        # Solution 2: Recursive Approach

        # The time complexity is O(N) so it is the same 
        # The space complexity is going to change because we will use extra memory : O(N)

        # We need to breakit down into sub problem
        # Our initial head is 1 and if i want to do recursive call 
        # Instead of reversing the entire linked list 
        # We reverse the remainder of the linked list 
        # Which is everytrhing except the first one 
        # now we break it down to 2 sub problems and have 2 nodes to deal with
        # Lets take it one step further now
        # lets break it down the second sub problem even more 2 and 3
        # after 3 it is null we can't reverse that so that is the base case
        # Instead of that we can take the second pointer from 2 to 3 and
        # Keep 3 and set us null and pop back so since we are at 2 then set it to null and pop back 
        # Now we are at 1 has access to 2 and we set 1 as null so the next is also Null so we reach the end 
        # All are reversed in the code we need to maintain the last node as new head

        # Base case
        if not head:
            return None
        
        newHead = head
        # Sub-problem
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead







        
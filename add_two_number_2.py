# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def display(self, data_node):
        __current_node = data_node
        while __current_node:
            print(__current_node.val)
            __current_node = __current_node.next
        print("null")
        
    def __get_len(self, __node):
        __current = __node
        __count = 0
        while __current:
            __count += 1
            __current = __current.next
        return __count
    def cal(self, __n1, __n2):
        __current1 = __n1
        __current2 = __n2
        __rev1 = self.reverse_n(__current1)
        __rev2 = self.reverse_n(__current2)

        __result1 = int("".join(map(str, __rev1)))
        __result2 = int("".join(map(str, __rev2)))
        
        __total = __result1 + __result2
    
        __text = str(__total)
        __text[::-1]
        __text = __text[::-1]
        __pp = []
        for o in range(len(__text)):
            __pp.append(int(__text[o]))

        __l1_node = ListNode(__pp[0])
        __cur = __l1_node
        for __x in range(len(__pp)):
            if __x != 0:
                __cur.next = ListNode(__pp[__x])
                __cur = __cur.next
 
        __print_p = __l1_node
        return __print_p
    
    def reverse_n(self, __list):
        __current = __list
        __rev1 = []
        while __current:
            __rev1.append(__current.val)
            __current = __current.next
            
        __rev1.reverse()
        
        return __rev1
                
               
    def addTwoNumbers(self, l1, l2):
        __current_l1 = l1
        __current_l2 = l2
        __result = self.cal(__current_l1, __current_l2)
        
        return __result
        
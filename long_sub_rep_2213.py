import re
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        
        string = s
        string_q = queryCharacters
        ind = queryIndices
        arr1 = list(string)
        arr2 = list(string_q)
        
        self.n = len(arr1)
        
        #self.n = len(data)
        # Allocating 4 * n space handles all tree levels safely
        self.tree = [""] * (4 * self.n)
        __end_len = self.n - 1
        if (len(string) == 1):
            self.tree = arr1
            
        else:
            if self.n > 0:
                self._build(arr1, 1, 0,__end_len)
            
        str_result = ""
        digit = ""
        str_digit = ""
        arr_result = []
        arr_digit = []
        #"""
        for x in range(len(ind)):
            self.update(ind[x], arr2[x])
            str_result = self.query(0, len(arr1))
            str_result = str_result.replace(",", "")
            result = re.sub(r'[a-zA-Z]', ',', str_result)
            if (len(str_result) == 1):
                arr_result.append(1)
            else:
                yyy = str(result)
                digit = yyy.split(',')
                arr_digit = digit.pop(len(digit) - 1)
                af_st = sorted(digit, key=int, reverse=True)
                arr_result.append(int(af_st[0]))
            
        #"""
        return arr_result
        
    def _build(self, data, tree_idx, start, end):
        """Recursively builds the tree by splitting the array in halves."""
        if start == end:
            self.tree[tree_idx] = data[start]
            return
        
        mid = (start + end) // 2
        left_child = 2 * tree_idx
        right_child = 2 * tree_idx + 1
        
        self._build(data, left_child, start, mid)
        self._build(data, right_child, mid + 1, end)
        
        self.__order_text(tree_idx, left_child, right_child)
        
        # Merge step (Change this to min() or max() for other variations)
       
        #self.tree[tree_idx] = min(self.tree[left_child], self.tree[right_child])

    def update(self, index, value):
        """Public method to update a specific index in the original array."""
        if (len(self.tree) == 1):
            self.tree = value
        else:
            self._update(1, 0, self.n - 1, index, value)

    def _update(self, tree_idx, start, end, index, value):
        """Traverses down to the leaf node, updates it, and re-evaluates parents."""
        if start == end:
            self.tree[tree_idx] = value
            return
            
        mid = (start + end) // 2
        left_child = 2 * tree_idx
        right_child = 2 * tree_idx + 1
        
        if index <= mid:
            self._update(left_child, start, mid, index, value)
        else:
            self._update(right_child, mid + 1, end, index, value)
            
        self.__order_text(tree_idx, left_child, right_child)
        #self.tree[tree_idx] = f"{self.tree[left_child]}{self.tree[right_child]}"

    def query(self, left, right):
        """Public method to query the inclusive range [left, right]."""
        if (len(self.tree) == 1):
            query_str = self.tree
            return query_str
        else:
            return self._query(1, 0, self.n - 1, left, right)

    def _query(self, tree_idx, start, end, left, right):
        """Finds segments that overlap with the targeted range."""
        
        # Case 1: Complete overlap
        if left <= start and end <= right:
            return self.tree[tree_idx]
            
        # Case 2: No overlap
        if end < left or start > right:
            return 0  # Identity element (0 for sum, inf for min, -inf for max)
            
        # Case 3: Partial overlap
        mid = (start + end) // 2
        left_sum = self._query(2 * tree_idx, start, mid, left, right)
        right_sum = self._query(2 * tree_idx + 1, mid + 1, end, left, right)
        __str = f"{left_sum}P{right_sum}"
        return __str
    
    def __order_text(self,tree_idx, left, right):
        
        left_text = self.tree[left]
        right_text = self.tree[right]
        tree_string = ""
        tmp_left_len = len(left_text)
        tmp_right_len = len(right_text)

        if (tmp_left_len == 1 and tmp_right_len == 1):
            if (left_text == right_text):
                self.tree[tree_idx] = f"2,{left_text}"
            else:
                self.tree[tree_idx] = f"1,{left_text},1,{right_text}"
        else:
            __count = 0
            __tmp_text = ""

            if (tmp_right_len == 1):
                __tmp_text = f"1,{right_text[0]}"
            else:
                __tmp_text = right_text
            
            left_array = left_text.split(",")
            right_array = __tmp_text.split(",")  
                      
            #__tmp_len = len(__tmp_text)
            left_len = len(left_array)
            right_len = len(right_array)

            if (left_array[left_len - 1] == right_array[1]):
                __count = int(left_array[left_len - 2]) + int(right_array[0])
                if (left_len == 4 and right_len == 4):
                    #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{__tmp_text[1:4]}" #2a4b1o
                    tree_string = f"{left_array[0]},{left_array[1]},{__count},{right_array[1]},{right_array[2]},{right_array[3]}"
                elif (left_len == 6 and right_len == 6):
                    if (int(left_array[2]) >= __count and int(left_array[2]) >= int(right_array[2])): # left second value have hightest
                        #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[__tmp_len - 2:__tmp_len]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[right_len - 2]},{right_array[right_len - 1]}"
                    elif (int(right_array[2]) >= __count and int(right_array[2]) >= int(left_array[4])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    elif (__count >= int(left_array[2]) and __count >= int(right_array[2])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{left_text[5:6]}{__tmp_text[4:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{__count},{left_array[5]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[4:6]}"
                        tree_string = "" f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                elif (left_len == 4 and right_len == 6):
                    if (__count >= int(right_array[2])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{__tmp_text[1:2]}{__tmp_text[4:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{__count},{right_array[1]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text}{__tmp_text[4:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                elif (left_len == 6 and right_len == 4):
                    if (__count >= int(left_array[2])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{left_text[5:6]}{__tmp_text[2:4]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{__count},{left_array[5]},{right_array[2]},{right_array[3]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[2:4]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}"
                elif (left_len == 2 and right_len == 4):
                    #self.tree[tree_idx] = f"{__count}{left_text[1]}{__tmp_text[2:4]}"
                    tree_string = f"{__count},{left_array[1]},{right_array[2]},{right_array[3]}"
                elif (left_len == 4 and right_len == 2):
                    #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{__tmp_text[1]}"
                    tree_string = f"{left_array[0]},{left_array[1]},{__count},{right_array[1]}"
                elif (left_len == 6 and right_len == 2):
                    tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{__count},{left_array[5]}"
                elif (left_len == 2 and right_len == 6):
                    tree_string = f"{__count}{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                else:# (left_len == 2 and __tmp_len == 2):
                    #self.tree[tree_idx] = f"{__count}{left_text[1]}"   
                    tree_string = f"{__count},{left_array[1]}"         
            else:
                """
                print("888888888")
                print(left_text[left_len - 2])
                print(__tmp_text[0])
                """
            if (left_array[left_len - 1] == right_array[1]):
                __count = int(left_array[left_len - 2]) + int(right_array[0])
                if (left_len == 4 and right_len == 4):
                    #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{__tmp_text[1:4]}" #2a4b1o
                    tree_string = f"{left_array[0]},{left_array[1]},{__count},{right_array[1]},{right_array[2]},{right_array[3]}"
                elif (left_len == 6 and right_len == 6):
                    if (int(left_array[2]) >= __count and int(left_array[2]) >= int(right_array[2])): # left second value have hightest
                        #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[__tmp_len - 2:__tmp_len]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[right_len - 2]},{right_array[right_len - 1]}"
                    elif (int(right_array[2]) >= __count and int(right_array[2]) >= int(left_array[4])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    elif (__count >= int(left_array[2]) and __count >= int(right_array[2])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{left_text[5:6]}{__tmp_text[4:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{__count},{left_array[5]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[4:6]}"
                        tree_string = "" f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                elif (left_len == 4 and right_len == 6):
                    if (__count >= int(right_array[2])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{__tmp_text[1:2]}{__tmp_text[4:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{__count},{right_array[1]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text}{__tmp_text[4:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                elif (left_len == 6 and right_len == 4):
                    if (__count >= int(left_array[2])):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{left_text[5:6]}{__tmp_text[2:4]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{__count},{left_array[5]},{right_array[2]},{right_array[3]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[2:4]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}"
                elif (left_len == 2 and right_len == 4):
                    #self.tree[tree_idx] = f"{__count}{left_text[1]}{__tmp_text[2:4]}"
                    tree_string = f"{__count},{left_array[1]},{right_array[2]},{right_array[3]}"
                elif (left_len == 4 and right_len == 2):
                    #self.tree[tree_idx] = f"{left_text[0:2]}{__count}{__tmp_text[1]}"
                    tree_string = f"{left_array[0]},{left_array[1]},{__count},{right_array[1]}"
                elif (left_len == 6 and right_len == 2):
                    tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{__count},{left_array[5]}"
                elif (left_len == 2 and right_len == 6):
                    tree_string = f"{__count},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                else:# (left_len == 2 and __tmp_len == 2):
                    #self.tree[tree_idx] = f"{__count}{left_text[1]}"   
                    tree_string = f"{__count},{left_array[1]}"         
            else:
                """
                print("888888888")
                print(left_text[left_len - 2])
                print(__tmp_text[0])
                """
                if (int(left_array[left_len - 2]) < int(right_array[0])):
                    if (left_len == 4 and right_len == 4):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text}"
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 6 and right_len == 4):
                        if (int(left_array[2]) <= int(right_array[0])):
                            #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text}"
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[2]},{right_array[3]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[2:4]}" 
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}" 
                    elif (left_len == 6 and right_len == 6):
                        if (int(left_array[2]) >= int(right_array[0]) and int(left_array[2]) >= int(right_array[2])): # left second value have hightest
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[__tmp_len - 2:__tmp_len]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                        elif (int(left_array[2]) <= int(right_array[2]) and  int(right_array[0]) <= int(right_array[2])): #right second value have hightest
                            #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                        elif (int(right_array[0]) >= int(left_array[2]) and int(right_array[0]) >= int(right_array[2])):
                            #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[0:2]}{__tmp_text[4:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[4]},{right_array[5]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[4:6]}" # second value of left and right are equeal and more than __tmp_text[0]
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]}.{right_array[4]},{right_array[5]}"
                    elif (left_len == 4 and right_len == 6):
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    elif (left_len == 2 and right_len == 4):
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 4 and right_len == 2):
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]}"
                    elif (left_len == 6 and right_len == 2):
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[0]},{right_array[1]}"
                    elif (left_len == 2 and right_len == 6):
                        if (int(right_array[0]) >= int(right_array[2])):
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[4]},{right_array[5]}"
                        else:
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text}{right_text}"
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]}"
                        
                elif (left_array[left_len - 2] > right_array[0]):########################################## >>>>>>>>
                    
                    if (left_len == 4 and right_len == 4):
                        #self.tree[tree_idx] = f"{left_text}{__tmp_text[__tmp_len - 2:__tmp_len]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 6 and right_len == 4):
                        if (int(left_array[2]) >= int(left_array[4])):
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[2:4]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text[0:2]}{left_text[4:6]}{__tmp_text[2:4]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[4]},{left_array[5]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 6 and right_len == 6):
                            if (int(left_array[2]) >= int(left_array[4]) and int(left_array[2]) >= int(right_array[2])):
                                
                                #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[4:6]}"
                                tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                            elif (int(right_array[2]) >= int(left_array[4]) and int(right_array[2]) >= int(left_array[2])):
                                
                                #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                                tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                            elif (int(left_array[4]) >= int(left_array[2]) and int(left_array[4]) >= int(right_array[2])):
                                #self.tree[tree_idx] = f"{left_text[0:2]}{left_text[4:6]}{__tmp_text[4:6]}"
                                
                                tree_string = f"{left_array[0]},{left_array[1]},{left_array[4]},{left_array[5]},{right_array[4]},{right_array[5]}"
                            else:
                                
                                #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[4:6]}" # second value of left and right are equeal and more than left_text[left_len - 2
                                tree_sting = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                    elif (left_len == 4 and right_len == 6):
                        if (int(left_array[2]) >= int(right_array[2])):
                            #self.tree[tree_idx] = f"{left_text}{__tmp_text[4:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    elif (left_len == 2 and right_len == 4):
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 4 and right_len == 2):
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[0]},{right_array[1]}"
                    elif (left_len == 6 and right_len == 2):
                        if (int(left_array[2]) >= int(left_array[4])):
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[0]},{right_array[1]}"
                        else:
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[4]},{left_array[5]},{right_array[0]},{right_array[1]}"
                    elif (left_len == 2 and right_len == 6):
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text}{__tmp_text[__tmp_len - 2:__tmp_len]}"  
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]}"
                else: # equal
                    if (left_len == 4 and right_len == 4):
                        #self.tree[tree_idx] = f"{left_text}{__tmp_text[__tmp_len - 2:__tmp_len]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 6 and right_len == 6):
                        if (int(left_array[2]) >= int(right_array[0]) and int(left_array[2]) >= int(right_array[2])): # left second value have hightest
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[__tmp_len - 2:len(__tmp_text)]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                        elif (int(right_array[2]) >= int(left_array[2]) and int(right_array[2]) >= int(left_array[4])):
                            #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[2:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                        elif (int(left_array[4]) >= int(left_array[2]) and int(left_array[4]) >= int(right_array[2])):
                            #self.tree[tree_idx] = f"{left_text[0:2]}{left_text[4:6]}{__tmp_text[4:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[4]},{left_array[5]},{right_array[4]},{right_array[5]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[4:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                    elif (left_len == 4 and right_len == 6):
                        if (int(right_array[0]) >= int(right_array[2])):
                            #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[0:2]}{__tmp_text[4:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[4]},{right_array[5]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text}{__tmp_text[4:6]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[4]},{right_array[5]}"
                    elif (left_len == 6 and right_len == 4):
                        if (int(left_array[4]) >= int(left_array[2])):
                            #self.tree[tree_idx] = f"{left_text[0:2]}{left_text[4:6]}{__tmp_text[2:4]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[4]},{left_array[5]},{right_array[2]},{right_array[3]}"
                        else:
                            #self.tree[tree_idx] = f"{left_text[0:4]}{__tmp_text[2:4]}"
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 4 and right_len == 2):
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]}"
                    elif (left_len == 2 and right_len == 4):
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]}"
                    elif (left_len == 6 and right_len == 2):
                        if (int(left_array[2]) >= int(left_array[4])):
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[2]},{left_array[3]},{right_array[0]},{right_array[1]}"
                        else:
                            tree_string = f"{left_array[0]},{left_array[1]},{left_array[4]},{left_array[5]},{right_array[0]},{right_array[1]}"
                    elif (left_len == 2 and right_len == 6):
                        if (int(right_array[0]) >= int(right_array[2])):
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]},{right_array[4]},{right_array[5]}"
                        else:
                            tree_string = f"{left_array[0]},{left_array[1]},{right_array[2]},{right_array[3]},{right_array[4]},{right_array[5]}"
                    else:
                        #self.tree[tree_idx] = f"{left_text[0:2]}{__tmp_text[__tmp_len - 2:__tmp_len]}"
                        tree_string = f"{left_array[0]},{left_array[1]},{right_array[0]},{right_array[1]}"
            self.tree[tree_idx] = tree_string             
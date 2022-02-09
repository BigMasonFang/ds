import sys, os
# to import object from the parent folder's sub folder can use this way
sys.path.insert(0, '..')
from stack.stack import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """append means put the new node to the end of the single linked list

        Args:
            data ([type]): [description]
        """
        # first objectize the node desired to append
        new_node = Node(data)

        # if the list is empty, place the new node as the head
        if self.head is None:
            self.head = new_node
            # in there u must write the force the function to quit
            # if not doing so, at the end, the self.head.next will
            # point to it self, it becames a circle in line 38
            return

        # set the head as the current last node
        last_node = self.head

        # find the true last node by while using the condition
        # the last node's next is none
        while last_node.next is not None:
            # print('caught')
            last_node = last_node.next

        # the loop is over, append the new node to the last node
        last_node.next = new_node

    def print_list(self):
        """print the whole single linked list
        """
        # using while loop to print the whole list
        # the old way not use the property of None and
        # in brief, when the <x> is None, False, "", 0, [], {}, (), the while x is False
        # ======== the old way ========
        # # first check the list is empty or not
        # if self.head is None:
        #     print("")
        # else:
        #     # set the head as the first node
        #     current_node = self.head
        #     print(current_node.data)
        #     # start loop
        #     while self.head.next is not None:
        #         print(current_node.data)
        #         current_node = current_node.next
        # ======= the pythonic way =========
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def prepend(self, data):
        """prepend means insert the new node to the first place of the list

        Args:
            data ([type]): [description]
        """
        # no need to check if the list is empty
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node: Node, data):
        """given the prev_node, insert a new node after it

        Args:
            prev_node ([type]): [description]
            data ([type]): [description]
        """
        # same
        new_node = Node(data)

        # check if the prev_node is none
        if not prev_node:
            print('Previous node does not exist.')
            return

        # since given the node, no need to find
        # using while loop to get the desire node
        # curr_node = self.head
        # while curr_node.data != prev_node:
        #     curr_node = curr_node.next

        # once get the desire node, first set curr_node.next to new_node.next
        new_node.next = prev_node.next
        # then set the new_node to the current.next
        prev_node.next = new_node

    def delete_by_value(self, value):
        """delete the node by its value
        """
        # consider the edge condition: 1 head 2 tail 3 value did not match (important)
        # 4 list is empty

        # first set the head as the current node
        cur_node = self.head

        # this is to fulfill the condition 1 and 4
        if cur_node and self.head.data == value:
            self.head = self.head.next
            # ? set cur_node to none
            cur_node = None
            return

        # set it or not
        pre_node = None
        # this is conditon 2,3 and normal loop the list, if match the value, jump
        # here u must set the cur_node to meet #4 to jump the loop
        while cur_node and cur_node.data != value:
            pre_node = cur_node
            cur_node = cur_node.next

        # catch the #3
        if cur_node is None:
            print('value does not match')
            return

        # the normal case
        pre_node.next = cur_node.next

    def delete_by_position(self, index: int):
        """delete the node by index
        """
        # like delete_by_value
        # consider edge position #1 empty #2 head #3 index out of bound
        cur_node = self.head

        if index == 0 and cur_node:
            self.head = self.head.next
            return

        # normal case and #3, using decriment index as the conditioner
        while cur_node and index > 0:
            pre_node = cur_node
            cur_node = cur_node.next
            index -= 1

        # catch #3
        if cur_node is None:
            print('index out of bound')
            return

        # normal case
        pre_node.next = cur_node.next

    def len_iter(self):
        count = 0
        cur_node = self.head

        while cur_node:
            cur_node = cur_node.next
            count += 1

        return count

    def len_recursive(self, node: Node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap(self, value_1, value_2):
        """swap two nodes in the list by given value
        """
        # edge condition #1 head other #2 DNE(one or both) #3 vlaue same
        #4 empty list
        # check #3
        if value_1 == value_2:
            return

        # set nodes for value_1
        pre_node_1, cur_node_1 = None, self.head

        # iterate the list, first identify vlaue_1
        while cur_node_1 and cur_node_1.data != value_1:
            pre_node_1 = cur_node_1
            cur_node_1 = cur_node_1.next

        # set nodes for value_2
        pre_node_2, cur_node_2 = None, self.head

        # iterate the list, first identify vlaue_1
        while cur_node_2 and cur_node_2.data != value_2:
            pre_node_2 = cur_node_2
            cur_node_2 = cur_node_2.next

        # check #2 and #4
        if not cur_node_1 or not cur_node_2:
            return

        # this is the key to solve edge #1 and #4
        if pre_node_1:
            pre_node_1.next = cur_node_2
        else:
            # solve #1
            self.head = cur_node_2

        if pre_node_2:
            pre_node_2.next = cur_node_1
        else:
            # solve #1
            self.head = cur_node_1

        # the normal case
        cur_node_1.next, cur_node_2.next = cur_node_2.next, cur_node_1.next

    def reverse_iter(self):
        """reverse the list using iterative method
        """
        prev_node = None
        cur_node = self.head

        while cur_node:
            # 1
            # None(prev) A(cur) -> B(next)
            # prev: None
            # next: cur_node.next (data: B, next: None)
            # cur: self.head (data: A, next: B)
            # 2
            # None <- A(prev) B(cur) -> None
            # prev: data: A, next: None
            # next: None
            # cur: data: B, next: None
            next_node = cur_node.next

            # 1
            # None(prev) <- A(cur)  B(next)
            # prev: None
            # next: data: B, next: None
            # cur: data: A, next: prev
            # 2
            # None <- A(prev) <- B(cur) None(next)
            # prev: data: A, next: None
            # next: None
            # cur: data: B, next: prev
            cur_node.next = prev_node

            # 1
            # None <- A(prev/cur) B(next)
            # prev: data: A, next: prev
            # next: data: B, next: None
            # cur: data: A, next: prev
            # 2
            # None <- A() <- B(prev) None(next)
            # prev: data: B, next: prev
            # next: None
            # cur: data: B, next: prev
            prev_node = cur_node

            # 1
            # None <- A(prev) <- B(cur)
            # prev: data: A, next:None
            # next: prev
            # cur: data:B , next: None
            # 2
            # None <- A() <- B(prev) None(cur)
            # prev: data: B, next: prev
            # next: None
            # cur: None
            cur_node = next_node

        # don't forget the head should be None
        self.head = prev_node

    def reverse_recur(self):
        def _reverse_recur(cur_node: Node, prev_node: Node):
            if not cur_node:
                return prev_node
            # same as reverse_iter
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            return _reverse_recur(cur_node, prev_node)

        self.head = _reverse_recur(cur_node=self.head, prev_node=None)

    def merge_sorted(self, llist: object):
        """ link tow sorted llist and the result shoukd be sorted too
        first l thought the pointer at the the two list is ok but it eventually stuck
        instead create a new llist is more reasonable
        edge condition empty list
        """
        # set three pointer p,q,s
        p = self.head
        q = llist.head
        s = None

        # edge condition
        if not p:
            return q
        if not q:
            return p

        # set new head
        if q and p:
            if q.data <= p.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                # first make s point to the smaller one
                s.next = p
                # reassign the pointer s
                s = p
                # set the old small node pointer to the next node
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        # once a llist is iterated over, set the pointer next to the other
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def rm_duplicate(self):
        """rm duplicate node in the llist
        """
        # set
        cur = self.head
        prev = None
        duplicates = set()

        # loop
        while cur:
            if cur.data in duplicates:
                prev.next = cur.next
                # safety
                cur = None
            else:
                duplicates.add(cur.data)
                prev = cur

            # after the judgement, set it traverse or go on to next
            cur = prev.next

    def print_nth_from_last_1(self, n: int):
        """print the node with is nth from the last node
        this one first use l=len() then calculate act l-n next from the head
        edge conditon: 1 empty list 2 wrong n (exceed the length of list)

        better not use steps and < > in the while statement, use == inside is better
        Args:
            n (int): [description]
        """
        # set
        cur = self.head

        # acheive length
        l = self.len_iter()

        # act
        while cur:
            if l == n:
                print(cur.data)
                return (cur.data)
            cur = cur.next
            l -= 1
        if cur is None:
            print('index exceed length of the list')
            return

    def print_nth_from_last_2(self, n: int):
        """using double pointer to solve the problem
        that is set set two pointers with n nodes partioned, traverse the list
        when the right node reachs none, the left pointer is pointing the nth from last
        edge conditon: 1 empty list 2 wrong n (exceed the length of list)
        """
        p = self.head
        q = self.head
        """
        This is a wrong example, also adding constrains in while q and p part,
        but eventually it will output the head when index n exceed
        if n > 0:
            # set right pointer
            while q and n>0:
                q = q.next
                n -= 1
            # traverse the list
            while q and p:
                p, q = p.next, q.next
            # consider edge condition 
            if p:
                print(p.data)
            else:
                print('index exceed length of the list')
            
        else:
            print('wrong index given')
            return
        """
        if n > 0:
            # set right pointer and do the judgement
            # first set count variable to judge if q exceed
            count = 0
            while q:
                # set count first and the do the condition
                # key of this
                count += 1
                if count >= n:
                    break
                q = q.next

            # detect if q exceed
            if not q:
                print('index exceed length of the list')
                return

            # two pointer move
            while p and q.next:
                p, q = p.next, q.next
            print(p.data)
            return p.data

        else:
            return

    def count_occurance_iter(self) -> dict:
        """count the occurance of each element
        """
        # using dict as the ouput data structure
        result = {}

        cur = self.head

        while cur:
            if cur.data not in result.keys():
                result[cur.data] = 0
            result[cur.data] += 1
            cur = cur.next

        return result

    def count_single_occurance_iter(self, data) -> int:
        """count the occurance of given data
        """
        cur = self.head
        occ = 0

        while cur:
            if cur.data == data:
                occ += 1
            cur = cur.next

        print(occ)
        return occ

    def count_single_occurance_recur(self, node: Node, data) -> int:
        if node is None:
            return 0
        if node.data == data:
            node = node.next
            return 1 + self.count_single_occurance_recur(node, data)
        else:
            node = node.next
            return self.count_single_occurance_recur(node, data)

    def rotate(self, k: int):
        """rotate the llist by a pivot node
        acutally pivot is not the node but the its link to the next node
        1. find the pivot (or given)    
        2. set tail node's next to head node
        2. set the new head node, the new head node is the node next to pivot
        4. set pivot.next to None
        edge condition 1.empty list 2.wrong given pivot
        """
        if self.head and self.head.next:
            # in there, p and q stand for the pivot and the tail
            p, q = self.head, self.head
            count = 0
            # prev is the temporary variable
            prev = None

        # edge conditon catch while p
        while p and count < k:
            prev = p
            p, q = p.next, q.next
            count += 1
        # at the end of while, the p and q should be the node after pivot, prev is the pivot
        # so assign prev to p
        p = prev

        while q:
            prev = q
            q = q.next
        # sam as above, q is the tail
        q = prev

        # step 2
        q.next = self.head
        # step 3
        self.head = p.next
        # step 4
        p.next = None

    def copy(self):
        """make a copy of new llist
        """
        result = SingleLinkedList()
        p = self.head
        while p:
            result.append(p.data)
            p = p.next
        return result

    def is_palindrome(self, solution=1) -> bool:
        """
        radar: True
        sex: False
        """
        # Using string to solve it
        if solution == 1:
            # store the data of list into a string
            s = ''
            p = self.head
            while p:
                s += p.data
                p = p.next
            # using slicing technique of string to reverse
            return s == s[::-1]

        # Using stack to solve it
        if solution == 2:
            s = Stack()
            p = self.head
            # first we push the data to the stack
            while p:
                s.push(p.data)
                p = p.next
            # then we pop the element by checking if it is the same, if not break
            p = self.head
            while p:
                data = s.pop()
                if p.data != data:
                    return False
                p = p.next
            return True

        # Using double pointer to solve it
        if solution == 3:
            # set first pointer
            p = self.head

            # create a reversed list and second pointer
            s = self.copy()
            s.reverse_iter()
            q = s.head

            # check both list with both pointer
            while p and q:
                if p.data != q.data:
                    return False
                p, q = p.next, q.next
            return True

    def move_tail_to_head(self):
        # edge condition: 1 empty 2. single node
        # use double pointer
        # set
        p = self.head
        q = None

        while p:
            # detect if p is the last one
            if p.next == None:
                break
            q = p
            p = p.next
            # now p is the last node, q is the 1th to last

        # edge conditon
        if (p or q) is None:
            return

        # set p.next to head
        p.next = self.head
        # set q.next to self.head
        q.next = None
        # set p as self.head
        self.head = p

    def sum_two_lists(self, llist) -> object:
        """as digit form
        basic conditions 1 with addition 2 without additionn
        3 different length 4 empty
        """
        # double pointer of cause
        p = self.head
        q = llist.head
        result = SingleLinkedList()
        addition = 0

        while p and q:
            # add and setting phase
            data = p.data + q.data

            # check if there is a addition
            if addition:
                data = data + addition

            # check if the result is greater than 9
            # to add data, use append(), do not use assignment
            if data > 9:
                data = data - 10
                result.append(data)
                addition = 1
            else:
                result.append(data)
                addition = 0

            p, q = p.next, q.next

        #loop is over, check length
        if p and (not q):
            r1 = result.head
            while r1:
                r2 = r1
                r1 = r1.next
            r2.next = p

        if q and (not p):
            r1 = result.head
            while r1:
                r2 = r1
                r1 = r1.next
            r2.next = q

        # else:
        #     print('wrong input (empty llist)')

        return result


if __name__ == "__main__":
    llist = SingleLinkedList()
    llist_empty = SingleLinkedList()

    llist.append('a')
    llist.append('b')
    llist.append('c')
    llist.append('d')
    llist.append('e')
    llist.prepend('0')

    llist.insert_after_node(llist.head, 1)

    llist.delete_by_value('d')

    llist.delete_by_value('f')

    llist.delete_by_position(2)

    llist.delete_by_position(7)

    print('\n the element of the list are: ')
    llist.print_list()

    print('\nthe length of the list using iterative method:')
    print(llist.len_iter())
    # print(llist_empty.len_iter())

    print('\nthe length of the list using recursive method:')
    print(llist.len_recursive(llist.head))
    # print(llist_empty.len_recursive(llist_empty.head))

    print('\n swap b and e using swap')
    llist.swap('b', 'e')
    llist.print_list()

    print('\n reverse the list using iterative method:')
    llist.reverse_iter()
    llist.print_list()
    # back
    llist.reverse_iter()

    print('\n reverse the list using recursive method:')
    llist.reverse_recur()
    llist.print_list()
    # back
    llist.reverse_recur()

    print('\n merge sorted llist:')
    llist_a = SingleLinkedList()
    llist_a.append(1)
    llist_a.append(3)
    llist_a.append(4)
    llist_a.append(7)

    llist_b = SingleLinkedList()
    llist_b.append(1)
    llist_b.append(2)
    llist_b.append(5)
    llist_b.append(6)
    llist_b.append(6)
    llist_a.merge_sorted(llist_b)
    llist_a.print_list()

    print('\n remove dupplicates of llist a:')
    llist_a.rm_duplicate()
    llist_a.print_list()

    print('\n solution 1 get nth from the last of llist a:')
    llist_a.print_nth_from_last_1(5)

    print('\n solution 2 get nth from the last of llist a:')
    llist_a.print_nth_from_last_2(5)

    llist_c = SingleLinkedList()
    for i in [1, 2, 1, 3, 1, 4, 1, 5, 2, 3, 2, 4]:
        llist_c.append(i)
    print('\n count the occurance of all elments of llist c:')
    result = llist_c.count_occurance_iter()
    print(result)

    print(
        '\n count the occurance of given elements of using iterative method on llist c:'
    )
    result = llist_c.count_single_occurance_iter(1)
    print(
        '\n count the occurance of given elements of using recursive method on llist c:'
    )
    result = llist_c.count_single_occurance_recur(llist_c.head, 1)
    print(result)

    llist_d = SingleLinkedList()
    for i in [1, 2, 3, 4, 5]:
        llist_d.append(i)
    print('\n (Pesudo) rotate the llist given pivot: ')
    llist_d.rotate(3)
    llist_d.print_list()
    llist_d.rotate(2)
    llist_d.print_list()

    print('\n test copy function')
    llist_e = llist_d.copy()
    llist_e.print_list()

    print('\n check the palindrome func')
    llist_f_1 = SingleLinkedList()
    llist_f_2 = SingleLinkedList()
    for i, j in zip('checkbox', 'fuckcuf'):
        llist_f_1.append(i)
        llist_f_2.append(j)

    print('\n with solution 1 using string')
    print('is llist_f_1 palindrome?', llist_f_1.is_palindrome(solution=1))
    print('is llist_f_2 palindrome?', llist_f_2.is_palindrome(solution=1))
    print('\n with solution 2 using stack')
    print('is llist_f_1 palindrome?', llist_f_1.is_palindrome(solution=2))
    print('is llist_f_2 palindrome?', llist_f_2.is_palindrome(solution=2))
    print('\n with solution 1 using string')
    print('is llist_f_1 palindrome?', llist_f_1.is_palindrome(solution=3))
    print('is llist_f_2 palindrome?', llist_f_2.is_palindrome(solution=3))

    print('\n exercise move head to tail:')
    llist_g = llist_d.copy()
    llist_g.move_tail_to_head()
    llist_g.print_list()

    print('\n exercise sum two linked list:')
    llist_h = SingleLinkedList()
    for i in [5, 6, 3]:
        llist_h.append(i)
    llist_i = SingleLinkedList()
    for i in [8, 4, 2]:
        llist_i.append(i)
    llist_j = llist_h.sum_two_lists(llist_i)
    llist_j.print_list()

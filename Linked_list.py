class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
 
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.next.prev = itr
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
    
    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                if itr.next.next:
                    itr.next.next.prev = itr
                itr.next = itr.next.next
                return
            itr = itr.next
            
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        lst = ""
        while itr:
            lst += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print(lst)
            
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        lst = ""
        while itr:
            lst += str(itr.data) + " <-- " if itr.prev else str(itr.data)
            itr = itr.prev
        print(lst)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.print_forward()
    ll.print_backward()

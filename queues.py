class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def enqueue(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length += 1

    def dequeue(self):
        if self.length==0: return None
        temp = self.first
        if self.length > 1:
            self.first=temp.next
            temp.next=None
        else:
            self.first=None
            self.last=None
        self.length -= 1
        return temp

    def print_queue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next

my_queue=Queue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
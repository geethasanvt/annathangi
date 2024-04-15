class Queue:

     def  __init__(self):
        self.qlist=list()

     def isEmpty (self):
        return len(self) == 0

     def  __len__(self):
        return len(self.qlist)

     def enqueue(self,item):
        self.qlist.append(item)

     def dequeue(self):
        assert not self.isEmpty(),"cannot dequeue from an empty queve."
        data=self.qlist.pop(0)
        return data

     def  display(self):
        print(self.qlist)

q=Queue()
print("contents of queue")
q.display()
print("enque operations")
q.enqueue(25)
q.enqueue(50)
q.enqueue(75)
q.enqueue(100)
print("contents of  Queue")
q.display()
print("Deque operations")
print(q.dequeue()," is removed from queue")
print(q.dequeue()," is removed from queue")
print("contents of Queue")
q.display()

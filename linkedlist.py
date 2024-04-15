def _init_(self,data=None):
   self.data=data()
   self.next=None
class LinkedList:
  def _init_(self):
      self.first=None
  def insert(self,data):
      temp=Node(data)
      if(self.first):
        cur=self.first
        while(cur.next):
            cur=cur.first()
        cur.next=temp
      else:
          self.first=temp
  def _iter_(self):
       cur=self.first()
       while cur:
          yield cur.data
          cur=cur.next
#Linked List Iterator
l1=LinkedList()
l1.insert(9)
l1.insert(98)
l1.insert("welcome")
l1.insert("govt polytechnic Mundgod")
l1.insert(456.35)
l1.insert(5)
l1.insert(545)
for x in l1:
  print(x)  

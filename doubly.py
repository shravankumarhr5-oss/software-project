class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublylinked:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
    def insert_begin(self,data):
        nb=node(data)
        nb.data=data
        nb.next=self.head
        self.head.prev=nb
        self.head=nb
    def insert_end(self,data):
        ne=node(data)
        ne.data=data
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.prev=next
    def insert_pos(self,data):
        np=node(data)
        np.data=data
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            np.prev=temp
            np.next=temp.next
        temp.next.prev=np
        temp.next=np
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
        
    def delete_end(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.before=None
    def delete_pos(self,pos):
        temp=self.head
        if pos==0:
            self.head=temp.next
            temp.next=None
        else:
            temp=self.head.next
            before=self.head
            for i in range(pos-1):
                temp=temp.next
                before=before.next
            before.next=temp.next
            temp.next.prev=before
            temp.next=None
            temp.prev=None
    
    def search(self,key):
        pos=0
        flag=0
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp is not None:
                if temp.data==key:
                    print("the key element present at ",pos)
                    flag=1
                temp=temp.next
                pos=pos+1
        if flag==0:
            print(" the key element is not present in linked list")
        
    def size(self):
        count=0
        temp=self.head
        while temp is not None:
            count=count+1
            temp=temp.next
        print("length of linked list is ",count)
    
           
    
        

l1=doublylinked()
l1.display()
n1=node(10)
l1.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n4=node(40)
n3.next=n4
n5=node(50)
n4.next=n5
l1.display()
print("\n")
while True:
    ch=int(input("\n enter the element to insert\n 1.insert_beign\n 2.insert_end\n3.insert_pos\n4.delete_beign\n5.delete_end\n6.delete_pos\n7.search\n8.size\n9.display\n10.exit\n"))
    if(ch==1):
        item=int(input("enter the item"))
        l1.insert_begin(item)
        l1.display()
    elif(ch==2):
        item=int(input("enter the item"))
        l1.insert_end(item)
        l1.display()
    elif(ch==3):
        pos=int(input("enter the position"))
        item=int(input("enter the item"))
        l1.insert_pos(item)
        l1.display()
    elif(ch==4):
        l1.delete_begin()
        l1.display()
    elif(ch==5):
        l1.delete_end()
        l1.display()
    elif(ch==6):
        pos=int(input("enter the position"))
        l1.delete_pos(pos)
        l1.display()
    elif(ch==7):
        key=int(input("enter the key element  search"))
        l1.search(key)
        l1.display()
    elif(ch==8):
        l1.size()
        l1.display()
    elif(ch==9):
        l1.display()
    else:
        break
    



        

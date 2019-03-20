def stack():
	s=[]
	return (s)
def push(s,data):
	s.append(data)
def pop(s):
	data=s.pop()
	return(data)
def peek(s):
	return(s[len(s)-1])
def isEmpty(s):
	return(s==[])
def size(s):
	return(len(s))
    
def createqueues():
    q=[]
    return(q)
def enqueues(q,data):
    q.insert(0,data)
    return(q)
def dequeues(q):
    data = q.pop()
    return(data)
def isEmpty(q):
    return(q==[])
def size(q):
    return(len(q))

def createDeques():
    d=[]
    return(d)
def addFront(d,data):
    d.insert(0,data)
    return(d)
def removeFront(q):
    data = d.pop(0)
    return(data)
def addRear(d,data):
    d.append(data)
def removeRear(d):
    data=d.pop()
    return(data)
def isEmpty(d):
    return(d==[])
def size(d):
    return(len(d))

class BilKomp:
    def __init__(self,a,b):
        self.real=a
        self.imj=b
    def display(self):
        a=self.real
        b=self.imj
        temp=str(self.real)+'+'+str(self.imj)+'i'
        return(temp)
    def __str__(self):
        return str(self.real)+"+"+str(self.imj)+"i"
    def addNum(self,a,b):
        self.real=a.real+b.real
        self.imj=b.imj+b.imj
    def addNum1(self,a):
        self.real=self.real+a.real
        self.imj=self.imj+a.imj
    def addKomp(self,ob):
        c=self.real+ob.real
        d=self.imj+ob.imj
        return BilKomp(c,d)
    def __add__(self, ob):
        a=self.real+ob.real
        b=self.imj+ob.imj
        return BilKomp(a,b)
    def __mul__(self, ob):
        a=self.real*ob.real
        return a
        b=self.real*ob.imj
        return b
        c=self.imj*ob.real
        return c
        d=self.imj*ob.imj
        return d
        e=b+"+"+c
        return BilKomp(e,f)

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        else:
            previous.setNext(current.getNext())

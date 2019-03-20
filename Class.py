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
data1=BilKomp(4,1)
print(data1)
data2=BilKomp(2,4)
data=BilKomp(2,3)
data.addKomp(data2)
data.addNum1(data2)
c=data1*data2
print(c)


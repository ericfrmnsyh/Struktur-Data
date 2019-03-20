"""
Linked List
bisa nambah data
bisa delete data
bisa insert data di tengah - tengah
sifatnya dinamis(bisa berubah- ubah)

Node
Linked List
Penambahan data dalam linked list
Traversal Linked List
Ordered List

Informasi yang menunjuk lokasi data pertama dinamakan head
node berisi dua informasi yaitu data dan ponter

Untuk mengetahui ukuran dari list, diperlukan tahapan traverse, yaitu menelusuri setiap node yang terdapat pada linked list

InsertPrevious, menambahkan node baru sebelum node tertentu
InsertNext, menambahkan node baru setelah node tertentu
"""
from ModulSMT2 import*

        
        
a = Node(93)
b = Node(20)
c = Node(45)
a.setNext(b)
b.setNext(c)
mylist=LinkedList()
mylist.add(45)
mylist.add(90)
mylist.size()
print(mylist.search(45))

"""
class Person :
    name = ""
    age = 0
    tel = ''

    
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.tel = c

    def printname(self):
        print(self.name)

    def printage(self):
        print(self.age)

    def printtel(self):
        print(self.tel)        


    # def greeting(self):
    #     print(self.hello)

    def sum(self, a, b):
        return a + b

# obj = Person()        
# obj.greeting()
"""

a = [1,2,3,4,5]

a.append(6)  #추가 [1,2,3,4,5,6]
a.insert(0,7)  #추가 [7,1,2,3,4,5,6]
a.remove(6) #6을 찾아서 삭제 [7,1,2,3,4,5]
del a[1]  #삭제 [7,2,3,4,5]

b = []
for i in range(5):
    b.append( ['i', '가나다', 34 ])
print(b) #[ [0,"가나다", 34], [0,"가나다", 34], [0,"가나다", 34], [0,"가나다", 34]]
del b[0]  # 첫번째 [] 없어짐
print()

for a1, a2, a3 in b :
    print(a1,a2,a3)
print()

for i in range(0, len(b), 1) :  #인덱스 개념
    x,y,z = b[i] 
    print(x,y,z)

# 1 => 12345
# 2 => 1234
# 3 => 123
# 4 => 12
# 5 => 1


"""
for i in range(1,6,1):    #  1    2     3   4   5 
    for j in range(1,7-i,1): # 1234 1234  123 12  1
        print(i, end=" ")         #여기까지 끝나야 또 돈다.
    print()
print()

a = [ 
    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9],
    [10,11,12]
    ]


for i in range(0,4,1) :  
    for j in range(0,3,1) :
        print( i[i][j] )
        

s=0
for i in a :
    print(i[0])
    s = s + i[0]  s += i[0]
"""
"""
a = [
    {"aaa":1, "bbb":2, "ccc":[3,4,5]},
    {"aaa":11,"bbb":21,"ccc":[31,32,33]},
    {"aaa":21,"bbb":22,"ccc":[41,42,43]},
    {"aaa":31,"bbb":23,"ccc":[51,52,53]},
    ]


s = 0
for i in a :
    # print(i["ccc"])    
    for j in i["ccc"] :  # s = s+i["ccc"][0]
        print(j)
        s = s+j
print(s)     #["ccc"]12개의 합
"""


a = [
    {"aaa":1, "bbb":2, "ccc":[ [3,  4], [5,6]   ]},
    {"aaa":11,"bbb":21,"ccc":[ [31,32], [33,45] ]},
    {"aaa":21,"bbb":22,"ccc":[ [41,42], [43,41] ]},
    {"aaa":31,"bbb":23,"ccc":[ [51,52], [53,34]  ]},
    ]


s = 0
for i in a : 
    # print(i["ccc"])      #[[],[]]   [[],[]]   [[],[]]   [[],[]]  
    # print()
    for j in i["ccc"][0] :  # s = s+i["ccc"][0]
        print(j)
        s += j  #==  s = s + j
print(s)     #["ccc"]12개의 합
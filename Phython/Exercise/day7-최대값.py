#최대값 구하기
a = [3,56,7,89,23]
max = a[0]
maxi = 0
for i,t in enumerate(a) :
    if max < t :
        max = t
        maxi = i
print(max, maxi)
###########


#최소값 구하기
min = a[0]
mini = 0
for m,n in enumerate(a):
    if min > n :
        min = n
        mini = m
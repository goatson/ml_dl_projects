import pandas as pd

a = [ ['', 14], ["bbb", 24], ["ccc", 34] ]

df = pd.DataFrame(a, columns = ['name', 'age'])
# 빈 문자열을 찾아서 None으로 변경하시오.
for i, t in enumerate(a):
    print(i, t)
    if t[0] == '':
        a[i][0] = None

print(df)
print(df.isnull())  #None 확인




print(df.describe())  #min, max, std, count, mean ...
"""
print(df.shape)

#data = [1, 3, 5, 6, 11, 15, 18]


print(df['age'])





# b = {
#     "name":['kim','lee','kang','choi'],
#      "year":[2013, 2014, 2015, 2016],
#      "points":[1.5, 1.7, 1.8, 1.9]}

# df1 = pd.DataFrame(b)
# print(df1)






# 파이썬기초 -> 자료구조(리스트, 딕셔너리) -> numpy ->
# pandas (series, dataframe) ->
# 전처리(비즈니스 이해 -> 데이터의 이해 -> 데이터 정제)
#

"""
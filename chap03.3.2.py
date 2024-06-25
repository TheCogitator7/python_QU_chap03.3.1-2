import pandas as pd

dict_data={'col1' : [1, 2, 3], 'col2' : [4, 5, 6], 'col3' : [7, 8, 9]}
df=pd.DataFrame(dict_data)

print(df)
print()
print()

print(type(df))
print()
print()

df2=pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df2)
print()
print()


df3=pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['index1', 'index2', 'index3'], columns=['col1', 'col2', 'col3'])
print(df3)
print()
print()

df3.index=['row1', 'row2', 'row3']
df3.columns=['c1', 'c2', 'c3']

print(df3)
print()
print()

df3.rename(index={'row1' : 'r1'}, inplace=True)
df3.rename(columns={'c1' : 'columns1'}, inplace=True)

print(df3)
print()
print()

df3.drop('row3', axis=0, inplace=True)
df3.drop('c3', axis=1, inplace=True)

print(df3)
print()
print()



dict_data={'col1' : [1, 2, 3, 4], 'col2' : [5, 6, 7, 8], 'col3' : [9, 10, 11, 12], 'col4' : [13, 14, 15, 16]}
df=pd.DataFrame(dict_data, index=['index1', 'index2', 'index3', 'index4'])

print(df)
print()
print()

print(df['col1'])
print()
print()

print(df.col1)
print()
print()

print(type(df['col1']))
print()
print()

print(df[['col1']])
print()
print()

print(type(df[['col1']]))
print()
print()

print(df[['col1', 'col2']])
print()
print()

#행을 선택하는 방법

print(df.loc['index1'])
print()
print()

print(df.iloc[0])
print()
print()

print(type(df.loc['index1']))
print()
print()

print(df.loc[['index1']])
print()
print()

print(df.iloc[[0]])
print()
print()

print(df.loc['index1':'index3'])
print()
print()

print(df.iloc[0:2])
print()
print()

print(df.loc['index1', 'col1'])
print()
print()

print(df.loc[['index1', 'index3'], ['col1', 'col4']])
print()
print()

print(df.loc['index1':'index3', 'col1':'col3'])
print()
print()

print(df.iloc[0, 0])
print()
print()

print(df.iloc[[0, 2], [0, 3]])
print()
print()

print(df.iloc[0:2, 0:3])
print()
print()

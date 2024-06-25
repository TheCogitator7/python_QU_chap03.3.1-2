import pandas as pd

dict_data={'a':1, 'b':2, 'c':3}
series=pd.Series(dict_data)

print(series)
print()

print(type(series))
print()

print(series.index)
print()

print(series.values)
print()
print()



list_data=['a', 'b', 'c']
series_2=pd.Series(list_data)

print(series_2)
print()
print()


series_3=pd.Series(list_data, index=['index1', 'index2', 'index3'])
print(series_3)
print()
print()

capital=pd.Series({
    'Korea' : 'Seoul', 
    'Japan' : 'Tokyo',
    'China' : 'Beijing',
    'India' : 'New Delhi',
    'Taiwan' : 'Taipei',
    'Singapore' : 'Singapore'
    })

print(capital)
print()

print(capital['Korea'])
print()

print(capital[['Korea', 'Taiwan']])
print()

print(capital[0])#Seoul
print()

print(capital[[0, 3]])
print()

print(capital[0:3])
print()




series_1=pd.Series([1, 2, 3])
series_2=pd.Series([4, 5, 6])

print(series_1 + series_2)
print()

print(series_1 * 2)
print()





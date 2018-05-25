import matplotlib.pyplot as plt
import pandas as pd

## Simple
# data = pd.DataFrame({
#     'names': ['Den', 'Jane', 'Kate', 'Mike'],
#     'ages': [12, 23, 34,45],
#     'country': ['RU', 'UK', 'JP', 'US'],
#     'salary': [60000, 41000, 54600, 90000]
# }, index=['D', 'J', 'K', 'M'])
# print(data, '\n---')
# print(data.iloc[1], '\n---')
# data.index.name = 'First'
# print(data)
# print(data[['names', 'salary']])
# data['job'] = ['QA', 'Bank', 'IT', 'Sales']
# print(data)
# data.to_csv('employees.csv')
# df = pd.read_csv('employees.csv', sep=',')
# print(df)


## Titanic
# data = pd.read_csv('titanic.csv', sep=',')

# print(data[data.Survived == 1][['Name', 'PClass', 'Age']])
# print(data.groupby(['Sex', 'Survived'])['PassengerID'].count())

## Apple
data = pd.read_csv('apple.csv', sep=',', index_col='Date' , parse_dates=True)
data.sort_index()
m = data.loc['2015-Feb':'2012-Feb', 'Close'].mean()

print(data[data['Close'] > m])

new_sample_df = data.loc['2017-Feb':'2012-Feb', ['Adj Close']]
new_sample_df.plot()
plt.show()
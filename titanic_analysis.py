import pandas as pd

data = pd.read_csv(r"D:\pythonInternship\project1\titanic.csv")
# print(data.shape)
# data.info()
# print(data.describe())

data.drop(['PassengerId', 'Name'], inplace=True, axis=1)

survived = data['Survived'].tolist()
siblings = data['SibSp'].tolist()
price_ticket = data['Fare'].tolist()
age = data['Age'].tolist

print("Max of number of survived people:", survived.count(1))
print("Min of number of survived people: :", survived.count(0))
print("Max of siblings :", data['SibSp'].max())
print("Min of siblings :", data['SibSp'].min())
print("Max of price_ticket :", data['Fare'].max())
print("Min of price_ticket :", data['Fare'].min())
print("Max of Age :", data['Age'].max())
print("Min of Age :", data['Age'].min())

print(age)
print(survived)
print(siblings)
print(price_ticket)



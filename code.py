import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Welcome, Let's discover some Forest Fires in Brazil 'Amazon'")
#Make DateFrame for data inside CSV
data = pd.read_csv('amazon.csv', encoding="ISO-8859-1")
#Print First 5 rows of data
print("Let's See some rows\n" , data.head())
print("--------------------")
#Know our Data types inside our DataFrame
print("The Data Type we have\n" , data.dtypes)
print("--------------------")
#Quick look into our data
print("Some statistics\n" , data.describe())
print("--------------------")
print("Let's See some graph to detect which year had more fires")
sns.lineplot(data=data,x='year',y='number')
plt.show()

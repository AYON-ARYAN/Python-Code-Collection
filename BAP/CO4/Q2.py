import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

a=pd.read_csv('/Volumes/DRIVE/loan.csv')
# print (a)
#1 histogram
print(sns.histplot(data=a,x='Income'))
plt.show()
# 2 heatmap
numeric_columns = a.select_dtypes(include=['float64', 'int64'])#because corr cannot be calculated for text coloumn
cor = numeric_columns.corr()
sns.heatmap(data=cor)
plt.show()
#3 Swarm plot
group_male=a.groupby('Gender')
sns.swarmplot(x='Gender', y='Income', data=a)
plt.show()
#4 swarmn
male_female_data = a.loc[a['Gender'].isin(['Male', 'Female'])]
sns.swarmplot(x='Gender', y='Income', data=male_female_data)
plt.show()
#5 line plot
sns.lineplot(x='Income',y='Loan Amount',data=a)
plt.show()
#6 Bar Graph
gender_count = a['Gender'].value_counts()
sns.barplot(x=gender_count.index, y=gender_count.values)
plt.show()
#7 Bar Graph gaduate or not
grad_count = a['Education'].value_counts()
sns.barplot(x=grad_count.index, y=grad_count.values)
plt.show()
#8 bar graph avg income
grouped_data = a.groupby('Gender')
avg_income_by_gender = grouped_data['Income'].mean().reset_index()
sns.barplot(x='Gender', y='Income', data=avg_income_by_gender)
plt.show()


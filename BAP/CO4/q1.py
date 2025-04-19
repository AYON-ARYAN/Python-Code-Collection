import pandas as pd
csv_name=('/Volumes/DRIVE/SEMESTER1/DATA ANALYTICS WITH PYTHON/Iris - Iris.csv')
a=pd.read_csv(csv_name)
#average of petal length
z=a['PetalLengthCm'].mean()
print(f"The average of Petal Length: {z}")
#average of petal width
j=a['PetalWidthCm'].mean()
print(f"The average of petal width: {j}")
#average of sepal length
k=a['SepalLengthCm'].mean()
print(f"The average of sepal length: {k}")
#average of sepal width
l=a['SepalWidthCm'].mean()
print(f"The average of sep[al width: {l}")
# Group data by species
grouped = a.groupby('Species')

# Calculate averages for each species
averages = grouped.mean()

# Print averages
print("Average measurements for each species:")
print(averages)
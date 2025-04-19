import pandas as pd

# Load your data into a DataFrame
data = pd.read_csv("/Users/ayon_aryan/Downloads/ReactionTypes.csv")

# Remove rows with missing values
data = data.dropna()

# Save the cleaned data to a new CSV file
data.to_csv("cleaned_reactiontype.csv", index=False)
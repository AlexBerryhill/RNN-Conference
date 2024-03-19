import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("data/conference_talks.csv")

# Extract the values of the "talk" column
talk_values = df['talk'].tolist()

# Write the values to a text file
with open("talk_values.txt", "w", encoding="utf-8") as file:
    for talk in talk_values:
        file.write(str(talk) + "\n")

print("Text file with talk values has been created.")

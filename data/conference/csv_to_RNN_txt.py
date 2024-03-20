import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("data/conference/conference_talks.csv")

# Extract the values of the "talk" column
talk_values = df['talk'].tolist()

# Define the characters to remove
chars_to_remove = ['#', '$', '%', '&', '*', '+','=','[', ']', '_','\xa0', '¡', '¢', '©', '®', '°', '·', '½', '¿', 'æ', 'ø','̀', '́', '̂', '̃', '̈', '̌', '̧','™', 'ﬁ', '\ufeff' ]

# Create a translation table that maps each character to None
trans_table = str.maketrans({key: None for key in chars_to_remove})

# Write the values to a text file
with open("data/conference/conference_talks.txt", "w", encoding="utf-8") as file:
    for talk in talk_values:
        # Remove the unwanted characters and write the result to the file
        file.write(str(talk).translate(trans_table) + "\n")

print("Text file with talk values has been created.")
import csv
import os

# Open the CSV file
with open('./data/recipies/recipes_data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    # Open the output text file
    with open('./data/recipies/recipes.txt', 'w') as txt_file:
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the title, ingredients, and directions from the row
            title = row[0]
            ingredients = row[1]
            directions = row[2]
            
            # Write the title, ingredients, and directions to the text file
            txt_file.write(f"{title}\n{ingredients}\n{directions}\n\n")

            # Check the size of the output file
            txt_file.flush()  # Ensure all data is written to disk
            if os.path.getsize('./data/recipies/recipes.txt') > 100 * 1024 * 1024:  # 200MB
                break  # Stop writing if the file size limit is reached

print("Text file with recipes has been created.")
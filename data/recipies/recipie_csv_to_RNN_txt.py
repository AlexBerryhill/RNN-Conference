import csv
import os

def read_first_100mb(file_path):
    with open(file_path, 'rb') as file:
        return file.read(100 * 1024 * 1024)  # Read the first 200MB

# Use the function
data = read_first_100mb('./data/recipies/recipes.txt')

def write_data_to_file(data, file_path):
    with open(file_path, 'wb') as file:
        file.write(data)

# Use the function
write_data_to_file(data, './data/recipies/recipes_200mb.txt')
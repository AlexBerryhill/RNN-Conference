import os

# Directory path
directory = './data/rally/speeches'

# Output file path
output_file = './data/rally/rally_speeches.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # Open each file in read mode
            with open(os.path.join(directory, filename), 'r') as infile:
                # Read the contents of the file
                contents = infile.read()
                # Write the contents to the output file
                outfile.write(contents)
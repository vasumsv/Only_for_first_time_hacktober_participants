# Define the patterns for each letter in "2023 HACK"
patterns = {
    '0': ['****', '*  *', '*  *', '*  *', '****'],
    '2': ['****', '   *', '****', '*   ', '****'],
    '3': '****', '   *', '****', '   *', '****'],
    ' ': [' ', ' ', ' ', ' ', ' '],  # Space
    'H': ['*  *', '*  *', '****', '*  *', '*  *'],
    'A': [' ** ', '*  *', '****', '*  *', '*  *'],
    'C': ['****', '*   ', '*   ', '*   ', '****'],
    'K': ['* * ', '* * ', '**  ', '* * ', '* * ']
}

# The text to display
text = "2023 HACK"

# Function to print the text using patterns
def print_text(text):
    for row in range(5):
        for char in text:
            pattern = patterns.get(char, [''])
            print(pattern[row], end='  ')
        print()

print_text(text)


#This code defines patterns for each letter in "2023 HACK" and then prints each row of the text using the corresponding patterns. The output will look like the text "2023 HACK" displayed in an asterisk pattern.






# Section 1: File Input
# Read the paragraph from a .txt file and 
# save it into a string variable.

file = open("paragraph.txt", "r")
paragraph = file.read()
print(paragraph)

count = 0

for i in range(paragraph):
    count = count + 1

print(count)





# Section 2: Basic Data Metrics
# Calculate and return the total number of characters 
# in the paragraph, including spaces, symbols, and numbers.

Total_Characters = 


# Count and return the number of lowercase letters (a-z) in the paragraph.
# Extract all uppercase letters from the paragraph and merge them into a single string (e.g., "thIs Sentence OF a feW wordS" → "ISOFWS").
# Add up all individual digits found in the text, treating each digit separately (e.g., "1 then 23" → 1 + 2 + 3 = 6).
# Section 3: Data Metrics with Parameters
# Find and return the character that is the n'th letter in the m'th chunk* of text in the paragraph if the chunk of text is a valid word, with n and m provided as parameters.
# Display only the words in the paragraph that are of length n or greater.
# Count the number of letters in the paragraph, excluding the specific letters provided.
# Find all occurrences of a specific substring in the paragraph and replace them with another substring.
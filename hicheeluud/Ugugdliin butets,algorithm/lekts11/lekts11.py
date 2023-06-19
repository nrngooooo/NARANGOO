import re
file = open('example.txt', 'r',encoding='utf-8')

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

delimiters=r'[!?.:;," ]'
words = re.split(delimiters,contents)

too_dict={}

for word in words:
    if word not in too_dict.keys():
        too_dict[word]  = 1
    else:
        too_dict[word] = too_dict[word]+1
# # Print the list of words
print(too_dict)
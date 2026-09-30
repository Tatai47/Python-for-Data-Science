def countWordFrequency(filePath):
    CharacterCount = 0 # this variable will use to count the total characters
    CountNumbers = 0
    WordCount = 0 # this variable will use to count the total word
    CountSpace = 0
    with open(filePath,'r') as file:
        content = file.read() #it will read the text file
        print(content) 
        for i in content:
            if(i!=" "):
                if i.isdigit():
                    CountNumbers += 1
                else:
                    CharacterCount+=1
            else:
                CountSpace+=1
        WordCount = len(content.split())
    return [f"Character count {CharacterCount}",f"Word count {WordCount}",f"Number count {CountNumbers}",f"Spaces count {CountSpace}"]


filePath = "E:\\Programming Codes\\MBA_-_BADS\\Chittajit\\Practice\\Python\\Udemy\\My Own\\Class Work\\noob.txt"
# print(countWordFrequency(filePath))
x = 1
for i in countWordFrequency(filePath):
    print(f"{x}. {i}")
    x+=1


"""
'r'ReadOpens a file for reading (Default). Throws an error if the file doesn't exist.
'w'WriteOpens a file for writing. Overwrites existing content or creates a new file.
'a'AppendOpens a file to add data to the end. Creates a new file if it doesn't exist.
'x'CreateCreates a specific file. Throws an error if the file already exists.
'b'BinaryOpens the file in binary mode (used for images, videos, etc.).
"""
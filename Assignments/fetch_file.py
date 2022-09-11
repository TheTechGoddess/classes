files = open('fetch_file.txt', 'r')

dictionary = {}

#print(files.read())

for file in files:
    key =  file.split(":")
    if len(key) < 2:
        continue
    dictionary[key[0]] = key[1].strip()

    
print(dictionary)
files.close()


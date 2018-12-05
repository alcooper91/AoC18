file_object = open("Input.txt", "r")

doubles = 0
triples = 0

for line in file_object:
    singleChars = []
    doubleChars = []
    tripleChars = []
    overChars = []

    for char in (line.strip()):
        if char in overChars:
            continue
        elif char in tripleChars:
            tripleChars.remove(char)
            overChars.append(char)
        elif char in doubleChars:
            doubleChars.remove(char)
            tripleChars.append(char)
        elif char in singleChars:
            singleChars.remove(char)
            doubleChars.append(char)
        else:
            singleChars.append(char)

    if len(doubleChars) != 0:
        doubles += 1

    if len(tripleChars) != 0:
        triples += 1

print("doubles: %d" % doubles)
print("triples: %d" % triples)
print("Checksum: %d" % (doubles * triples))

file_object.close()
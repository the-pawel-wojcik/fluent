import random
END_OF_FILE = object()

options = [END_OF_FILE] + [object() for _ in range(5)]
while True:
    node = random.choice(options)

    if node is END_OF_FILE:
        print("End of file")
        break
    print("Not end of file, keep going")

import collections

sentence = "Hello world! It's time to count."
counter = collections.Counter(sentence)


print("Here is the popularity contest in the sentece:")
print(sentence)
print("")
for pair in counter.most_common():
    print(pair)

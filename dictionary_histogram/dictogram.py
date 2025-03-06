import matplotlib.pyplot as plt

# Path to the file
file_path = "/var/lib/words/dict"
file_path = "./README.md"

# Initialize counter
letters_counts = {}

lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

for letter in lowercase_letters:
     letters_counts[letter] = 0

with open(file_path, "r") as file:
        for line in file:
            letters = [char.lower() for char in line if char.isalpha()]
            for letter in letters:
                  letters_counts[letter] += 1

plt.bar(letters_counts.keys(), letters_counts.values())
plt.xlabel("Letter")
plt.ylabel("Occurances")
plt.title(file_path + " Histogram")
plt.savefig('histogram.png')
#plt.show()

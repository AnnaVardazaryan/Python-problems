f = open("text.txt", "r")
f1 = open("analyze_of_text", "w")
num_of_words = {}
num_of_letters = {}

for lines in f:
    words = lines.strip().split(" ")
    for word in words:
        if word in num_of_words:
            num_of_words[word] += 1
        else:
            num_of_words[word] = 1
        for let in word:
            if let in num_of_letters:
                num_of_letters[let] += 1
            else:
                num_of_letters[let] = 1

number_of_words = len(num_of_words)
number_of_letters = len(num_of_letters)

if num_of_words[max(num_of_words, key=num_of_words.get)] == 1:
    most_used_word = 0
else:
    most_used_word = max(num_of_words, key=num_of_words.get)

if num_of_letters[max(num_of_letters, key=num_of_letters.get)] == 1:
    most_used_letter = 0
else:
    most_used_letter = max(num_of_letters, key=num_of_letters.get)

f.seek(0)
count_of_sent = 0
for lines in f:
    sentences = lines.strip().split(".")
    for sentence in sentences:
        if sentence and sentence[0].isupper():
            count_of_sent += 1

f1 = f1.write(f"The number of words:{number_of_words} \nThe number of letters: {number_of_letters}\n"
              f"The number of sentences: {count_of_sent} \nLetter frequency: {most_used_letter} \nWord frequency: {most_used_word}")

f.close()

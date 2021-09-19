words_dict = {}
text = input(">>> ")
text = text.split(" ")
for word in text:
    word_count = words_dict.get(word, 0)
    words_dict[word] = word_count + 1

words = list(words_dict.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_dict[word]))
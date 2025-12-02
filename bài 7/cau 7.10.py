def longest_words(fname):
    with open(fname, "r", encoding="utf-8") as f:
        words = f.read().split()

    max_len = len(max(words, key=len))
    longest = [word for word in words if len(word) == max_len]
    return longest

# Gọi hàm
print(longest_words("test.txt"))

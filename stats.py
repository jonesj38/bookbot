def get_num_words(book):
    return len(book.split())

def get_char_counts(book):
    char_counts = {}
    for word in book.split():
        for char in word.lower():
            if not(char.isalpha()):
                continue
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    return sorted(char_counts.items(), reverse=True, key=lambda x: x[1])
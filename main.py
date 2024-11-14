def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    return text


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words():
    text = main()
    words = text.split()
    return len(words)

def letter_count():
    text = main()
    count_dict = {}
    for letter in text.lower():
        if letter in count_dict:
            count_dict[letter] = count_dict[letter] + 1
        else:
            count_dict[letter] = 1
    return(count_dict)

def report():
    x = []
    char_counts = letter_count()
    for char in char_counts:
        if char.isalpha():
            x.append({"char": char, "count": char_counts[char]})

    x.sort(key=lambda d: d["count"], reverse=True)

    for item in x:
        char = item["char"]
        count = item["count"]

        print(f"The {char} character was found {count} times!")     


report()
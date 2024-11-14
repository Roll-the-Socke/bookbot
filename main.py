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
    print (count_dict)
    return(count_dict)
        


letter_count()

def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words," words was found on the document")
    chars_dict = get_chars_dict(text)
    display(chars_dict)


def display(chars_dict):
    # charList = list(chars_dict.items())
    charList = []
    for c in chars_dict:
        charList.append({"char": c,"num":chars_dict[c]})
    charList.sort(key = sortFunc,reverse=True)
    for i in charList:
        if(i["char"].isalpha()):
             print("The character ",i["char"]," was found ",i["num"]," times")

def sortFunc(e):
    return e["num"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
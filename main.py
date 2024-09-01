def main():
    bookPath = "books/frankenstein.txt"
    print(
    return item[1]


def read_file(pathStr):
    with open(pathStr) as f:
        return f.read()


def word_count(bookStr):
    return len(bookStr.split())


def count_characters(bookStr):
    char_count_dict = {}
    bookStr = bookStr.lower()

    for char in bookStr:
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1

    return char_count_dict


main()


# Solutions

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     print()

#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"The '{item['char']}' character was found {item['num']} times")

#     print("--- End report ---")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def sort_on(d):
#     return d["num"]


# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()

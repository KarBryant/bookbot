import sys
from stats import get_word_count,get_char_count,char_sort


def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
    return file_content


def main():
    book_text = get_book_text(sys.argv[1])
    chars = get_word_count(book_text)
    count = get_char_count(book_text)
    sorted_letters = char_sort(count)


    print("============ BOOKBOT ============")
    print(f"analyzing book found at books/frankenstein.txt. . .")
    print("----------- Word Count ----------")
    print(chars)
    print("--------- Character Count -------")

    for item in range(len(sorted_letters)):
        print(f"{sorted_letters[item]["char"]}: {sorted_letters[item]["num"]}")

    print("============= END ===============")


try:
    main()


except Exception as e:
    if len(sys.argv) < 2:
        e = "Usage: python3 main.py <path_to_book>"
        print(e)
        sys.exit(1)
    else:
        print(e)

import string

def get_word_count(book_text):
    word_count = len(book_text.split())
    response = f"Found {word_count} total words"
    return response

def get_char_count(boot_text):
    counted_letters = {
        letter: 0 for letter in string.ascii_lowercase
    }

    for letter in boot_text.lower():
        if letter in counted_letters.keys():
            counted_letters[letter] += 1

    return counted_letters

def sort_on(dict):
    return dict["num"]
    
def char_sort(chars):

    new_list = []
    for item in chars.items():
        new_dict = {
            "char": item[0],
            "num": item[1]
        }
        new_list.append(new_dict)
    

    new_list.sort(reverse=True, key=sort_on)
    
   

    return new_list
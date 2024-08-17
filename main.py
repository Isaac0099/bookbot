def main():
    book_path = "books/frankenstein.txt"
    book_contents = read_file(book_path)
    num_words = word_count(book_contents)
    character_counts = char_count(book_contents)
    sorted_char_dict_list = chars_dict_to_sorted_list(character_counts)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for item in sorted_char_dict_list:
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")    


def word_count(text):
    words = text.split()
    return len(words)


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]
   

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def char_count(text):
    low_text = text.lower()
    char_dict = {}
    for letter in low_text:
        if letter in char_dict:
            char_dict[letter] = char_dict[letter] + 1
        else:
            char_dict[letter] = 1
    return char_dict


def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()
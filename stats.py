def get_book_text(file_path):

    with open(file_path) as f:
        text_content = f.read()
        return text_content

def count_words(file_path):
    text_content = get_book_text(file_path)
    word_list = text_content.split()
    return len(word_list)

def count_char(file_path):
    text_content = get_book_text(file_path)

    char_dict = {}

    for char in text_content:
        low_char = char.lower()
        if low_char in char_dict:
            char_dict[low_char] += 1
        else:
            char_dict[low_char] = 1
        
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    char_list = []
    
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def pretty_print(word_count, char_dict):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")
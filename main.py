from stats import count_words, count_char, sort_dict, pretty_print
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = count_words(sys.argv[1])
    # print(f"{num_words} words found in the document")
    # print(count_char("books/frankenstein.txt"))

    char_dict = count_char(sys.argv[1])
    sorted_dict = sort_dict(char_dict)
    #print(sort_dict(char_dict))
    pretty_print(num_words, sorted_dict)

main()

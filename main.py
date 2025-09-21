import sys

from stats import get_num_words
from stats import get_char_and_nums
from stats import sort_dict_by_value

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():

    file_path = sys.argv

    if len(file_path) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        

    # get the book's information
    book_text = get_book_text(file_path)

    # count up all the "words"
    num_words = get_num_words(book_text)
    

    # make dictionary of all characters and their numbers
    char_dict = get_char_and_nums(book_text)
    
    # make the sorted list
    new_dict = sort_dict_by_value(char_dict)
    
    # print title of program
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k in new_dict:
        print(f"{k}: {new_dict[k]}")
    print("============= END ===============")
    
    


main()
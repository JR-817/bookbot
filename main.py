#frnknstn = "books/frankenstein.txt"

import sys
from stats import count_words, count_characters, sorted_dictionary

def get_book_text(filepath) :
    with open(filepath) as f :
        book = f.read()
        return book

def main() :
    #print(sys.argv)                            #for testing
  #  print(len(sys.argv))                       #for testing
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1] 
    #print(path_to_book)                        #for testing
    book = get_book_text(path_to_book)    
    #print(count_words(book))                   #earlier lesson
    #print(count_characters(book))              #earlier lesson
    print(sorted_dictionary(path_to_book, book))

main()
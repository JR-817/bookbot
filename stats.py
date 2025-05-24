def count_words(book) :
    num_words = len(book.split())
    #return (f"{num_words} words found in the document")        #first lesson
    return f"Found {num_words} total words"
def count_characters(book) : 
    num_chars = {}
    words = book.lower()
    for word in words :
        if word not in num_chars:
            num_chars[word] = 1
        else:
            num_chars[word] += 1
    return num_chars
def sorted_dictionary(file_path, book) :
    characters_dictionary = count_characters(book)          #get unordered dictionary
    sorted_dicts = []                        
    for is_letter in characters_dictionary :
        count = characters_dictionary[is_letter]   
        if is_letter.isalpha() == True :
            new_dict = {"letter is " : is_letter , "count is" : count}
            sorted_dicts.append(new_dict)
    def sort_on(dict):                                        #helper function
        return dict["count is"]                               #for sorting dict
    
    sorted_dicts.sort(reverse=True,key=sort_on)

    def list_each_dict(sorted_dicts) :
        master_list = ""
        for each_dict in sorted_dicts :
            master_list+=f"\n{each_dict["letter is "]}: {each_dict["count is"]}"
        return master_list
        
#formated report of ordered dictionary
    header = "============ BOOKBOT ============\n"
    book_path = f"Analyzing book found at {file_path} ...\n"
    wc = f"----------- Word Count ----------\n{count_words(book)}\n"
    char_cnt = f"--------- Character Count -------{list_each_dict(sorted_dicts)}\n"
    end = "============= END ==============="

    return header+book_path+wc+char_cnt+end
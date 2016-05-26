# practice writing code by recreating the replace method

def myreplace(search_string, target_string,new_string):
    # finds all instances of target_string in search_string and then replaces
    # them with new_string
    start_position = 0
    i=0
    length_old = len(target_string)
    length_new = len(new_string)
    while True:
        start_position = search_string.find(target_string,i)
        if start_position == -1:
            break
        end_position = start_position + length_old
        search_string = search_string[:start_position] + new_string + search_string[end_position:]
        i = start_position + length_new #add length_new to avoid error if search_string
                                        # is a substring of new_string the replacement
    return search_string


text = "hello this is a test string it is a place to find the word is "
print myreplace(text, 'hiddy ho','this')

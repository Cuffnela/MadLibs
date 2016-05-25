# practice writing code by recreating the replace method

def myreplace(search_string, target_string):
    # finds all instances of target_string in search_string and then replaces
    # them with new_string
    position = 0
    i=0
    while position != -1:
        position = search_string.find(target_string,i)
        i = position + 1


text = "hello this is a test string it is a place to find the word is "
myreplace(text, 'is')

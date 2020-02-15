import difflib
import json

def translate(word):
    dic = json.loads(data.json)
    if (meaning:=dic.get(word)) is not None:
        return meaning
    elif meaning.lower is not None:
        return meaning
    return None

def ask(word):
    while True:
        ask = input("did you mean this word [y,n]>>>")
        ask_l_yes = ["y","yes",""]
        ask_l_no = ["n","no"]
        if ask.lower in ask_l_yes:
            return True
        elif ask.lower in ask_l_no:
            return False
            


def gussed(gussed_word_func):
    gusseed_word = difflib.get_close_matches(gussed_word_func,n=1,cutoff=.5)
    if gusseed_word is not None :
        return gusseed_word
    return None
    
    

def main(word):
    while True:
        word = input("enter a word >>>")
        translate_word = translate(word)
        if translate_word not None:
            print(translate_word)
            continue
        elif translate_word None:
           ask_word = ask(word)
            if ask_word:
                continue
            else:
                gussed_word = gussed(word)
                print(gussed_word)
                ask()
                

    
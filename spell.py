from translate import image_to_gif

def spell(english):
    english = english.lower()
    english = english.split()
    english = english[1:]
    
    sign = ""
    index = "_001"
    
    for word in english:
        word = list(word)
        word = [i + index + " " + i + index for i in word]
        word = " ".join(word)
        sign = sign + " " + word
        print(word)
            
    sign = sign.strip()
    return sign

# could optimize the string operations
    
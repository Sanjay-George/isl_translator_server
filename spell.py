from translate import image_to_gif

def spell(english):
#    english = "spell Sanjay Varkey georGE"
    name = english.replace(" ", "_")  # name for the gif
     
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
    
    try :
        gif_path = image_to_gif(sign, name) # FINAL RETURN 
    except :
        print("Error occured. File doesn't exist")
        return str(0)

    return gif_path
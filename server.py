from flask import Flask
from translate import preprocess, fetch_sign, image_to_gif
from spell import spell

app = Flask(__name__)


# root
@app.route("/")
def index():
    return "This is root!!!!"


@app.route('/spell/<english>')
def spell_words(english):
    name = english.replace(" ", "_")  # name for the gif
#    SPELL THE INPUT
    sign = spell(english)
    try :
        gif_path = image_to_gif(sign, name) # FINAL RETURN 
    except :
        print("Error occured. File doesn't exist")
        return str(0)    
    return gif_path


@app.route('/engtoisl/<english>')
def translate_text(english):
    english = preprocess(english)
    name = english.replace(" ", "_")  # name for the gif
#    try:
    sign = fetch_sign(english)
#    except : 
#        print("error occured. No proper translation")
#        return str(0) 
    
#    try :
    gif_path = image_to_gif(sign, name) # FINAL RETURN 
#    except :
#        print("Error occured. File doesn't exist")
#        return str(0)
    return gif_path


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
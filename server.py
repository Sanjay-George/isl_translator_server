from flask import Flask
from translate import preprocess, fetch_sign, image_to_gif
from spell import spell

app = Flask(__name__)


# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"

#GET
@app.route('/users/<user>')
def hello_user(user):
	return "Hello %s!" % user


@app.route('/spell/<english>')
def spell_words(english):
    gif_path = spell(english)
    return gif_path


@app.route('/engtoisl/<english>')
def translate_text(english):
    english = preprocess(english)
    name = english.replace(" ", "_")  # name for the gif
    try:
        sign = fetch_sign(english)
    except : 
        print("error occured. No proper translation")
        return str(0)
    # -------------------------------------------------
    # TODO : uncomment the try except before final run  
    try :
        gif_path = image_to_gif(sign, name) # FINAL RETURN 
    except :
        print("Error occured. File doesn't exist")
        return str(0)
    #--------------------------------------------------
    return gif_path


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
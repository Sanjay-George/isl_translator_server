from flask import Flask
from translate import preprocess, fetch_sign, image_to_gif


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

@app.route('/translate/<english>')
def translate_text(english):
    english = preprocess(english)
    name = english.replace(" ", "_")  # name for the gif
    sign = fetch_sign(english)
    gif_path = image_to_gif(sign, name) # FINAL RETURN 
#    return json.dumps({'gif_path' : gif_path} )
    return gif_path


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
import re
import imageio
from inference import inference
from mapping import mapping
from rules import check_rules

from nltk.stem.porter import PorterStemmer
import socket



# UPDATE STOPWORDS 
stopwords = ['an', 'to', 'shall', 'are', 'were', 'is', 'was', 'am', 'the', 'do', 'in', 'there', 'that', 'had', 'of', 'too', 'used', 'really', 'very', 'so', 'will']
# host address : localhost 
host = socket.gethostbyname(socket.gethostname())

#function to preprocess the input text - must match with preprocessing.py
def preprocess(english):
    english = re.sub('[^a-zA-Z0-9]', ' ', english)
    english = english.lower()
    english = english.split()
    ps = PorterStemmer()
    english = [ps.stem(word) for word in english if not word in set(stopwords)]
#    english = [word for word in english if not word in set(stopwords)]
    english = " ".join(english)
#    name = english
    return english
    

#function to fetch the signs
def fetch_sign(english):
    temp = inference(english)
    index = temp['best_index']
    sentence = temp['answers'][index]
    print("english = " + english)
    print("sentence = " + sentence)
    sentence = check_rules(english, sentence)
    print("sentence(rules check) : " + sentence)
    sign = mapping(sentence)
    print("sign = " + sign)
    return sign

# UPDATE THE FOLLOWING PATHS ACCORDING TO THE SERVER
path = "./resources/images/"
output = "./resources/output/"
localhost = "http://{}/translator/MODEL7/nmt-chatbot/resources/output/".format(host)  

#function to convert images to gif
def image_to_gif(sign, name):
    filenames = []
    images = []
#    convert signs to jpg filenames
    sign = sign.split()
    for word in sign:
        word = path + word + ".jpg"
        filenames.append(word)
#    filenames = ["{}you_001.jpg".format(path), "{}you_001.jpg".format(path), "{}know_001.jpg".format(path), "{}know_002.jpg".format(path), "{}know_003.jpg".format(path),  "{}book_001.jpg".format(path), "{}book_002.jpg".format(path), "{}book_003.jpg".format(path), "{}book_004.jpg".format(path), "{}book_005.jpg".format(path), "{}book_006.jpg".format(path)]   
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('{}{}.gif'.format(output, name) , images, duration=0.3)
    return '{}{}.gif'.format(localhost, name)   #PATH TO GIF : FINAL RETURN 












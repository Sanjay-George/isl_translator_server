Server side code for isl translator. Flask server with NMT

This repo uses the tensorflow NMT architecture Reference : 
@article{luong17,
  author  = {Minh{-}Thang Luong and Eugene Brevdo and Rui Zhao},
  title   = {Neural Machine Translation (seq2seq) Tutorial},
  journal = {https://github.com/tensorflow/nmt},
  year    = {2017},
}

This repo uses the utils built by Daniel Kukiela on top of NMT 
Link : https://github.com/daniel-kukiela/nmt-chatbot
Modifications have been made to the above utils inorder to translate efficiently for small dataset (size = 1000 approx.)

Server: Flask server, Localhost
Frontend : Android app (Java) https://github.com/Sanjay-George/isl_translator


STEPS FOR RUNNING:
1. Create a folder in htdocs
2. Clone this repo into that folder
3. Open translate.py and change the value of localhost variable to the correct file path
4. Open model/checkpoint and change the model_checkpoint_path to the correct file path 
5. Open model/hparams and change the property "best_bleu_dir" to the correct file path
6. Run server.py. It will be run on port 5000. 
7. Run apache server on localhost.

NOTE : Send GET request to the flash server at the route /translate/<english_text>



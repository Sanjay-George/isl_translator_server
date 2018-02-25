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

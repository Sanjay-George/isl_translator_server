# SERVER SIDE PROGRAM TO CONVERT IMAGES INTO GIF 
import imageio
path = "./resources/images/"
output = "./resources/output/"
#filenames = ["{}you_001.jpg".format(path), "{}you_001.jpg".format(path), "{}know_001.jpg".format(path), "{}know_002.jpg".format(path), "{}know_003.jpg".format(path),  "{}book_001.jpg".format(path), "{}book_002.jpg".format(path), "{}book_003.jpg".format(path), "{}book_004.jpg".format(path), "{}book_005.jpg".format(path), "{}book_006.jpg".format(path)]
images = []

filenames = ['./resources/images/born_001.jpg',
 './resources/images/born_002.jpg',
 './resources/images/place_001.jpg',
 './resources/images/place_002.jpg',
 './resources/images/where_001.jpg',
 './resources/images/where_002.jpg',
 './resources/images/where_003.jpg',
 './resources/images/where_004.jpg',
 './resources/images/where_005.jpg',
 './resources/images/where_006.jpg',
 './resources/images/f_001.jpg',
 './resources/images/f_001.jpg',
 './resources/images/r_001.jpg',
 './resources/images/r_001.jpg',
 './resources/images/a_001.jpg',
 './resources/images/a_001.jpg',
 './resources/images/n_001.jpg',
 './resources/images/n_001.jpg',
 './resources/images/k_001.jpg',
 './resources/images/k_001.jpg',
 './resources/images/f_001.jpg',
 './resources/images/f_001.jpg',
 './resources/images/u_001.jpg',
 './resources/images/u_001.jpg',
 './resources/images/r_001.jpg',
 './resources/images/r_001.jpg',
 './resources/images/t_001.jpg',
 './resources/images/t_001.jpg']

for filename in filenames:
    images.append(imageio.imread(filename))
    
imageio.mimsave('{}movie.gif'.format(output), images, duration=0.3)
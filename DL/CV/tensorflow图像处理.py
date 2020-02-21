import tensorflow as tf
import matplotlib.pyplot as plt

raw_data= tf.gfile.FastGFile('1.jpg','rb').read()

with tf.Session() as sess:
    img_data = tf.image.decode_jpeg(raw_data)
    print(img_data.eval())
    
    plt.imshow(img_data.eval())
    plt.show()  
    
    encoded_image = tf.image.encode_jpeg(img_data)
        
    with tf.gfile.GFile('2.jpg','wb') as f:
        f.write(encoded_image.eval())

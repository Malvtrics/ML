import tensorflow as tf 
import numpy as np

train_files = tf.train.match_filenames_once('path/to/train_file-*')
test_files = tf.train.match_filenames_once('path/to/test_file-*')

def parser(record):
    features = tf.parse_single_sequence_example(
            record,
            features = {
                    'image':tf.FixedLenFeature([],tf.string),
                    'label':tf.FixedLenFeature([],tf.int64),
                    'height':tf.FixedLenFeature([],tf.int64),
                    'width':tf.FixedLenFeature([],tf.int64),
                    'channels':tf.FixedLenFeature([],tf.int64)
                    })
    decoded_image = tf.decode_raw(features['image'],tf.uint8)
    decoded_image.set_shape([features['height'],features['width'],features['channels']])
    label = features['label']
    return decoded_image,label

def distort_color(image, color_ordering=0):
    if(color_ordering==0):
        image = tf.image.random_brightness(image,max_delta=32./255.)
        image = tf.image.random_saturation(image,lower=0.5,upper=1.5)
        image = tf.image.random_hue(image,max_delta=0.2)
        image = tf.image.random_contrast(image,lower=0.5,upper=1.5)
    elif(color_ordering==1):
        image = tf.image.random_saturation(image,lower=0.5,upper=1.5)
        image = tf.image.random_brightness(image,max_delta=32./255.)
        image = tf.image.random_contrast(image,lower=0.5,upper=1.5)
        image = tf.image.random_hue(image,max_delta=0.2)
    else:
        pass
    return tf.clip_by_value(image,0.0,1.0)

def preprocess_for_train(image,height,width,bbox):
    if bbox is None:
        bbox = tf.constant([0.0,0.0,1.0,1.0,],dtype=tf.float32,shape=[1,1,4])
    if image.dtype != tf.float32:
        image = tf.image.convert_image_dtype(image,dtype=tf.float32)
    bbox_begin,bbox_size,_ = tf.image.sample_distorted_bounding_box(tf.shape(image),bounding_boxes=bbox)
    distorted_image = tf.slice(image, bbox_begin, bbox_size)
    distorted_image = tf.image.resize_images(distorted_image,[height,width],np.random.randint(4))
    distorted_image = distort_color(distorted_image,np.random.randint(4))
    return distorted_image

image_size = 299
batch_size = 100
shuffle_buffer = 10000

dataset = tf.data.TFRecordDataset(train_files)
dataset = dataset.map(parser)

dataset = dataset.map(lambda image,label:(preprocess_for_train(image,image_size,image_size,None),label))
dataset = dataset.shuffle(shuffle_buffer).batch(batch_size)

NUM_EPOCHS = 10
data = dataset.repeat(NUM_EPOCHS)

iterator = dataset.make_initializable_iterator()
image_batch,label_batch = iterator.get_next()

learning_rate = 0.01
logit = inference(image_batch)
loss = calc_loss(logit,label_batch)
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

test_dataset = tf.data.TFRecordDataset(train_files)
test_dataset = test_dataset.map(lambda image,label:(preprocess_for_train(image,image_size,image_size,None),label))
test_dataset = test_dataset.batch(batch_size)
test_iterator = test_dataset.make_initializable_iterator()
test_image_batch,test_label_batch = test_iterator.get_next()
test_logit = inference(test_image_batch)
predictions = tf.arg_max(test_logit,axis=-1,output_type=tf.int32)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer(),tf.local_variables_initializer)
    sess.run(iterator.initializer)
    while(True):
        try:
            sess.run(train_step)
        except(tf.errors.OutOfRangeError):
            break
    sess.run(test_iterator)
    test_results=[]
    test_labels=[]
    while(True):
        try:
            pred,label = sess.run([predictions,test_label_batch])
            test_results.extend(pred)
            test_labels.extend(label)
        except(tf.errors.OutOfRangeError):
            break
    
    correct = [float(y==y_) for (y,y_) in zip(test_results,test_labels)]
    accuracy = sum(correct)/len(correct)
    print('Test accuracy is : {0}'.format(accuracy))

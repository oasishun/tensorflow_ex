import tensorflow as tf

#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x_data = [1,2,3]
y_data = [1,2,3]

print (x_data)
print (y_data)

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0,1.0))


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)








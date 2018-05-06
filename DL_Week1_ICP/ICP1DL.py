
# Importing the Tensorflow
import tensorflow as tf

# The required formula: (a^2+b)*c 


# The matrices variables:
a = [[2, 4], [6, 7]]
b = [[5, 2], [1, 4]]
c = [[4, 0], [8, 1]]


# The a^2 part
op1 = tf. multiply(a, a)
op1_2 = tf.pow(a, 2)


# The a^2+b part
op2 = tf.add(op1, b)
op2_2 = tf.add(op1_2, b)


# The (a^2+b)*c part
op3 = tf.multiply(op2, c)
op3_2 = tf.multiply(op2_2, c)


# Extracting the equation value
with tf.Session() as sess:
    print(sess.run(op3))
    print(sess.run(op3_2))















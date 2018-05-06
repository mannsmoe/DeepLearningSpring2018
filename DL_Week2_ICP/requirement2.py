
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = 'data/Smoking.xls'
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1
X1 = tf.placeholder(tf.float32, name='Smoking_status')
X2 = tf.placeholder(tf.float32, name='Age_classification')
Y = tf.placeholder(tf.float32, name='Death_status')
X3 = tf.placeholder(tf.float32, name='Number_of_cases')

w1 = tf.Variable(0.0, name='weights')
w2 = tf.Variable(1.0, name='weights')
b = tf.Variable(0.0, name='bias')
Y_predicted = X1* w1 + X2*w2+b
loss = tf.square(Y - Y_predicted, name='loss')
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    for i in range(50):
        total_loss = 0
        for x1,x2, y,x3 in data:
            _, l = sess.run([optimizer, loss], feed_dict={X1: x1, X2:x2,Y: y})
            total_loss += l
    writer.close()
    w1,w2, b = sess.run([w1,w2, b])
X1,X2,Y = data.T[0], data.T[1],data.T[2]
plt.plot(X1,X2, Y, 'bo', label='Real data')
plt.plot(X1,X2 , X1* w1 + X2*w2+b, 'r', label='Predicted data')
plt.legend()
plt.show()
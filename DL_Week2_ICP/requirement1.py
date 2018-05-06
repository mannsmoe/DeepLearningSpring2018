
import numpy as num
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

# Loading the data
DATA_FILE = 'data/USA_Housing.xls'
ExcelFile = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
ExcelSheet = ExcelFile.sheet_by_index(0)
data = num.asarray([ExcelSheet.row_values(i) 
                    for i in range(1, ExcelSheet.nrows)])
data = num.asarray(data[:100,[1,3,5]],dtype = float)

# Initializing and formating the variables
indep1 = tf.placeholder(tf.float32, name = "Avg_Area_House_Age")
indep2 = tf.placeholder(tf.float32, name = "Avg_Area_Number_of_Rooms")
pred1 = tf.placeholder(tf.float32, name = "Price")
Wieght = tf.Variable(0.0, name='weights')
biase = tf.Variable(0.0, name='bias')


# Declearing the linear regression formula
PredY1 = indep1*Wieght + biase
PredY2 = indep2*Wieght + biase
PredY1Loss = tf.square(pred1 - PredY1, name='loss')
PredY2Loss = tf.square(pred1 - PredY2, name='loss')
Y1PredOpt = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(PredY1Loss)
Y2PredOpt = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(PredY2Loss)

# Starting the learning session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    # Saving the needed data for the Tensorboard 
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    for i in range(50):
        total_loss1 = 0
        total_loss2 = 0
        for x2,x3,y in data:
            _, l1 = sess.run([Y1PredOpt, PredY1Loss], feed_dict={indep1:x2,pred1: y})
            total_loss1 += l1
            _, l2 = sess.run([Y2PredOpt, PredY2Loss], feed_dict={indep2:x3,pred1: y})
            total_loss2 += l2
    writer.close()
    Wieght, biase = sess.run([Wieght, biase])

# The graph
indep1,indep2,pred1 = data.T[0], data.T[1], data.T[2]
plt.plot(indep1,indep2, pred1, 'bo', label='Real data')
plt.plot(indep1,indep1*Wieght +biase, 'r', label='Avg_Area_House_Age')
plt.plot(indep2,indep2*Wieght +biase, 'g', label='Avg_Area_Number_of_Rooms')
plt.legend()
plt.show()
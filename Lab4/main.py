# Importing the required modules such as tensorflow
#from __future__ import print_function
import tensorflow as TFlow

# Loading the MNIST dataset from the examples folder of tensorflow module and specify the location to be loaded to (same as the folder of the source code file )
from tensorflow.examples.tutorials.mnist import input_data
print("\n Loading the MNIST dataset ... \n")
MnistDataset = input_data.read_data_sets("./", one_hot=True)

# Setting the Hyperparameters values
Bs = 10 # The Batch SIze
Te = 30 # The Training Epoch
Ds = 1 # The Display Step
Lr = 1  # The Learning Rate

# Parsing the loaded data into float32 placeholders
Dimention1 = TFlow.placeholder(TFlow.float32, [None, 784])
Dimention2 = TFlow.placeholder(TFlow.float32, [None, 10])

# Initialize the graph variables
Var1 = TFlow.Variable(TFlow.zeros([784, 10]))
Var2 = TFlow.Variable(TFlow.zeros([10]))
Var3 = TFlow.nn.softmax(TFlow.matmul(Dimention1, Var1) + Var2)
# Calculating the mean
MeanValue = TFlow.reduce_mean(-TFlow.reduce_sum(Dimention2*TFlow.log(Var3), reduction_indices=1))
DescOpt = TFlow.train.GradientDescentOptimizer(Lr).minimize(MeanValue)
Var4 = TFlow.global_variables_initializer()

# Running the training session:
with TFlow.Session() as TrainSession:
    TrainSession.run(Var4)
    EventsLogger = TFlow.summary.FileWriter('./', TrainSession.graph)
    print("\n Starting the training and optimization session ...")
    for epoch in range(Te):
        middle = 0.
        AccumilativeBatch = int(MnistDataset.train.num_examples/Bs)
        for i in range(AccumilativeBatch):
            HorizantalBatch, VerticalBatch = MnistDataset.train.next_batch(Bs)
            _, TrainOut = TrainSession.run([DescOpt, MeanValue], feed_dict={Dimention1: HorizantalBatch, Dimention2: VerticalBatch})
            middle += TrainOut / AccumilativeBatch
    
    ModelTesting = TFlow.equal(TFlow.argmax(Var3, 1), TFlow.argmax(Dimention2, 1))
    
    # Model accuracy calculation and printing
    ModelAccuracy = TFlow.reduce_mean(TFlow.cast(ModelTesting, TFlow.float32))
    Acc = ModelAccuracy.eval({Dimention1: MnistDataset.test.images, Dimention2: MnistDataset.test.labels})
    print("\n The final model accuracy is : ", Acc)
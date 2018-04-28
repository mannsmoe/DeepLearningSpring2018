
import tensorflow as TensFl
import numpy as NmP
import os
import time
import datetime
import loader
from parsing import Parsee
from tensorflow.contrib import learn

TensFl.flags.DEFINE_float("splitting", .25, "Percentage of the training data")
TensFl.flags.DEFINE_string("ones_data_file", "./data/ones.one", "Data source for 1 star.")
TensFl.flags.DEFINE_string("twos_data_file", "./data/twos.two", "Data source for 2 stars.")
TensFl.flags.DEFINE_string("threes_data_file", "./data/threes.thr", "Data source for 3 stars")
TensFl.flags.DEFINE_string("fours_data_file", "./data/fours.fou", "Data source for 4 stars")
TensFl.flags.DEFINE_string("fives_data_file", "./data/fives.fiv", "Data source for 5 stars")

TensFl.flags.DEFINE_integer("BatchSize", 64, "")
TensFl.flags.DEFINE_integer("Epochs", 200, "")
TensFl.flags.DEFINE_integer("PeriodOfCompare", 100, "")
TensFl.flags.DEFINE_integer("CHeck", 100, "")
TensFl.flags.DEFINE_integer("ChTimes", 5, "")
TensFl.flags.DEFINE_boolean("allow_soft_placement", True, "")
TensFl.flags.DEFINE_boolean("log_device_placement", False, "")


TensFl.flags.DEFINE_integer("EmDim", 128, "")
TensFl.flags.DEFINE_string("ModFiltSize", "3,4,5", "")
TensFl.flags.DEFINE_integer("UsedFilters", 128, "")
TensFl.flags.DEFINE_float("DKP", 0.5, "")
TensFl.flags.DEFINE_float("Lam", 0.0, "")

FLAGS = TensFl.flags.FLAGS

print(" Importing and raeding data...")
Var, Outt = loader.load_data_and_labels(FLAGS.ones_data_file, FLAGS.twos_data_file)
DocLeng = max([len(Var2.split(" ")) for Var2 in Var])
WordsPool = learn.preprocessing.VocabularyProcessor(DocLeng)
Var2 = NmP.array(list(WordsPool.fit_transform(Var)))
NmP.random.seed(10)
Var3 = NmP.random.permutation(NmP.arange(len(Outt)))
ind1 = Var2[Var3]
dep1 = Outt[Var3]


Var5 = -1 * int(FLAGS.splitting * float(len(Outt)))
x_train, x_dev = ind1[:Var5], ind1[Var5:]
y_train, y_dev = dep1[:Var5], dep1[Var5:]

del Var2, Outt, ind1, dep1

print("Vocabulary Size: {:d}".format(len(WordsPool.vocabulary_)))
print("Train/Dev split: {:d}/{:d}".format(len(y_train), len(y_dev)))

with TensFl.Graph().as_default():
    session_conf = TensFl.ConfigProto(
      allow_soft_placement=FLAGS.allow_soft_placement,
      log_device_placement=FLAGS.log_device_placement)
    sessionn = TensFl.Session(config=session_conf)
    with sessionn.as_default():
        cnn = Parsee(
            sequence_length=x_train.shape[1],
            num_classes=y_train.shape[1],
            vocab_size=len(WordsPool.vocabulary_),
            embedding_size=FLAGS.EmDim,
            ModFiltSize=list(map(int, FLAGS.ModFiltSize.split(","))),
            UsedFilters=FLAGS.UsedFilters,
            Lam=FLAGS.Lam)
			
        Iterationn = TensFl.Variable(0, name="Iterationn", trainable=False)
        optimizer = TensFl.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, Iterationn=Iterationn)


import sys
import pickle
import numpy as np
import argparse
from pitf import PITF

def read_data(filepath):
    return np.genfromtxt(filepath, delimiter=' ', dtype=int)


p = argparse.ArgumentParser()
'''
p.add_argument("-i", "--infile", help="input tensor file", type=argparse.FileType('r'), required=True)
p.add_argument("-o", "--outfile", help="output model file", type=argparse.FileType('w'), required=True)
p.add_argument("-a", "--alpha", help="alpha (default=0.05)", type=float, nargs='?', default=0.05)
p.add_argument("-l", "--lamb", help="lambda (default=0.00005)", type=float, nargs='?', default=0.00005)
p.add_argument("-k", help="k (default=10)", type=int, nargs='?', default=10)
p.add_argument("-m", "--max_iter", help="max_iter (default=100)", type=int, nargs='?', default=100)
p.add_argument("-v", "--verbose", help="verbosity", action='store_true')
'''
args = p.parse_args()

fileName = "base1000_step1000_n1"
args.infile = "..//data//" + fileName + ".train"
args.outfile = open("..//data//" + fileName + ".model", "w")
args.alpha = 0.01
args.lamb = 0.005
args.k = 10
args.max_iter = 100
args.verbose = True

data = read_data(args.infile)
data_shape = data[0]
data = data[1:]

print "begin PITF"
model = PITF(args.alpha, args.lamb, args.k, args.max_iter, data_shape, args.verbose)

model.fit(data, data)
pickle.dump(model, args.outfile)

args.outfile.close()

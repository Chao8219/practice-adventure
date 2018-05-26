import pickle
import string
import os

path='userinfo'
outputFile=path+'/test.data'
inputFile=path+'/test.data'

if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(outputFile):
    with open(outputFile, 'w+'): pass

dataset = ['hello','world']
fw = open(outputFile, 'wb')
pickle.dump(dataset, fw)
fw.close()


fd = open(inputFile, 'rb')
dataset2 = pickle.load(fd)
print(dataset2[1])


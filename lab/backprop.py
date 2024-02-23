from math import exp
from random import seed , random

def init_net(inp,hid,op):
    net = [
        [{'weights':[random() for _ in range(inp+1)]} for _ in range(hid)],
        [{'weights':[random() for _ in range(hid+1)]} for _ in range(op)]
        
    ]
    '''
        bias                                                                bias
        [1]\                                                                [1]\
             \w0                                                                 \w0
t e     x1     \    h1         range(inp+1)                 _               a1     \    o1        range(hid+1)                  _
r x     []-w1------ {'weights':[w1,w2,w0],output=a1,delta}   |              []-w1------ {'weights':[w1,w2,w0],output,delta}      |
a a           /                                              |                     /                                             |
i m     x2  / w2    h2                                       |range(hid)    a2   / w2   o2                                       |range(op)
n p     []/         {'weights':[w1,w2,w0],output=a2,delta}} _|              [] /        {'weights':[w1,w2,w0],output,delta}}    _|
i l
n e                                                                                                                                                        label y
g s
        input       hidden                                                              output
    '''
    return net

def activate(w:list,inp:list)->float:
    '''
    #w is list of weights of neuron units in a layer
    #inp is a single training example (x(a list), t)
    #ignore w0 and t 
    '''
    activation = w[-1]          #add bias unit 1*w0
    for i in range(len(w)-1):
        activation += w[i]*inp[i]
    return activation

def forward(net, row):
    #row is a single training example (x:list, t)
    inp = row
    for layer in net:
        layer_out = []
        for neuron in layer:
            z = activate(neuron['weights'], inp)
            act = 1.0/(1.0+exp(-z))
            neuron['output'] = act      #add the output to each neuron
            layer_out.append(act)
        inp = layer_out
    return inp

def derivative(err,output):
    return err*output*(1-output)

def back_prop(net, expected):
    for i in range(len(net)-1,-1,-1):# from n-1th layer till layer 0
        layer = net[i]
        if i==len(net)-1:
            for neuron, expectation in zip(layer, expected):
                error = expectation-neuron['output']
                neuron['delta'] = derivative(error,neuron['output'])
        else:
            for j in range(len(layer)):
                error = 0.0
                for neurons in net[i+1]:
                    error += neurons['weights'][j]*neurons['delta']
                layer[j]['delta'] = derivative(error,layer[j]['output'])

def update(net, te, lr):
    for i in range(len(net)):
        inputs = te[:-1]
        if i!= 0:
            inputs = [neuron['output'] for neuron in net[i-1]]
        for neuron in net[i]:
            for j in range(len(inputs)):
                neuron['weights'][j]+=lr*neuron['delta']*inputs[j]
            # neuron['weights'][-1] += lr*neuron['delta']     #??update bias!!!????

def train(net, train, lr, epoch, n_out):
    '''
    train: dataset
    lr: learning rate
    epoch: number of epochs. 1 (forward,back_prop,update) = 1 epoch
    n_out: number of classes(labels)
    '''
    for _ in range(epoch):
        sum_error = 0       #cost
        for te in train:
            out = forward(net, te)
            #multi class classifier output vector
            expected = [0]*n_out
            expected[te[-1]]= 1     #mark label class
            sum_error += sum((x-y)**2 for x,y in zip(out,expected))       #accumulate errors on each training example
            back_prop(net, expected)
            update(net,te,lr)

        print(f'>epoch={_}, lrate = {lr}, error = {sum_error}')
            
seed(1) #use 1 as seed for random number generation, not current system time or os random
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
#exclude label y
n_inputs = len(dataset[0]) - 1
#get number of distinct classes from labels
n_outputs = len(set([row[-1] for row in dataset]))
network = init_net(n_inputs, 2, n_outputs)
train(network, dataset, 5, 50, n_outputs)
for layer in network:
    print(layer)
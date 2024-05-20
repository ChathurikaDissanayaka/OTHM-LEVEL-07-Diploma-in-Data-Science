# multinomial logistic regression
import numpy as np

# input to softmax function
input_to_softmax = [0.5, 1.7, 0.1]

# denominator of softmax function
# summation of exponentials
exp_sum = np.exp(input_to_softmax[0]) + np.exp(input_to_softmax[1]) 
+ np.exp(input_to_softmax[2])

# softmax function outputs
softmax_outputs = [round(np.exp(input_to_softmax[0])/exp_sum, 1),
                   round(np.exp(input_to_softmax[1])/exp_sum, 1),
                   round(np.exp(input_to_softmax[2])/exp_sum, 1)]

# print the siftmax function outputs
print(softmax_outputs)

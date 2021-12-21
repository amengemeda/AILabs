import pandas as pd
import numpy as np

from numpy import array
from sklearn.preprocessing import Normalizer
from keras.activations import sigmoid
from keras.losses import mse
from numpy.random import uniform

batch_size = 1

data = {'Day 1': [30, 40, 50, 20, 15, 60], 'Day 2': [40, 50, 20, 15, 60, 70],
        'Day 3': [50, 20, 15, 60, 70, 50], 'Target': [20, 15, 60, 70, 50, 40]}

dataset = pd.DataFrame(data)

X = dataset.drop('Target', axis=1)
y = dataset['Target']

X_norm = Normalizer(norm='max').fit_transform(X)

np.reshape(array(y), (1, -1))
y_norm = Normalizer(norm='max').fit_transform(np.reshape(array(y), (1, -1)))

weight_1 = uniform(-1, 1, (3, 2))  # shape 3 by 2
weight_2 = uniform(-1, 1, (2, 1))

for i in range(100):
    X_norm[0:batch_size]
    output_1 = X_norm[0:batch_size] @ weight_1
    act_output = sigmoid(output_1).numpy()
    pred_output = act_output @ weight_2
    pred_output = np.reshape(pred_output, (1, -1))

    # Create a matrix of ones
    ones = uniform(1, 1, (1, 1))  # shape 1 by 6

    # Error at the output layer (node K)
    error_output_layer = (y_norm - pred_output) * (pred_output * (ones - pred_output))
    error_output_layer_constant = error_output_layer[0][0]

    # Extracting outputs of node J
    output_j = act_output[:, 0]

    # Create a matrix of weight_jk
    weight_2_j = uniform(weight_2[0], weight_2[0], (1, 1))  # shape 1 by 6

    # Error at the hidden layer (node J)
    error_hidden_layer_j = error_output_layer_constant * weight_2_j * output_j * (ones - output_j)

    # Extracting outputs of node I
    output_i = act_output[:, 1]

    # Create a matrix of weight_ik
    weight_2_i = uniform(weight_2[1], weight_2[1], (1, 1))  # shape 1 by 6

    # Error at the hidden layer (node I)
    error_hidden_layer_i = error_output_layer_constant * weight_2_i * output_i * (ones - output_i)

    # **`Weight Updates using Delta rule `**
    # *𝑊𝑛𝑒𝑤 = 𝑊𝑐𝑢𝑟𝑟𝑒𝑛𝑡 + Δ𝑊𝑐𝑢𝑟𝑟𝑒𝑛t*
    # *Δ𝑊𝑐𝑢𝑟𝑟𝑒𝑛𝑡 𝑖𝑠 𝑐𝑜𝑚𝑝𝑢𝑡𝑒𝑑 𝑎𝑠 (𝜂) [𝐸𝑟𝑟𝑜𝑟(𝑘)](𝑂𝑘)*
    learning_rate = 0.03

    # Creating a matrix of learning_rate
    a = np.array(error_hidden_layer_j)
    b = np.array(error_hidden_layer_i)
    hidden_layer_errors = np.concatenate((a, b), axis=1)

    hidden_layer_outputs = np.concatenate((output_j, output_i), axis=0)
    hidden_layer_outputs = np.reshape(hidden_layer_outputs, (1, 2))

    # Finding delta for Weight_1
    Delta_weight_1 = learning_rate * hidden_layer_errors * hidden_layer_outputs

    # Adjusting weight_1
    Weight_1_new = weight_1 + Delta_weight_1

    # Finding delta for Weight_2
    output_layer_outputs = pred_output
    error_output_layer = np.reshape(array(error_output_layer_constant), (1, 1))
    Delta_weight_2 = learning_rate * error_output_layer * output_layer_outputs

    # Adjusting weight_2
    Weight_2_new = weight_2 + Delta_weight_2
    Weight_2_new

    # Reinitializing new weights
    weight_1 = Weight_1_new
    weight_2 = Weight_2_new
    print("\n\nEpoch: ", (i + 1))
    print("\nWeight 1:\n", weight_1)
    print("\nWeight 2:\n", weight_2)
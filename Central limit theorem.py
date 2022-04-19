import numpy
import numpy as np
import random
from matplotlib import pyplot as plt
import math

def sum_of_array_items(array):
    sum_of_items =0
    for i in range(len(array)):
        sum_of_items += array[i]
    return sum_of_items

def uniform_value_generator(numberofvalue):
    my_array = []
    for j in range(200000):
        value =0
        for i in range(numberofvalue):
            value1 = random.uniform(0,1)
            value += value1
        my_array.append(value)
    return my_array

def dependent_array_generator():
    dependent_array = []
    for j in range(200000):
        sum_values =0
        value = random.uniform(90, 110)
        sum_values += value
        for i in range(49):
            if value < 99:
                value = random.uniform(0,200)
                sum_values += value
            else :
                value = random.uniform(98,102)
                sum_values += value
        dependent_array.append(sum_values)
    return dependent_array

def different_sampled_value_generator():
    arr = []
    for j in range(200000):
        sum_values =0
        for i in range(50):
            a = random.uniform(0,1)
            b = random.uniform(0,1)
            if a > b:
                value = random.uniform(b,a-b)
            else :
                value = random.uniform(a,b-a)
            sum_values += value
        arr.append(sum_values)
    return arr

def printing_function(array, x , experiment_number):
    mean = sum_of_array_items(array) / len(array)
    standard_deviation = np.std(array)
    print("mean {}".format(experiment_number) + ": {}" .format(mean))
    print("standard deviation {} ".format(experiment_number) + ": {}".format(standard_deviation))
    a1 = mean + standard_deviation * np.random.randn(200000)
    f1 = 1 / (standard_deviation * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * standard_deviation ** 2))
    plt.plot(x, f1, color="g")
    plt.hist(a1, 100, density=True, facecolor='y')
    plt.title("EXPERIMENT {}" .format(experiment_number))
    plt.show()

entry = int(input("enter the experiment number: "))

if entry== 1:
    # EXPERIMENT 1
    array1= uniform_value_generator(2)
    x1 = np.linspace(0, 2, 100)
    printing_function(array1,x1,1)
elif entry==2:
    # EXPERIMENT 2
    array2 = uniform_value_generator(4)
    x2 = np.linspace(0,4,200)
    printing_function(array2, x2,2)
elif entry==3:
    # EXPERIMENT 3
    array3 = uniform_value_generator(50)
    x3 = np.linspace(0, 50, 2500)
    printing_function(array3, x3,3)
elif entry == 4:
    # EXPERIMENT 4
    array4 = dependent_array_generator()
    x4 = np.linspace(0, 10000, 2500)
    printing_function(array4,x4, 4)
elif entry == 5:
    # EXPERİMENT 5
    array5 = different_sampled_value_generator()
    x5 = np.linspace(0, 50, 2500)
    printing_function(array5, x5, 5)





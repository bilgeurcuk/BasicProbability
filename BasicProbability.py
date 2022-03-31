import numpy
from matplotlib import pyplot as plt
import random

N= [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
# theoretical probability of p1
no_three_dice = (5 / 6) ** 5
P1 = (1 - no_three_dice)

# theoretical probability of p2
a = (1 - (5 / 6) ** 5)  # having three condition
b = 1-(3/6)**5  # having even condition
c = (2 / 6) ** 5  # no three, no even condition
sum_of_all_conditions = a + b + c
intersection_set = sum_of_all_conditions - 1  # this is what conditions say
P2 = intersection_set / b  # because the given(known) situation, intersection set must be divided by the known.

# theoretical probability of p3

# if there is only one even ,and it is known we can act like there is only four dice
# and there is no even and at least one three.
# that means our general set is {1,3,5} for this four dice.
no_three_probability = (2 / 3) ** 4
P3 = 1 - no_three_probability

# empirical probability of p1
emp_prob1_array = []
for i in range(len(N)):
    three_counter = 0
    for j in range(N[i]):
        integer_list = []
        for k in range(5):
            random_integer = random.randint(1, 6)
            integer_list.append(random_integer)

            if 3 == integer_list[k]:
                three_counter += 1
                break
    empirical_probability_p1 = (three_counter / N[i])
    emp_prob1_array.append(empirical_probability_p1)


# empirical probability of p2
emp_prob2_array = []
for i in range(len(N)):
    even_counter = 0
    for j in range(N[i]):
        integer_list = []
        for k in range(5):
            random_integer = random.randint(1, 6)
            integer_list.append(random_integer)

        if 3 in integer_list:
            if 2 in integer_list or 4 in integer_list or 6 in integer_list:
                even_counter += 1

    empirical_probability_p2 = (even_counter / N[i])/(31/32)
    emp_prob2_array.append(empirical_probability_p2)
# because the given(known) situation, intersection set must be divided by the known.
empirical_probability_p2 = empirical_probability_p2

# empirical probability of p3
emp_prob3_array = []
for i in range(len(N)):
    counter = 0
    for j in range(N[i]):
        integer_list = []
        for k in range(4):
            number_list = [1, 3, 5]
            random_integer = random.choice(number_list)
            integer_list.append(random_integer)

        if 3 in integer_list:
            counter += 1

    empirical_probability_p3 = (counter / N[i])

    emp_prob3_array.append(empirical_probability_p3)

which_probability = input("please the number(1-2-3): ")

if which_probability == "1":
    # plot of p1
    print("theoretical probability of P1 is ", P1)
    print("Empirical probability of P1 is : ", empirical_probability_p1)
    plt.axhline(y=P1, color="red")
    plt.plot(N, emp_prob1_array)
    plt.xscale("log")
    plt.show()
elif which_probability == "2":
    # plot of p2
    print("theoretical probability of P2 is ", P2)
    print("Empirical probability of P2 is : ", empirical_probability_p2)
    plt.axhline(y=P2, color="purple")
    plt.plot(N, emp_prob2_array)
    plt.xscale("log")
    plt.show()
elif which_probability == "3":
    # plot of P3
    print("theoretical probability of P3 is ", P3)
    print("Empirical probability of P3 is : ", empirical_probability_p3)
    plt.axhline(y=P3, color="purple")
    plt.plot(N, emp_prob3_array)
    plt.xscale("log")
    plt.show()

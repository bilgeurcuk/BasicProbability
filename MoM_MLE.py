from matplotlib import pyplot as plt
import numpy as np

X = [0.3, 0.6, 0.8, 0.9]
N = [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]


# f(x) = (2*theta^^)/x^3


def mom_estimate(arr):
    average_of_sample = sum(arr) / len(arr)
    theta = average_of_sample / 2
    return theta


def mle_estimate(x):
    min_num = x[0]
    for i in range(len(x)):
        if min_num > x[i]:
            min_num = x[i]
        else:
            continue
    return min_num


def population_generation():
    fu_arr = []
    for i in range(10000000):
        u = np.random.rand()
        f_u = np.sqrt(5.76 / (1 - u))
        fu_arr.append(f_u)
    return fu_arr


P = population_generation()


def func(theta, x):
    return (2 * (theta ** 2)) / x ** 3


def mom_and_mle_calculator(P, N):
    for i in range(len(N)):
        theta_arr = []
        theta_arr2 = []
        for k in range(100000):
            sample_arr = []
            for j in range(N[i]):
                indices = np.random.randint(0, 10000000)
                sample_arr.append(P[indices])
            mom_thetas = mom_estimate(sample_arr)
            mle_thetas = mle_estimate(sample_arr)
            theta_arr.append(mom_thetas)
            theta_arr2.append(mle_thetas)

        if N[i] == 1:
            continue
        else:

            plt.figure()
            plt.hist(theta_arr, bins=np.linspace(0, 4.8, 100), alpha=0.5, density=True,
                     label=f"MoM estimate histogram for N = {N[i]}")
            plt.hist(theta_arr2, bins=np.linspace(0, 4.8, 100), alpha=0.5, density=True,
                     label=f"MLE estimate histogram for N = {N[i]}")
            plt.legend()
            plt.show()

        print("for N = ", N[i])
        print("MoM estimate mean: ", round(np.mean(theta_arr), 2), "MoM estimate std: ", round(np.std(theta_arr), 2))
        print("MLE estimate mean:", round(np.mean(theta_arr2), 2), "MLE estimate std: ", round(np.std(theta_arr2), 2))


print("MoM estimate for the sample is: ", round(mom_estimate(X), 2))
print("MLE estimate for the sample is: ", round(mle_estimate(X), 2))

plt.figure()
x = np.linspace(2.5, 20.0, 100)
plt.plot(x, func(2.4, x), color='purple')
plt.hist(P, bins=np.linspace(2.5, 20.0, 100), alpha=0.5, density=True)
plt.show()

mom_and_mle_calculator(P, N)

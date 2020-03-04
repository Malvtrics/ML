import random
import numpy as np
import time
import matplotlib.pyplot as plt


def GD(data, mode='minibatch-sgd', lr=0.01, presicion=0.0001, max_iters=10000, batch_size=16):
    N = len(data)
    x = data[:, 0:2]
    y = data[:, -1]
    theta = np.array([1, 1])
    loss = 10
    curr_iters = 0
    plot_x = []
    plot_y = []

    time_start = time.time()
    while loss > presicion and curr_iters < max_iters:
        if mode == 'gd':
            y_predict = np.matmul(x, theta)
            err = np.dot(x.T, y_predict - y) / N
            theta = theta - lr * err
            loss = np.sum(np.power((np.matmul(x, theta) - y), 2)) / (2 * N)
        elif mode == 'sgd':
            i = random.randint(0, N-1)
            y_predict = np.matmul(x[i], theta)
            err = np.dot(x[i].T, y_predict - y[i])
            theta = theta - lr * err
            loss = np.sum(np.power((np.matmul(x, theta) - y), 2)) / (2 * N)
        else:
            start = (curr_iters * batch_size) % N
            end = min(start + batch_size, N)  # https://blog.csdn.net/Together_CZ/article/details/88408961
            y_predict = np.matmul(x[start:end], theta)
            err = np.dot(x[start:end].T, y_predict - y[start:end])
            theta = theta - lr * err
            loss = np.sum(np.power((np.matmul(x, theta) - y), 2)) / (2 * N)
        curr_iters += 1
        plot_x.append(curr_iters)
        plot_y.append(loss)
    time_end = time.time()

    print('time cost:', time_end - time_start)
    print('theta:', theta)
    print('final loss:', loss)
    print('total iters:', curr_iters)
    return plot_x, plot_y


# prepare data
N = [50, 5000, 50000, 500000]
for i in range(len(N)):

    x = np.random.randn(N[i]).reshape(N[i] // 2, 2)
    np.random.shuffle(x)
    y = np.reshape(6 * x[:, 0] + 8 * x[:, 1], (N[i] // 2, 1))
    data = np.hstack((x, y))

    print('----------Gradient Descend----------')
    x_gd, y_gd = GD(data, mode='gd')
    print('----------Stochastic Gradient Descend----------')
    x_sgd, y_sgd = GD(data, mode='sgd')
    print('----------Mini-batch Stochastic Gradient Descent----------')
    x_msgd, y_msgd = GD(data)

    s = '22' + str(i+1)
    ax = plt.subplot(s)
    ax.plot(x_gd, y_gd, 'b', label='GD')
    ax.plot(x_sgd, y_sgd, 'g', label='SGD')
    ax.plot(x_msgd, y_msgd, 'r', label='MSGD')
    ax.legend()

plt.show()

#可以看出数据量在50万量级的时候，其实SGD和GD的速度已经差不多了，也就意味着SGD的边缘效应越来越小
#minibatch无论在何时都是最牛逼的


import numpy as np


def fun1(x, y):
    return y


def answer_fun1(x, y):
    return np.exp(x)


def fun2(x, y):
    return 7 * y + 1


def answer_fun2(x, y):
    return (np.exp(7 * x) - 1) / 7


def predict_Euler(f, x, y, h):
    return y + h * f(x, y)


def predict_Runge_Kutta_2k(f, x, y, h):
    y_tilda = y + h * f(x, y)
    return y + h / 2 * (f(x, y) + f(x + h, y_tilda))


def predict_Runge_Kutta_4k(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h / 2, y + h / 2 * k1)
    k3 = f(x + h / 2, y + h / 2 * k2)
    k4 = f(x + h, y + h * k3)
    return y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def draw_plot(X, y0, h, real_fun, answer_fun, prediction_fun, plots):
    Y = [y0]
    for index in range(1, len(X)):
        predict = prediction_fun(real_fun, X[index - 1], Y[index - 1], h)
        Y.append(predict)
    Y_real = [answer_fun(X[index], Y[index]) for index in range(len(X))]
    Y_diff = [abs(Y_real[index] - Y[index]) for index in range(len(X))]
    plots[0].plot(X, Y_real, "g")  # real
    plots[0].plot(X, Y, "r")  # predict
    plots[1].plot(X, Y_diff)  # diff

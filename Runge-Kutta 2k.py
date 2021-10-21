import matplotlib.pyplot as plt

from predictions import *

fig, p = plt.subplots(2, 2)
fig.suptitle("Runge-Kutta 2k")

h = 0.01
p[0][0].set_title("y' = y")
draw_plot(np.arange(0, 4, h), 1, h, fun1, answer_fun1, predict_Runge_Kutta_2k, [p[0][0], p[1][0]])

p[0][1].set_title("y' = 7y+1")
h = 0.01
draw_plot(np.arange(0, 1, h), 0, h, fun2, answer_fun2, predict_Runge_Kutta_2k, [p[0][1], p[1][1]])
plt.show()

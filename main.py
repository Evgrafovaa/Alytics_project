import matplotlib.pyplot as plt
import numpy as np

#http://lybniz2.sourceforge.net/safeeval.html

def eval_num(line, t):
    res = eval(line)
    return res


def print_func(line, min_t, max_t, dt):
    t = np.arange(min_t, max_t, dt)
    f = [eval_num(line, n) for n in t]
    plt.plot(t, f)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.show()

def main():
    print_func("t*t-2", 0, 10, 1)

main()
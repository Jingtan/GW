import matplotlib.pyplot as plt
import math


'''
设置参数：
设置粒子所组成的圆的半径为1，在圆中取60个散点，设置引力波振幅h_0为1.
'''
r = 1
n = 60
h_0 = 1


def plot():
    for i in range(n):
        # 每个时间切片下：
        t = i / n * 2 * math.pi
        x_list = []
        y_list = []
        x2_list = []
        y2_list = []
        for j in range(n):
            # 根据TT规范，只有两个方向有影响：
            s1 = r*math.cos(j / n * 2 * math.pi)
            s2 = r*math.sin(j / n * 2 * math.pi)

            # 考虑加模情况
            x = (1 / 2 * h_0 * math.sin(t) + 1) * s1
            x_list.append(x)
            y = (-1 / 2 * h_0 * math.sin(t) + 1) * s2
            y_list.append(y)

            # 考虑叉模情况：
            x2 = s1 + 1/2 * h_0 * math.sin(t) * s2
            x2_list.append(x2)
            y2 = s2 + 1/2 * h_0 * math.sin(t) * s1
            y2_list.append(y2)

        plt.figure(num="1", figsize=(12, 6))
        # 加模作图
        ax1 = plt.subplot(1, 2, 1)
        plt.scatter(x_list, y_list)
        plt.title("h+")
        plt.xticks([-2, 2])
        plt.yticks([-2, 2])

        # 叉模作图
        ax2 = plt.subplot(1, 2, 2)
        plt.scatter(x2_list, y2_list)
        plt.title("hx")
        plt.xticks([-2, 2])
        plt.yticks([-2, 2])
        plt.pause(0.0001)
        plt.show(block=False)
        plt.clf()



n1 = 5
counter = 0
while counter < n1:
    counter += 1
    plot()

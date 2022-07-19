import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [5, 7, 4]

x2 = [10, 11, 14]
y2 = [5, 9, 7]

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 1, 5, 7, 4, 9]

plt.scatter(x, y, label='scitscat', color='k', marker='*', s=10)

# plt.plot(x1, y1, label='First Line')
# plt.plot(x2, y2, label='Second Line')
plt.xlabel('Plot Number')  # legend on x axis
plt.ylabel('Important var')
plt.title('Interesting graph\nCheck it out')  # Title of our graph

plt.legend()  # to use it, you should add 'label' argument to 'plot' function

plt.show()  # to take it from the background




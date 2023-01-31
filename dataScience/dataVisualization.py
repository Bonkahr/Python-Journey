from matplotlib import pyplot as plt

data = [[0, 1, 2, 3, 4, 5, 6, 7], [4, 6, 7, 8, 9, 11, 23, 34]]
x = plt.plot(data[0], data[1], color='red', marker='*', linestyle='solid')
plt.title('Thengrolius')
plt.ylabel('Kimngolians')
plt.xlabel('Kafunda')
plt.savefig('plots/capira')

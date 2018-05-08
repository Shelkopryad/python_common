from matplotlib import pyplot as plt
import numpy as np

arg = input("choose example\n")

if arg == "1":
  variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
  bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

  total_error = [x + y for x , y in zip(variance, bias_squared)]

  xs = [i for i, _ in enumerate(variance)]

  plt.plot(xs, variance,      'g-', label='дисперсия')
  plt.plot(xs, bias_squared,  'r-.', label='смещение ^ 2')
  plt.plot(xs, total_error,   'b:', label='суммарная ошибка')

  plt.legend(loc=9)
  plt.xlabel("Сложность модели")
  plt.title("Компромисс между смещением и дисперсией")

if arg == "2":
  np.random.seed(19680801)
  data = np.random.randn(2, 100)

  fig, axs = plt.subplots(2, 2, figsize=(5, 5))
  axs[0, 0].hist(data[0])
  axs[1, 0].scatter(data[0], data[1])
  axs[0, 1].plot(data[0], data[1])
  axs[1, 1].hist2d(data[0], data[1])

plt.style.use('ggplot')
plt.show()
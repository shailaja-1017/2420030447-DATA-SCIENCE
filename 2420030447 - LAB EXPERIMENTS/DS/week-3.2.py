import numpy as np

pointA = np.array([3,7,2])
pointB = np.array([8,4,10])

manhattan_dist = np.sum(np.abs(pointA - pointB))
print("Manhattan Distance:", manhattan_dist)

similarity_man = 1 / (1 + manhattan_dist)
print("Manhattan Similarity:", similarity_man)
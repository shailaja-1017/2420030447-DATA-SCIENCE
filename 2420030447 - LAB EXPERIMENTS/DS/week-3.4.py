import numpy as np
from scipy.spatial import distance
pointA = np.array([3,7,2])
pointB = np.array([8,4,10])
e_dist=distance.euclidean(pointA,pointB)
print("Euclideans Distance:",e_dist)
similarity_euc= 1/(1+e_dist)
print("Euclideans Similarity:",similarity_euc)


import numpy as np
pointA = np.array([3,7,2])
pointB = np.array([8,4,10])
manhattan_dist = np.sum(np.abs(pointA - pointB))
print("Manhattan Distance:", manhattan_dist)
similarity_man = 1 / (1 + manhattan_dist)
print("Manhattan Similarity:", similarity_man)


import numpy as np
from scipy.spatial import distance
pointA = np.array([3,7,2])
pointB = np.array([8,4,10])
m_dist=distance.minkowski(pointA,pointB,p=3)
print("Minkowski Distance:",m_dist)
similarity_min= 1/(1+m_dist)
print("Minkowski Similarity(p=3):",similarity_min)


import numpy as np
from scipy.spatial import distance
pointA = np.array([3,7,2])
pointB = np.array([8,4,10])
m_dist=distance.minkowski(pointA,pointB,p=2)
print("Minkowski Distance:",m_dist)
similarity_min= 1/(1+m_dist)
print("Minkowski Similarity(p=2):",similarity_min)


import numpy as np
from scipy.spatial import distance
pointA = np.array([3,7,2])
pointB = np.array([8,4,10])
m_dist=distance.minkowski(pointA,pointB,p=1)
print("Minkowski Distance:",m_dist)
similarity_min= 1/(1+m_dist)
print("Minkowski Similarity(p=1):",similarity_min)
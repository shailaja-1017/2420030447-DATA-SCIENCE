import numpy as np
from scipy.spatial import distance
pointA = np.array([3,7,2])
pointB = np.array([8,4,10])
m_dist=distance.minkowski(pointA,pointB,p=3)
print("Minkowski Distance:",m_dist)
similarity_min= 1/(1+m_dist)
print("Minkowski Similarity(p=3):",similarity_min)
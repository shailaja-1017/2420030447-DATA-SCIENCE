import numpy as np
from scipy.spatial import distance
pointA=np.array([2,4,6])
pointB=np.array([5,1,9])
e_dist=distance.euclidean(pointA,pointB)
print("Euclideans Distance:",e_dist)
similarity_euc= 1/(1+e_dist)
print("Euclideans Distance:",similarity_euc)
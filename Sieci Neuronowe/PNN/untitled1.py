import numpy as np
import pandas as pd
from numpy import genfromtxt
import matplotlib.pyplot as plt

dane = pd.read_csv('Simple_data_points_for_PNN.csv', sep=',',header=0)
przetworzone_dane = np.array([ dane['Feature 1'].tolist(),dane['Feature 2'].tolist()]).T
print (dane)
print (przetworzone_dane)
grupy = dane.groupby('Class')
liczba_klas = len(grupy) 
dictionary_of_sum = {}
numrber_of_features  = 2 
sigma = 1
increament_current_row_in_matrix = 0
point_want_to_classify = [0.6,0.6]
for k in range(1,liczba_klas+1):
	dictionary_of_sum[k] = 0
	number_of_data_point_from_class_k = len(grupy.get_group(k))
	temp_summnation = 0.0
	for i in range(1,number_of_data_point_from_class_k+1):
		tempx = (point_want_to_classify[0] - przetworzone_dane[increament_current_row_in_matrix][0]) * (point_want_to_classify[0] - przetworzone_dane[increament_current_row_in_matrix][0]) 
		tempy = (point_want_to_classify[1] - przetworzone_dane[increament_current_row_in_matrix][1]) * (point_want_to_classify[1] - przetworzone_dane[increament_current_row_in_matrix][1]) 
		temp_sum = -1 * (tempx + tempy)
		temp_sum = temp_sum/( 2 * np.power(sigma,2) )
		temp_summnation = temp_summnation + temp_sum
		increament_current_row_in_matrix  = increament_current_row_in_matrix + 1
	dictionary_of_sum[k]  = temp_summnation 
classified_class = str( max(dictionary_of_sum, key=dictionary_of_sum.get) )
grupy = dane.groupby('Class')
fig, ax = plt.subplots()
ax.margins(0.05)
for name, group in grupy:
    ax.plot(group['Feature 1'], group['Feature 2'], marker='o', linestyle='', ms=12, label=name)
ax.plot(point_want_to_classify[0], point_want_to_classify[1], marker='o', linestyle='', ms=12)
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([0,1])
plt.title('Classified as : ' + str(classified_class) )
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
import numpy as np

km = np.loadtxt('3º ANO\TED\Arquivos_Python_Data_Science_Numpy\carros-km.txt')
anos = np.loadtxt('3º ANO\TED\Arquivos_Python_Data_Science_Numpy\carros-km.txt',dtype=int)

km_Media = km / (2021-anos)

print(km_Media)
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 22:36:09 2018

@author: Carolina
"""

#soporta la carga de multiples tipos de archivos
#si se desea cargar archivos de texto se podria usar numpy.loadtxt
import scipy.io as sio;
# libreria para hacer graficos tipos matlab (pyplot)
import matplotlib.pyplot as plt;
#libreria de manejo de arreglos de grandes dimensiones (a diferencia de las listas basicas de python)
import numpy as np;
#libreria con rutinas de PDS
import scipy.signal as signal;

import statistics as stats;
#PRIMERA PARTE CARGA Y MANIPULACION BASICA

#loading data
mat_contents = sio.loadmat('signals.mat')
#los datos se cargan como un diccionario, se puede evaluar los campos que contiene
print("Los campos cargados son: " + str(mat_contents.keys()));

ECG = mat_contents['ECG_asRecording'];
print("Variable python: " + str(type(ECG)));
print("Tipo de variable cargada: " + str(ECG.dtype));
print("Dimensiones de los datos cargados: " + str(ECG.shape));
print("Numero de dimensiones: " + str(ECG.ndim));
print("Tamanio: " + str(ECG.size));
print("Tamanio en memoria (bytes): " + str(ECG.nbytes));

ECG_Fil = mat_contents['ECG_filtered'];
EMG1 = mat_contents['EMG_asRecording1'];
EMG2 = mat_contents['EMG_asRecording2'];
EMG1_Fil = mat_contents['EMG_filtered1'];
EMG2_Fil = mat_contents['EMG_filtered2'];

# vector de tiempo
 
Fs= mat_contents['Fs'];
print(Fs)
print(ECG.shape)
t_ECG=np.arange(0, ECG.size/Fs, 1/Fs) # Tiempo de duración de la señal ECG
print(t_ECG.shape)
t_ECG=t_ECG.reshape((1,t_ECG.size))
print(t_ECG.shape)

#plt.subplot(211)
plt.plot(t_ECG,ECG)
#plt.subplot(212)
#plt.plot(ECG)

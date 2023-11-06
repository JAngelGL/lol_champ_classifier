# -*- coding: utf-8 -*-
"""Test_Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nFWTAxTfwm_Rmjr8TsJJQhdS5SRhzcji
"""

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Cargar el modelo entrenado
model = tf.keras.models.load_model('lol_champion_classifier3.h5')

# Lista de nombres de campeones
champion_names = ['atroxx', 'ahir', 'akali', 'akshan','alistar' ]  # Agrega el nombre de tus campeones aquí en el mismo orden que se usó para el entrenamiento

# Cargar una imagen para probar (reemplaza 'imagen_a_probar.jpg' con la ruta de tu imagen)
img_path = '/content/aatroxturn.jpg' #Cambiar a la ruta del archivo

#img_path = '/test_images'
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normaliza la imagen

# Realizar una predicción
predictions = model.predict(img_array)

# Obtener la clase predicha
predicted_class_index = np.argmax(predictions)
predicted_champion = champion_names[predicted_class_index]

print(f"El campeón predicho es: {predicted_champion}")

# Portafolio de Implementación - League of Legends Champion Performance Prediction

## Introducción

En este repositorio, presentamos un emocionante proyecto centrado en el popular juego "League of Legends". Hemos desarrollado un modelo de deep learning utilizando un conjunto de datos personalizado que comprende 60 campeones del juego. Nuestro objetivo es utilizar este modelo para analizar y predecir el rendimiento de los campeones en el juego.

## Data Set

El dataset utilizado para entrenar esta red neuronal fue creado de manera personalizada, ya que la mayoría de las plataformas de datos de uso libre no se ajustaban al enfoque que deseábamos para nuestro portafolio. Para construir este dataset, realizamos grabaciones de video de aproximadamente 8 a 10 segundos de juego con 60 campeones diferentes en la Grieta del Invocador. Luego, utilizamos la biblioteca OpenCV para dividir cada uno de los videos en frames, generando así alrededor de 300 a 400 imágenes por campeón/clase.

El script utilizado para realizar esta tarea se encuentra en este mismo repositorio y lleva por nombre "nex_file.py". Este script toma los videos de un directorio específico, los divide en frames y crea una carpeta para cada campeón con el nombre de los archivos correspondientes.

## Estructura del Repositorio

- **data/**: Carpeta que contiene el dataset de imágenes de campeones.

- **models/**: Carpeta donde se almacenan los modelos de deep learning entrenados.

- **nex_file.py**: Script de Python utilizado para dividir los videos en frames y organizar el dataset.

- **5_champ_classifier.ipynb**: Jupyter Notebook con el código para el entrenamiento del modelo.

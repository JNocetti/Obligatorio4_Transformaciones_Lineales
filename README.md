# Transformaciones_Lineales
Proyecto en grupo de algebra aplicada

## Objetivo:
En este proyecto se espera que el estudiante ponga en práctica los conocimientos vistos en la unidad 4 del curso sobre Transformaciones Lineales, y valores y vectores propios de una matriz. La aplicación está relacionada con el procesamiento de imágenes.

## Introducción
Transformaciones lineales
Las transformaciones lineales son un concepto fundamental en el ámbito del álgebra lineal que desempeñan un papel crucial en diversos campos. Estas transformaciones describen cómo los espacios vectoriales y sus elementos se relacionan y cambian bajo ciertas operaciones matriciales o lineales.

Tenemos varios tipos de transformaciones lineales y aplicaciones de las mismas. En el presente trabajo el foco está puesto en el procesamiento de imágenes. Recordemos que una imagen puede ser vista como una matriz donde cada una de sus entradas se corresponde con los valores de los píxeles (que van de 0 a 255). Dentro de las transforamciones que podemos aplicarle a una imagen tenemos: rotación, escalado, deformación (distorsión a lo largo de un eje), reflexión y proyección.

Estas transformaciones permiten modificar la apariencia de una imagen, lo que resulta útil en diversas aplicaciones, como la corrección de imágenes y la mejora de la visualización.

En este trabajo, estaremos aplicando las siguientes:

* Escalado (Scaling): El escalado es aquella operación que aumenta/disminuye el tamaño de los objetos . En un escalado, cada vector  v , se escala por un factor k, es decir  T(v)=kv , para cada  v∈R² . Esto permite cambiar el tamaño o la proporción de una imagen.

![image](https://github.com/JNocetti/Transformaciones_Lineales/assets/88642593/a633c5b1-46ef-4294-bdfc-a853cddf4e20)

* Rotación: La rotación implica girar una imagen alrededor de un punto o eje específico que representamos con la letra  θ . Las matrices de rotación son ortonormales.
  ![image](https://github.com/JNocetti/Transformaciones_Lineales/assets/88642593/9208e96e-d34e-4545-941d-1c4614291abb)

* Deformación (Shearing): La deformación implica cambiar la forma de una imagen de manera que no necesariamente se conservan las distancias y ángulos entre píxels, alterando localmente la posición de los mismos. Los píxeles individuales se desplazan a nuevas ubicaciones, lo que cambia la forma general de la imagen. Cuando ejecutamos una deformación, la imagen se puede inclinar tanto en sentido horizontal como en sentido vertical. Lo que se hace es mapear un punto  P  en un correspondiente punto  P′  y un angulo  α  se forma entre  PP′  y el eje  x .
  ![image](https://github.com/JNocetti/Transformaciones_Lineales/assets/88642593/06bf3740-a31b-4a1d-863b-4a85a6fd41f0)

 ## Compresión de imágenes utilizando SVD
La compresión de imágenes comprende un conjunto de técnicas que se aplican con el fin de reducir el volumen de información que contienen. Muchas veces las imágenes utilizan volúmenes de datos muy altos, del orden de mega y giga bytes.

Esta compresión se puede realizar a través de la descomposición de valores singulares (SVD), que es una técnica de álgebra lineal utilizada en diversos campos, incluido el procesamiento de imágenes. De manera simplificada, SVD se puede aplicar a una imagen para descomponerla en sus componentes principales y conservar los componentes que almacenan mayor información.

Entonces, tenemos que una matriz  M  de tamaño  m×n  y de rango  r  puede descomponerse como el producto de tres matrices de la forma  M=U.S.VT , lo que se denomina Descomposición en valores singulares de la matriz M (SVD - Singular Value Descomposition) dónde:

* U  es una matriz  m×r  ortonormal por columnas, es decir, cada una de sus columnas es un vector de norma 1 y el producto punto de dos columnas cualesquiera es 0.Esta matriz representa las relaciones entre filas (píxeles) de la imagen. Cada columna de U se denomina "vector singular izquierdo" y está relacionada con una característica o patrón particular en la imagen.
* S  es una matriz diagonal que contiene los valores singulares de  M . Los valores singulares son las raíces cuadradas de los valores propios de  Mt∗M . Estos valores le indican qué tan importante es cada vector singular izquierdo y derecho correspondiente para representar la imagen. Los valores singulares están ordenados desde el más importante (arriba a la izquierda) al menos importante (abajo a la derecha).
* V  es una matriz  r×n  ortonormal por filas, es decir, cada una de sus filas es un vector de norma 1 y el producto punto de dos filas cualesquiera es 0. Esta matriz representa las relaciones entre columnas (píxeles) de la imagen. Cada columna de  VT  se denomina "vector singular derecho" y está relacionada con una característica o patrón particular en la imagen.
Una imagen contiene información redundante, es decir, que puede ser eliminada sin que el efecto visual sea notable, y se podría sustituir  M  por otra matriz  M1  de menor rango. Para esto debemos descomponer la matriz de imagen y luego comprimir la información tomando solo cierta cantidad  k , con  1<k<r , de valores singulares.

## Pautas
Se pide:

Encontrar la matriz correpondiente a cada transformación lineal, que aplicada a una imagen, logre:
a) Rotarla un ángulo  θ 

b) Escalarla un factor  sx  en el eje horizontal y un factor  sy  en el eje vertical.

c) Deformarlarla un factor  dx  en el eje horizontal y un factor  dy  en el eje vertical.

Elegir una imagen con la cual se trabajara también en la Aplicación II y realizarle las transformaciones lineales anteriormente mencionadas implementando una función en Python. Probar con distintos valores de los parametros en cada caso, (al menos 2).

Explicar qué observa en cada transformación.

Aplicacion II - Compresión de Imagenes
Se pide:

Con la imagen elegida en la parte I, implementar en Python un algoritmo que comprima la imagen, utilizando la descomposición SVD como se detalló en la introducción.

Probar con distintos valores de k (al menos 4) y mostrar los resultados de las imágenes comprimidas. Comentar los resultados. Recordar que los valores están ordenados de mayor a menor, por lo que nos quedamos con los  k  mayores.

¿Qué ocurre al aumentar el valor de k? ¿Por qué sucede eso? ¿Qué representa el valor k en el contexto de la Descomposición de Valor Singular (SVD)?

¿Por que efectivamente el procedimiento realizado resulta en una compresión de la imagen?

## Sobre el informe
* El tiempo para entregar el informe es hasta el sábado 9 de Diciembre inclusive. La entrega se realizará por webasignatura.
* El informe deberá estar en formato pdf, la entrega también deberá incluir los scripts utilizados. Es importante que el informe sea autocontenido.
* El informe deberá contener título, fecha, nombre y cédula del estudiante.
* Se evaluaráa: prolijidad del informe, utilización correcta del idioma español, redacción, prolijidad del código presentado en los scripts, conclusiones.




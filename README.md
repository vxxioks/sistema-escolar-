# Sistema de Registro Escolar

Este es un programa en Python para administrar datos de estudiantes en un colegio. Permite registrarlos, calcular sus promedios de notas de forma automática y evaluar si están en situación de riesgo.

## Criterios de Riesgo
El sistema revisa los datos del alumno y entrega uno de estos 4 estados:
* **Riesgo Académico:** Si el promedio de notas es menor a 4.0.
* **Riesgo de Asistencia/Conducta:** Si tiene más de 15 faltas o más de 5 anotaciones negativas.
* **Riesgo Crítico:** Si tiene el promedio rojo y además cumple con el límite de faltas o anotaciones.
* **Sin Riesgo:** Si cumple con todo lo anterior positivamente.

## Conceptos de POO Utilizados
* **Clases y Objetos:** Se crearon dos clases principales: estudiante y sistemaEscolar.
* **Abstracción:** Solo se tomaron los datos realmente importantes para el problema (nombre, curso, notas, faltas, etc.), dejando de lado información innecesaria.
* **Encapsulamiento:** Se agruparon las variables y los comportamientos en una sola unidad.

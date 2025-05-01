# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

Este reto técnico consiste en procesar un archivo CSV que contiene información de transacciones bancarias y mostrar un reporte con los siguientes datos:
- balance final
- ID y transacción de mayor monto
- Número total de transacciones por tipo de transacción, débito o crédito.

## Instrucciones de ejecución:

Ejecutar el programa con Python y pasar como argumento el archivo que contiene la información de transacciones.

- En Windows: python reporte_transacciones.py data.csv
- En Linux: python3 reporte_transacciones.py data.csv

## Enfoque y solución:

La solución ha sido desarrollada usando el lenguaje de programación Python.

1. **Lógica de implementación**

   La lógica de implementación consiste en leer y extraer la información del archivo csv. Luego se decidió trabajar con centavos para el procesamiento de los montos de las transacciones con el fin de evitar errores de precisión con los decimales. Finalmente se muestran los resultados requeridos convertidos en formato moneda, dinero real.


   El procesamiento consiste en leer fila por fila el contenido del archivo csv y extraer por cada fila el id, tipo y monto de cada transacción. En cada lectura se extrae información y se van realizando operaciones con cada valor extraído:
   - Se van sumando los montos según el tipo de transacción y se va contabilizando si la transacción fue "Crédito" o "Débito". 
   - Se va comparando cada monto con el monto de la fila o transacción anterior para encontrar el monto mayor de todas las transacciones.
   
2. **Decisiones de diseño**

   - Se eligió trabajar en centavos haciendo conversiones para mejorar la precisión del resultado de balance final.
   - Se decidió pasar el archivo csv como argumento para mayor flexibilidad durante la ejecución en la terminal.
   - Se organizó el código en funciones para una mayor legibilidad.

## Estructura del proyecto

La estructura es la siguiente:

interbank-academy-25/
│
├── data.csv
├── reporte_transacciones.py
└── README.md

El archivo principal es reporte_transacciones.py que contiene toda la implementación del proyecto.
Es necesario pasar como argumento el archivo csv que contiene la información de las transacciones.


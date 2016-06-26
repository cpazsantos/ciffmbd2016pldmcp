# idmbd -- Innovando el Desarrollo de Modelos a través del Big Data

[![PyPI](https://img.shields.io/pypi/v/idmbd.svg?style=flat-square)](https://pypi.python.org/pypi/idmbd/)

1) Limpieza automatizada de datos; identificar los valores y / o filas no válidas y resolver automáticamente el problema, sea él NaN, falta de datos, valores atípicos, valores poco fiables, fuera del rango. Tu grupo debe pensar que solución quiere dar a cada situación e implementarla.

```python
DataCleaning(dataframe)
```
El parámeto de entrada del método es un dataframe. Como salida nos devolverá un nuevo dataframe.

2) Creación automática de ratio y selección de los mejores ratios utilizando Principal Component Analysis y árbol de decisión.
Mediante combinaciones de variables X y Y de la siguiente forma:
- (X-Y)/Y 
- X+Y
- X*Y
- X/Y
- X-Y 
- X^2

```python
Ratios_PCA_DT(dataframe, 'nombre_col_target')

```
Los parámetros de entrada del método son un dataframe y el nombre de la columna target. Como salida nos devolverá un nuevo dataframe con los ratios generados y seleccionados.

3) Utilizar Algoritmo Genético para estimar los parámetros de la regresión en una Regresión Logística

```python
GeneticLogisticRegression(dataframe, 'nombre_col_target')

```
Los parámetros de entrada del método son un dataframe y el nombre de la columna target. Como salida nos devolverá una lista con los parámetros de la regresión logística.

### Instalación

For Python 2.x and Python 3.x respectively:

```python
pip install idmbd
pip3 install idmbd

```

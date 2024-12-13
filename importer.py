# -*- coding: utf-8 -*-
"""Importer.ipynb

Original file is located at
    https://colab.research.google.com/drive/1JxL1pIP62AScIkyLl8KsVygUK9pprr9J
"""

def buscadorindexSTR(lista, nombre):
  """
  Toma una lista de cualquier cosa y busca el string a discresión consiguiendo una lista con 
  los indices donde ese string se encuentra
  ----------
  parámetros:
  lista: la lista de datos donde se consigue el string 
  nombre: nombre del dato a buscar
  ----------
  retorna: lista de indices donde el valor buscado se encuentra dentro de la lista
  """
  indices = []
  for i in range(len(lista)):
    if str(nombre) in lista[i:]:
      if lista.index(str(nombre),i,len(lista)) not in indices:
        indices.append(lista.index(str(nombre),i,len(lista)))
    else:
      continue
    
  return indices
    
    def buscadorindexFLOAT(lista, nombre):
  """
  Toma una lista de cualquier cosa y busca el float a discresión consiguiendo una lista con 
  los indices donde ese float se encuentra
  ----------
  parámetros:
  lista: la lista de datos donde se consigue el float 
  nombre: nombre del dato a buscar
  ----------
  retorna: lista de indices donde el valor buscado se encuentra dentro de la lista
  """
  indices = []
  for i in range(len(lista)):
    if int(nombre) in lista[i:]:
      if lista.index(int(nombre),i,len(lista)) not in indices:
        indices.append(lista.index(int(nombre),i,len(lista)))
    else:
      continue
    
  return indices

def buscadorindexINT(lista, nombre):
  """
  Toma una lista de cualquier cosa y busca el integer a discresión consiguiendo una lista con 
  los indices donde ese integer se encuentra
  ----------
  parámetros:
  lista: la lista de datos donde se consigue el integer 
  nombre: nombre del dato a buscar
  ----------
  retorna: lista de indices donde el valor buscado se encuentra dentro de la lista
  """
  indices = []
  for i in range(len(lista)):
    if int(nombre) in lista[i:]:
      if lista.index(int(nombre),i,len(lista)) not in indices:
        indices.append(lista.index(int(nombre),i,len(lista)))
    else:
      continue
    
  return indices
    
def correlacion(x,y):
  """
  Función que calcula el coeficiente de correlación dadas 2 listas para ambos ejes
  --------
  Parámetros:
  x: lista en el eje x
  y: lista en el eje y
  --------
  nota: si o si deben ser listas
  --------
  retorna: coeficiente de correlación 
  """
  xmed = mim.media_aritmetica(x)
  ymed = mim.media_aritmetica(y)

  numerador = 0
  for i in range(len(x)):
    numerador += (x[i]-xmed)*(y[i]-ymed)

  denom = 0
  for i in range(len(x)):
    denom += (x[i]-xmed)**2

  for i in range(len(y)):
    denom += (y[i]-ymed)**2

  return numerador / (denom**(1/2))

def lecturageneral(nombre):
  """
  Función que lee la columna de un archivo dado de manera general, sin depuraciones de nan,
  sin embargo depura valores no existentes aparte del nan
  --------
  Parámetros:
  nombre: dirección del archivo a leer
  lin: input que pide el valor de la columna para leer a discresión
  --------
  retorna: lista de los valores de la columna no depurados ni transformados
  """
  with open(nombre,"r") as archivo:
    array = []
    archivo.readline()
    lin = input("Ingrese la columna que desea leer: ")

    for linea in archivo:
      if linea != '\n' and linea != " " and linea != "":
        linea = linea.split()
        array.append(linea[int(lin)])
        
  archivo.close()
  return array
    
def lecturaconfloat(nombre):
  """
  Función que lee la columna de un archivo dado a discresión, o sea, lee la columna 
  depurando los nan
  --------
  Parámetros:
  nombre: dirección del archivo a leer
  lin: input que pide la columna a leer a discresión
  --------
  retorna: lista de los valores de la columna depurado de nans
  """
  with open(nombre,"r") as archivo:
    array = []
    archivo.readline()
    lin = input("Ingrese la columna que desea leer: ")

    for linea in archivo:
      if linea != '\n' and 'nan' not in linea and linea != " " and linea != "":
        linea = linea.split()
        array.append(float(linea[int(lin)]))

  archivo.close()
  return array


def encabezado(nombre):
  """
  Función que consigue solo la primera linea de un archivo,
  de esta manera uno puede conseguir los encabezados de cada columna,
  este complementa las funciones de lectura anteriores, sin embargo,
  la lista retornada se le debe restar 1 al indice del nombre de la 
  columna a querer conseguir
  --------
  parámetros:
  nombre: dirección del archivo a conseguir el encabezado
  --------
  nota: poco completo, pienso seguir trabajando en esta función para utilizarla con
  las funciones de lectura anterior de manera conjunta
  --------
  retorna: lista de la primera linea de un archivo
  """
  with open(nombre,"r") as archivo:
    content = archivo.readline()
    for palabra in content:
      info = ""
      for palabra in content:
        info += palabra
      info = info.split()

    archivo.close()
    return info

def promedio(list):
  """
  Calcula el promedio de una lista de números
  -------
  Parámetros:
  lista: lista de números a promediar
  -------
  Retorna: promedio de la lista
  """
  largo = len(list)
  sumatoria = 0
  for elemento in list:
    sumatoria += elemento

  return sumatoria / largo

def media_aritmetica(lista):
  """
  Código para calcular el promedio de una lista de números
  ----------
  parámetros:
    lista: lista de números
    mitad_list: mitad de la lista
    mediana: numerador de la fracción de la mediana
  ----------
  retorna: mediana de la lista
  """
  mitad_list = len(lista)//2
  lista.sort()
  if len(lista)%2 == 0:
    mediana = lista[mitad_list] + lista[mitad_list-1]
    return mediana/2
  else:
    mediana = lista[mitad_list]
  return mediana

def MAD(lista):
  """
  Función que calcula la Desviación Absoluta Media de una
  lista de datos.
  ----------
  Parámetros:
  lista: lista de numeros a calcular MAD
  ----------
  Retorna: MAD de una lista de datos como valor
  """
  lista.sort()
  mediana = media_aritmetica(lista)
  sum = 0
  for elem in lista:
    sum += abs(elem - mediana)
  return sum/len(lista)

def moda(lista):
  """
  Función que calcula la moda de una lista de datos.
  --------
  Parámetros:
  lista: lista de datos a calcular la moda de
  -------
  Retorna: Valor más comun de la lista como elemento de diccionario
  """
  dic = {}
  for elemento in lista:
    if elemento in dic:
      dic[elemento] += 1
    else:
      dic[elemento] = 1
  return max(dic, key=dic.get), max(dic.values())

def modas(lista):
  """
  Función que calcula la moda general de una lista de datos, o sea, 
  la cantidad de cada valor dentro de la lista.
  -------
  Parámetros:
  lista: lista de datos a calcluar las modas
  -------
  Retorna: todos los datos y sus cantidades respectiva en la lista como diccionario
  """
  dic = {}
  for elemento in lista:
    if elemento in dic:
      dic[elemento] += 1
    else:
      dic[elemento] = 1
  return dic

def rango(lista):
  """
  Función que calcula el rango de una lista
  -----
  Parámetros:
  lista: lista a la que calcular el rango de
  -----
  Retorna: el valor del rango
  """
  lista.sort()
  return lista[-1] - lista[0]

def varianza(lista):
  """
  Función que calcula la varianza de una lista de datos
  -------
  Parámetros:
  lista: lista a calcular la varianza de
  -------
  Retorna: valor de la varianza
  """
  lista.sort()
  promedio_lista = promedio(lista)
  suma = 0
  for elemento in lista:
    suma += (elemento - promedio_lista)**2
  return suma / len(lista)

def desviacion_estandar(lista):
  """
  Función que calcula la desviación estándar de una lista
  -------
  Parámetros:
  lista: lista a calcular la desviación estándar de
  -------
  Retorna: valor de la desviación estándar
  """
  return varianza(lista)**0.5

def percentil(vals_in, q):
    import math
    """
    Calcula el percentil q de una lista de datos.

    Parameters
    ----------
    vals_in : list
        Lista de datos numéricos.
    q : float
        Percentil a calcular (0-100).

    Returns
    -------
    float
        Valor del percentil.

    """
    vals = [v for v in vals_in if math.isfinite(v)]
    if not vals:
        return None

    vals.sort()
    pos = (len(vals) - 1) * (q / 100.0)
    base = int(pos)
    resto = pos - base

    if base + 1 < len(vals):
        return vals[base] + resto * (vals[base + 1] - vals[base])
    else:
        return vals[base]

def iqr(vals_in):
    """
    Calcula el rango intercuartil (IQR) de una lista de datos.

    Parameters
    ----------
    vals_in : list
        Lista de datos numéricos.

    Returns
    -------
    float
        Rango intercuartil.

    """
    q75 = percentil(vals_in, 75)
    q25 = percentil(vals_in, 25)
    if q75 is not None and q25 is not None:
        return q75 - q25
    return None

def FYD(lista):
    """
    Función que calcula el ancho de bines de una lista
    ------
    Parámetros:
    lista: lista de la que calcular el ancho de bines
    ------
    Retorna: ancho de bines 
    """
    return 2*iqr(lista)*len(lista)**(-1/3)
    
#de aqui no uso las funciones, debo terminar de documentarlas
def mse(x,y,theta):
  """
  Función que calcula el minimo error cuadrado de(...)
  """
  m,b = theta
  res = [(y_i - (m*x_i+b)**2) for x_i, y_i in zip(x,y)]
  mse = sum(res) / len(x)
  return mse

def lim_de_cuo(x, y, f, v, i, h=0.0001):#limite de cuociente
  w = [v_j + (h if j==i else 0) for j,v_j in enumerate(v)]
  return (f(x,y,w) - f(x,y,v)) / h

def estimate_gradient(x, y, f, v, h = 0.0001):
  return [lim_de_cuo(x, y, f, v, j) for j in range(len(v))]

def paso_en_gradiente(v, gradiente, step_size):
  step = [step_size * g_i for g_i in gradiente]
  return [a + b for a, b in zip(v, step)]

def gradiente_mse(x, y, theta):
  pendiente, intercepto = theta
  y_pred = [pendiente * xv + intercepto for xv in x]

  g1 = 2 / len(x) + sum([(y_p - y_d) * x_d for x_d, y_d, y_p in zip(x, y_pred, y)])
  g2 = 2 / len(x) + sum([(y_p - y_d) for x_d, y_d, y_p in zip(x, y, y_pred)])

  return [g1, g2]

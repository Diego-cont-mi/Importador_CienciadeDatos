# -*- coding: utf-8 -*-
"""Importer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JxL1pIP62AScIkyLl8KsVygUK9pprr9J
"""

def lecturaconfloat(nombre):
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
    
def lecturanofloat(nombre):
  with open(nombre,"r") as archivo:
    array = []
    archivo.readline()
    lin = input("Ingrese la columna que desea leer: ")

    for linea in archivo:
      if linea != "\n" or linea != "nan" or linea != " " or linea != "":
        linea = linea.split()
        array.append(linea[int(lin)])

  archivo.close()
  return array

print(lecturanofloat("/content/bsc_sel.dat"))
def encabezado(nombre):
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
  Args:
    lista: lista de números
  Returns:
    promedio: promedio de la lista
  """
  largo = len(list)
  sumatoria = 0
  for elemento in list:
    sumatoria += elemento

  return sumatoria / largo

def media_aritmetica(lista):
  """
  Código para calcular el promedio de una lista de números

  parámetros:
    lista: lista de números
    mitad_list: mitad de la lista
    mediana: numerador de la fracción de la mediana

  retorna:
    Mediana/2: mediana de la lista
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
  lista.sort()
  mediana = media_aritmetica(lista)
  sum = 0
  for elem in lista:
    sum += abs(elem - mediana)
  return sum/len(lista)

def moda(lista):
  dic = {}
  for elemento in lista:
    if elemento in dic:
      dic[elemento] += 1
    else:
      dic[elemento] = 1
  return max(dic, key=dic.get), max(dic.values())

def modas(lista):
  dic = {}
  for elemento in lista:
    if elemento in dic:
      dic[elemento] += 1
    else:
      dic[elemento] = 1
  return dic

def rango(lista):
  lista.sort()
  return lista[-1] - lista[0]

def varianza(lista):
  lista.sort()
  promedio_lista = promedio(lista)
  suma = 0
  for elemento in lista:
    suma += (elemento - promedio_lista)**2
  return suma / len(lista)

def desviacion_estandar(lista):
  return varianza(lista)**0.5

def media_aritmetica(lista):
  mitad_list = len(lista)//2
  lista.sort()
  if len(lista)%2 == 0:
    mediana = lista[mitad_list] + lista[mitad_list-1]
    return mediana/2
  else:
    mediana = lista[mitad_list]
  return mediana

def percentil(vals_in, q):
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

def mse(x,y,theta): #minimum square error
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

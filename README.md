# 🔍 Búsqueda Inteligente en Grafos – Rumania Map

Este proyecto implementa algoritmos clásicos de búsqueda en inteligencia artificial para encontrar rutas óptimas en un grafo que representa el mapa de Rumania.

---

## 🚀 ¿Qué hace este proyecto?

Simula diversos métodos de búsqueda, tanto informados como no informados, para comparar su eficiencia resolviendo rutas entre ciudades. Se muestran las rutas encontradas, el número de nodos visitados y generados.

---

## 🧠 Algoritmos implementados

- 📘 **Búsqueda en anchura (BFS)** – Explora los nodos más cercanos al inicio.
- 📘 **Búsqueda en profundidad (DFS)** – Explora los nodos más alejados primero.
- 🔎 **Branch and Bound** – Explora caminos con menor costo acumulado.
- 🔭 **Branch and Bound con heurística** – Utiliza estimaciones con la distancia recta al destino para mejorar la eficiencia.

---

## 🗂️ Estructura del proyecto

| Archivo        | Propósito                                                                |
|----------------|--------------------------------------------------------------------------|
| `run.py`       | Define varios problemas sobre el mapa y ejecuta los algoritmos           |
| `search.py`    | Contiene las clases `Problem`, `Node` y los algoritmos de búsqueda       |
| `utils.py`     | Funciones auxiliares, estructuras (`Dict`, `Struct`) y tipos de colas    |

---

## 🧪 ¿Cómo funciona?

```python
ab = GPSProblem('A', 'B', romania)
search.branch_and_bound_with_heuristic_graph_search(ab).path()
```
Esto crea una instancia del problema de búsqueda de una ruta desde A hasta B usando el mapa de Rumania.

```python
search.branch_and_bound_graph_search(ab).path()
```
El algoritmo busca la mejor ruta según su criterio (BFS, DFS, costo, heurística) y devuelve la secuencia de nodos visitados.

A continuación, se mostrarán las funciones que se usarán en el camino de búsqueda:

| Función                                          | Descripción                                                         |
| ------------------------------------------------ | ------------------------------------------------------------------- |
| `graph_search(problem, fringe)`                  | Lógica central de búsqueda, con manejo de nodos cerrados y abiertos |
| `Node.expand()`                                  | Expande el nodo actual generando todos los posibles sucesores       |
| `GPSProblem.h(node)`                             | Devuelve la heurística: distancia recta al objetivo                 |
| `branch_and_bound_with_heuristic_graph_search()` | Implementación del algoritmo A\* usando colas con prioridad         |

Al ejecutar run.py se mostrará la siguiente salida
```python
[<Node A>, <Node S>, <Node F>, <Node B>]
****
[<Node A>, <Node S>, <Node R>, <Node P>, <Node B>]
-------------------------------------------------------
[<Node T>, <Node A>, <Node S>, <Node F>, <Node B>, <Node G>, <Node D>]
...
La cantidad de nodos visitados son: 9
La cantidad de nodos generados son: 14
```

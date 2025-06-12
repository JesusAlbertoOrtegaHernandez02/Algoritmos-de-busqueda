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



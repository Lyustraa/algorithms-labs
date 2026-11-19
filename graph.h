// graph.h - граф варіанта 10 (зважений неорієнтований, 8 вершин, 12 ребер)
#ifndef GRAPH_H
#define GRAPH_H

#define INF 9999999        // ознака відсутності ребра
#define V 8                // кількість вершин

struct Edge { int u, v, w; };

// ребра графа варіанта 10 (вершини нумеруються з 1)
const Edge EDGES[] = {
    {1, 3, 2}, {1, 4, 4}, {1, 6, 8}, {2, 3, 7}, {2, 4, 6}, {2, 6, 3},
    {2, 7, 6}, {3, 8, 4}, {4, 5, 1}, {5, 7, 4}, {6, 8, 3}, {7, 8, 5}};
const int E_COUNT = sizeof(EDGES) / sizeof(EDGES[0]);

// матриця вагових коефіцієнтів (INF - ребра немає)
inline void build_matrix(int g[V][V]) {
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            g[i][j] = INF;
    for (int k = 0; k < E_COUNT; k++) {
        g[EDGES[k].u - 1][EDGES[k].v - 1] = EDGES[k].w;
        g[EDGES[k].v - 1][EDGES[k].u - 1] = EDGES[k].w;   // граф неорієнтований
    }
}

#endif

// Лістинг 5.1. Матриця суміжності та списки суміжності графа варіанта 10
#include <iostream>
#include <iomanip>
#include "graph.h"
using namespace std;

struct Node {                  // вузол списку суміжності
    int vertex, weight;        // сусідня вершина та вага ребра
    Node* next;
};

// InsertInList(L, null, d): додає вузол на початок списку
Node* insert_in_list(Node* head, int vertex, int weight) {
    return new Node{vertex, weight, head};
}

int main() {
    int g[V][V];
    build_matrix(g);

    cout << "Матриця суміжності (0 - ребра немає):" << endl << "    ";
    for (int j = 1; j <= V; j++) cout << setw(4) << j;
    cout << endl;
    for (int i = 0; i < V; i++) {
        cout << setw(3) << i + 1 << " ";
        for (int j = 0; j < V; j++)
            cout << setw(4) << (g[i][j] == INF ? 0 : g[i][j]);
        cout << endl;
    }

    // списки суміжності: сусіди додаються на початок у порядку зростання номерів
    Node* adj[V + 1] = {nullptr};
    for (int v = 1; v <= V; v++)
        for (int u = 1; u <= V; u++)
            if (g[v - 1][u - 1] != INF)
                adj[v] = insert_in_list(adj[v], u, g[v - 1][u - 1]);

    cout << endl << "Списки суміжності, формат вершина(вага):" << endl;
    for (int v = 1; v <= V; v++) {
        cout << v << ": ";
        for (Node* n = adj[v]; n != nullptr; n = n->next)
            cout << n->vertex << "(" << n->weight << ") -> ";
        cout << "NULL" << endl;
    }

    for (int v = 1; v <= V; v++)           // звільнення пам'яті
        while (adj[v] != nullptr) {
            Node* tmp = adj[v];
            adj[v] = adj[v]->next;
            delete tmp;
        }
    return 0;
}

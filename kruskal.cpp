// Лістинг 5.3. Алгоритм Краскала (DSU), граф - з graph.h
#include <iostream>
#include <vector>
#include <algorithm>
#include "graph.h"
using namespace std;
#define edge pair<int, int>

class Graph {
private:
    vector<pair<int, edge>> G;     // граф: (вага, (u, v))
    vector<pair<int, edge>> T;     // MST
    int *parent;                   // система неперетинних множин (DSU)
    int n;                         // кількість вершин
public:
    Graph(int n);
    ~Graph() { delete[] parent; }
    void AddWeightedEdge(int u, int v, int w);
    int find_set(int i);
    void union_set(int u, int v);
    void kruskal();
    void print();
};

Graph::Graph(int n) {
    this->n = n;
    parent = new int[n + 1];       // вершини нумеруються з 1
    for (int i = 0; i <= n; i++)   // спочатку кожна вершина - окрема множина
        parent[i] = i;
}

void Graph::AddWeightedEdge(int u, int v, int w) {
    G.push_back(make_pair(w, edge(u, v)));
}

int Graph::find_set(int i) {
    if (i == parent[i])            // i - представник своєї множини
        return i;
    return find_set(parent[i]);
}

void Graph::union_set(int u, int v) {
    parent[u] = parent[v];
}

void Graph::kruskal() {
    sort(G.begin(), G.end());      // за неспадною вагою (при рівності - за u, v)
    cout << "Відсортований список ребер (u-v=вага):" << endl;
    for (size_t i = 0; i < G.size(); i++)
        cout << G[i].second.first << "-" << G[i].second.second << "="
             << G[i].first << (i % 6 == 5 ? "\n" : " ");

    for (size_t i = 0; i < G.size() && T.size() < (size_t)(n - 1); i++) {
        int u = G[i].second.first, v = G[i].second.second, w = G[i].first;
        int uRep = find_set(u), vRep = find_set(v);
        if (uRep != vRep) {        // цикл не утворюється
            cout << "ребро " << u << "-" << v << "=" << w << ": FIND(" << u
                 << ")=" << uRep << " != FIND(" << v << ")=" << vRep
                 << ", додаємо" << endl;
            T.push_back(G[i]);     // додаємо ребро до дерева
            union_set(uRep, vRep);
        } else {
            cout << "ребро " << u << "-" << v << "=" << w
                 << ": утворює цикл, пропускаємо" << endl;
        }
    }
}

void Graph::print() {
    int total = 0;
    cout << endl << "Edge : Weight" << endl;
    for (size_t i = 0; i < T.size(); i++) {
        cout << T[i].second.first << " - " << T[i].second.second << " : "
             << T[i].first << endl;
        total += T[i].first;
    }
    cout << "Сумарна вага MST: " << total << endl;
}

int main() {
    Graph g(V);
    for (int k = 0; k < E_COUNT; k++)
        g.AddWeightedEdge(EDGES[k].u, EDGES[k].v, EDGES[k].w);
    g.kruskal();
    g.print();
    return 0;
}

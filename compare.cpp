// Лістинг 5.4. Порівняння результатів алгоритмів Пріма та Краскала
#include <iostream>
#include <vector>
#include <set>
#include <tuple>
#include <algorithm>
#include "graph.h"
using namespace std;

int cost(const vector<Edge>& t) {
    int s = 0;
    for (size_t i = 0; i < t.size(); i++) s += t[i].w;
    return s;
}

// Алгоритм Пріма від вершини start (1..V); повертає ребра в порядку додавання
vector<Edge> prim(int start) {
    int g[V][V];
    build_matrix(g);
    bool selected[V] = {false};
    selected[start - 1] = true;
    vector<Edge> t;
    while ((int)t.size() < V - 1) {
        int best = INF, x = 0, y = 0;
        for (int i = 0; i < V; i++)
            if (selected[i])
                for (int j = 0; j < V; j++)
                    if (!selected[j] && g[i][j] < best) {
                        best = g[i][j];
                        x = i;
                        y = j;
                    }
        selected[y] = true;
        t.push_back({x + 1, y + 1, best});
    }
    return t;
}

int find_set(int* parent, int i) {
    return i == parent[i] ? i : find_set(parent, parent[i]);
}

// Алгоритм Краскала; повертає ребра в порядку додавання
vector<Edge> kruskal() {
    vector<Edge> e(EDGES, EDGES + E_COUNT), t;
    sort(e.begin(), e.end(), [](const Edge& a, const Edge& b) {
        return make_tuple(a.w, a.u, a.v) < make_tuple(b.w, b.u, b.v);
    });
    int parent[V + 1];
    for (int i = 0; i <= V; i++) parent[i] = i;
    for (size_t k = 0; k < e.size() && (int)t.size() < V - 1; k++) {
        int ru = find_set(parent, e[k].u), rv = find_set(parent, e[k].v);
        if (ru != rv) { parent[ru] = rv; t.push_back(e[k]); }
    }
    return t;
}

// ребра без урахування порядку та напрямку
set<tuple<int, int, int>> norm(const vector<Edge>& t) {
    set<tuple<int, int, int>> s;
    for (size_t i = 0; i < t.size(); i++)
        s.insert(make_tuple(min(t[i].u, t[i].v), max(t[i].u, t[i].v), t[i].w));
    return s;
}

void show(const char* name, const vector<Edge>& t) {
    cout << name;
    for (size_t i = 0; i < t.size(); i++) cout << t[i].u << "-" << t[i].v << " ";
    cout << "= " << cost(t) << endl;
}

int main() {
    vector<Edge> tp = prim(1), tk = kruskal();
    show("Прім:    ", tp);
    show("Краскал: ", tk);
    cout << "Однакова вага: " << (cost(tp) == cost(tk) ? "так" : "ні") << endl;
    cout << "Однакова множина ребер: "
         << (norm(tp) == norm(tk) ? "так" : "ні") << endl;
    for (int s = 1; s <= V; s++) {       // Прім з різних початкових вершин
        vector<Edge> t = prim(s);
        cout << "Прім зі старту " << s << ": вага " << cost(t)
             << ", те саме дерево: "
             << (norm(t) == norm(tk) ? "так" : "ні") << endl;
    }
    return 0;
}

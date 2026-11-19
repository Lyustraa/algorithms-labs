// Лістинг 5.2. Алгоритм Пріма (матриця суміжності), граф - з graph.h
#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include "graph.h"
using namespace std;

int main() {
    int G[V][V];
    build_matrix(G);

    int no_edge = 0;               // кількість ребер у MST
    int selected[V];               // true - вершина вже входить до MST
    memset(selected, false, sizeof(selected));
    selected[0] = true;            // починаємо з вершини 1
    int total = 0;                 // вартість MST
    int ex[V], ey[V], ew[V];       // ребра MST у порядку додавання

    cout << left;
    cout << "Крок  V_T                   e*" << endl;
    cout << "0     {1}" << endl;
    while (no_edge < V - 1) {      // MST має містити V - 1 ребро
        int min = INF, x = 0, y = 0;
        for (int i = 0; i < V; i++) {
            if (selected[i]) {
                for (int j = 0; j < V; j++) {
                    // j не в MST і ребро існує; при рівності ваг береться перше
                    if (!selected[j] && G[i][j] < min) {
                        min = G[i][j];
                        x = i;
                        y = j;
                    }
                }
            }
        }
        selected[y] = true;
        ex[no_edge] = x + 1; ey[no_edge] = y + 1; ew[no_edge] = min;
        total += min;
        no_edge++;

        string vt = "{";
        for (int k = 0; k < V; k++)
            if (selected[k]) vt += (vt.size() > 1 ? "," : "") + to_string(k + 1);
        vt += "}";
        cout << setw(6) << no_edge << setw(22) << vt
             << "(" << x + 1 << "," << y + 1 << ")=" << min << endl;
    }

    cout << endl << "Edge : Weight" << endl;
    for (int k = 0; k < no_edge; k++)
        cout << ex[k] << " - " << ey[k] << " : " << ew[k] << endl;
    cout << "Сумарна вага MST: " << total << endl;
    return 0;
}

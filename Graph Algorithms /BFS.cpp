#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;
void bfs(const vector<vector<int>>& graph, int start) {
    unordered_set<int> visited;           // Set to keep track of visited vertices
    queue<int> q;                         // Queue for BFS traversal

    q.push(start);                        // Enqueue the starting vertex

    while (!q.empty()) {
        int current_vertex = q.front();   // Dequeue a vertex from the front of the queue
        q.pop();

        if (visited.find(current_vertex) == visited.end()) {
            cout << current_vertex << " ";  // Process the current vertex (you can modify this part)
            visited.insert(current_vertex);

            // Enqueue neighboring vertices that haven't been visited
            for (int neighbor : graph[current_vertex]) {
                if (visited.find(neighbor) == visited.end()) {
                    q.push(neighbor);
                }
            }
        }
    }
}

int main() {
    vector<vector<int>> graph = {
        {1, 3},     // Neighbors of vertex 0
        {0, 2, 3},  // Neighbors of vertex 1
        {1, 4},     // Neighbors of vertex 2
        {0, 1, 5},  // Neighbors of vertex 3
        {2},        // Neighbors of vertex 4
        {3}         // Neighbors of vertex 5
    };

    int start_vertex = 0;  // Starting vertex for BFS traversal

    cout << "BFS starting from vertex " << start_vertex << ":\n";
    bfs(graph, start_vertex);

    return 0;
}

#include <iostream>

using namespace std;

int N, M, cnt = 0;
int arr[100][100] = { 0 };
int visited[100] = { 0 };

void DFS(int vertex) {
	cnt++;
	visited[vertex] = 1;

	for (int i = 0; i < N; i++) {
		if (arr[vertex][i] && !visited[i])
			DFS(i);
	}
}

void Input() {
	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		int vertex1, vertex2;

		cin >> vertex1 >> vertex2;
		arr[vertex1 - 1][vertex2 - 1] = 1;
		arr[vertex2 - 1][vertex1 - 1] = 1;
	}
}

int main() {
	Input();
	DFS(0);
	cout << cnt - 1;
}

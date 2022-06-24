#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int N, M, V;
map<int, vector<int>> vertice;
vector<int> travdfs;

void DFS(int vertex) {
	vector<int>::iterator vecit;

	cout << vertex << " ";
	travdfs.push_back(vertex);

	if (vertice.find(vertex) == vertice.end())
		return;

	vector<int> vec = vertice.find(vertex)->second;

	for (vecit = vec.begin(); vecit != vec.end(); vecit++) {
		if (find(travdfs.begin(), travdfs.end(), *vecit) == travdfs.end())
			DFS(*vecit);
	}
}

void BFS(int vertex) {
	vector<int>::iterator vecit;
	vector<int> trav;
	queue<int> q;

	q.push(vertex);
	trav.push_back(vertex);

	while (!q.empty()) {
		cout << q.front() << " ";

		if (vertice.find(q.front()) == vertice.end())
			return;

		vector<int> vec = vertice.find(q.front())->second;
		q.pop();

		for (vecit = vec.begin(); vecit != vec.end(); vecit++) {
			if (find(trav.begin(), trav.end(), *vecit) == trav.end()) {
				trav.push_back(*vecit);
				q.push(*vecit);
			}
		}
	}
}

void SortMap() {
	map<int, vector<int>>::iterator mapit;

	for (mapit = vertice.begin(); mapit != vertice.end(); mapit++)
		sort(mapit->second.begin(), mapit->second.end());
}

void Input() {
	cin >> N >> M >> V;

	for (int i = 0; i < M; i++) {
		int vertex1, vertex2;

		cin >> vertex1 >> vertex2;

		map<int, vector<int>>::iterator it = vertice.find(vertex1);

		if (it != vertice.end())
			it->second.push_back(vertex2);
		else {
			vector<int> v;

			v.push_back(vertex2);
			vertice.insert(make_pair(vertex1, v));
		}

		it = vertice.find(vertex2);
		if (it != vertice.end())
			it->second.push_back(vertex1);
		else {
			vector<int> v;

			v.push_back(vertex1);
			vertice.insert(make_pair(vertex2, v));
		}
	}
}

int main() {
	Input();
	SortMap();
	DFS(V);
	cout << endl;
	BFS(V);
}

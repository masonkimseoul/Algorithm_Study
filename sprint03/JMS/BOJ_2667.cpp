#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int n, cnt = 0, housecnt;
int arr[25][25];
int diri[4] = { -1,1,0,0 }, dirj[4] = { 0,0,-1,1 };
bool visited[25][25] = { false };
vector<int> housecntV;

typedef struct index {
	int i, j;
}Index;

void Input() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		string temp;
		
		cin >> temp;
		for (int j = 0; j < temp.size(); j++)
			arr[i][j] = temp[j] - '0';
	}
}

void DFS(Index index) {
	visited[index.i][index.j] = true;

	for (int i = 0; i < 4; i++) {
		Index sum = { index.i + diri[i], index.j + dirj[i] };

		if (sum.i < 0 || sum.j < 0 || sum.i >= n || sum.j >= n || visited[sum.i][sum.j] || !arr[sum.i][sum.j])
			continue;

		housecnt++;
		DFS(sum);
	}
}

int main() {
	Input();

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j] && arr[i][j]) {
				cnt++;
				housecnt = 1;
				DFS({ i,j });
				housecntV.push_back(housecnt);
			}
		}
	}

	sort(housecntV.begin(), housecntV.end());

	cout << cnt;
	for (auto p : housecntV)
		cout << endl << p;
}

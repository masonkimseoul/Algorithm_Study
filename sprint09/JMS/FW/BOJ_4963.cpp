#include <iostream>
#include <cstring>

using namespace std;

int diri[8] = { -1,-1,-1,0,0,1,1,1 };
int dirj[8] = { -1,0,1,-1,1,-1,0,1 };
int arr[50][50];
bool visited[50][50];
int w, h;

typedef struct Coordinate {
	int i, j;
}Coordinate;

void DFS(Coordinate current) {
	visited[current.i][current.j] = true;

	for (int i = 0;i < 8;i++) {
		Coordinate nextCoordinate = { current.i + diri[i], current.j + dirj[i] };
		
		if (nextCoordinate.i < 0 || nextCoordinate.j < 0 || nextCoordinate.i >= h || nextCoordinate.j >= w || !arr[nextCoordinate.i][nextCoordinate.j] 
			|| visited[nextCoordinate.i][nextCoordinate.j])
			continue;

		DFS(nextCoordinate);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (1) {
		int cnt = 0;

		cin >> w >> h;
		if (w == 0 && h == 0)
			break;

		memset(visited, false, sizeof(visited));

		for (int i = 0;i < h;i++) {
			for (int j = 0;j < w;j++)
				cin >> arr[i][j];
		}

		for (int i = 0;i < h;i++) {
			for (int j = 0;j < w;j++) {
				if (arr[i][j] && !visited[i][j]) {
					cnt++;
					DFS({ i,j });
				}
			}
		}

		cout << cnt << '\n';
	}
}

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
#define ll long long

int n, m;
int map[1001][1001] = { 0, };
int map_short[1001][1001][2];

int main() {
	//iostream과 stdio 버퍼 동기화시켜서 입력 빨리받아오자
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	//==============================================
	//n,m과 map을 받아온다

	cin >> n >> m;
	string one_line;
	for (int i = 1; i <= n; i++) {
		cin >> one_line;
		for (int j = 0; j < m; j++) {
			map[i][j + 1] = one_line[j] - '0';
		}
	}

	//short[n][m][2]을 선언하고 최대값으로 세팅

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			map_short[i][j][0] = 100000000;
			map_short[i][j][1] = 100000000;
		}
	}

	//상하좌우
	int posr[4] = { -1,1,0,0 };
	int posc[4] = { 0,0,-1,1 };

	//큐에 (1,1,0)부터 넣고 BFS
	queue<vector<int>> q;
	vector<int> one(3, 0); //row, col, break
	vector<int> two(3, 0);
	one = { 1,1,0 };
	map_short[1][1][0] = 1;
	q.push(one);
	while (q.size() > 0) {
		one = q.front();
		q.pop();

		//벽을 안깨고 온경로
		if (one[2] == 0) {
			for (int p = 0; p < 4; p++) {
				two[0] = one[0] + posr[p];
				two[1] = one[1] + posc[p];
				if (two[0]<1 || two[0]>n || two[1]<1 || two[1]>m) continue; //map밖인거 건너뜀

				//벽이 없을때
				if (map[two[0]][two[1]] == 0) {
					if (map_short[two[0]][two[1]][0] > map_short[one[0]][one[1]][0] + 1) {
						map_short[two[0]][two[1]][0] = map_short[one[0]][one[1]][0] + 1;
						two[2] = 0;
						q.push(two);
					}
				}
				//벽이 있을때
				else {
					if (map_short[two[0]][two[1]][1] > map_short[one[0]][one[1]][0] + 1) {
						map_short[two[0]][two[1]][1] = map_short[one[0]][one[1]][0] + 1;
						two[2] = 1;
						q.push(two);
					}
				}
			}
		}

		//벽을 깨고 온 경로
		else {
			for (int p = 0; p < 4; p++) {
				two[0] = one[0] + posr[p];
				two[1] = one[1] + posc[p];
				if (two[0]<1 || two[0]>n || two[1]<1 || two[1]>m) continue; //map밖인거 건너뜀
				//벽이 없을때
				if (map[two[0]][two[1]] == 0) {
					if (map_short[two[0]][two[1]][1] > map_short[one[0]][one[1]][1] + 1) {
						map_short[two[0]][two[1]][1] = map_short[one[0]][one[1]][1] + 1;
						two[2] = 1;
						q.push(two);
					}
				}
				//벽이 있을때는 못감
			}
		}
	}

	//short[n][m]의 벽이 있는경우와 없는경우중 최단거리를 출력하라. 만약 둘다 MAX값이라면 -1출력
	if (map_short[n][m][0] == 100000000 && map_short[n][m][1] == 100000000) {
		cout << -1;
	}
	else if (map_short[n][m][0] < map_short[n][m][1]) {
		cout << map_short[n][m][0];
	}
	else {
		cout << map_short[n][m][1];
	}

	return 0;
}

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

char arr[20][20];
int mincnt = 1000;
int N, M;
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };
bool isVisited1[20][20] = { false };
bool isVisited2[20][20] = { false };
vector<pair<int,int>> coin;

bool IsFall(int n, int m) {
	if (n < 0 || m < 0 || n >= N || m >= M) return true;
	return false;
}

void Solution(int n1, int m1, int n2, int m2, int cnt) {
	if ((IsFall(n1, m1) && !IsFall(n2, m2)) || (IsFall(n2, m2) && !IsFall(n1, m1))) {
		mincnt = min(mincnt, cnt);
		return;
	}
	if ((IsFall(n1, m1) && IsFall(n2, m2)) || cnt > 10) return;

	for (int j = 0; j < 4; j++) {
		int nextn1 = n1 + diri[j], nextm1 = m1 + dirj[j];
		int nextn2 = n2 + diri[j], nextm2 = m2 + dirj[j];

		if (!IsFall(nextn1, nextm1) && arr[nextn1][nextm1] == '#') { nextn1 = n1; nextm1 = m1; }
		if (!IsFall(nextn2, nextm2) && arr[nextn2][nextm2] == '#') { nextn2 = n1; nextm2 = m1; }

		if (!IsFall(nextn1, nextm1) && isVisited1[nextn1][nextm1] && !IsFall(nextn2, nextm2) && isVisited2[nextn2][nextm2])
			continue;

		if (!IsFall(nextn1, nextm1)) isVisited1[nextn1][nextm1] = true;
		if (!IsFall(nextn2, nextm2)) isVisited2[nextn2][nextm2] = true;
		Solution(nextn1, nextm1, nextn2, nextm2, cnt + 1);
		if (!IsFall(nextn1, nextm1)) isVisited1[nextn1][nextm1] = false;
		if (!IsFall(nextn2, nextm2)) isVisited2[nextn2][nextm2] = false;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		getchar();
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == 'o') coin.push_back(make_pair(i, j));
		}
	}

	isVisited1[coin[0].first][coin[0].second] = true;
	isVisited2[coin[1].first][coin[1].second] = true;
	Solution(coin[0].first, coin[0].second, coin[1].first, coin[1].second, 0);

	if (mincnt > 10) cout << -1;
	else cout << mincnt;
}

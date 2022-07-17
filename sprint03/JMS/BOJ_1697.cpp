#include <iostream>
#include <queue>

using namespace std;

int N, K;
bool visited[100001];

typedef struct info {
	int num, cnt;
}info;

bool IsRange(int a) {
	if (a >= 0 && a <= 100000)
		return true;
	else
		return false;
}

void BFS() {
	queue<info> q;

	q.push({ N,0 });
	visited[N] = true;

	while (!q.empty()) {
		info temp = q.front();
		q.pop();

		if (temp.num == K) {
			cout << temp.cnt;
			return;
		}

		int minustemp = temp.num - 1, multitemp = temp.num * 2, plustemp = temp.num + 1;

		if (IsRange(minustemp) && !visited[minustemp]) {
			visited[minustemp] = true;
			q.push({ minustemp, temp.cnt + 1 });
		}
		if (IsRange(plustemp) && !visited[plustemp]) {
			visited[plustemp] = true;
			q.push({ plustemp, temp.cnt + 1 });
		}
		if (IsRange(multitemp) && !visited[multitemp]) {
			visited[multitemp] = true;
			q.push({ multitemp, temp.cnt + 1 });
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> K;

	BFS();
}

#include <iostream>
#include <map>
#include <cmath>

using namespace std;

typedef struct Cd {
	int y, x;
}Cd;

int arr[2187][2187];
int N;
map<int, int> ans;

void Soultion(Cd cd, int size) {
	if (size == 1) {
		ans[arr[cd.y][cd.x]]++;
		return;
	}

	int firstValue = arr[cd.y][cd.x], f = 0;
	for (int i = cd.y; i < cd.y + size; i++) {
		for (int j = cd.x; j < cd.x + size; j++) {
			if (arr[i][j] != firstValue) {
				f = 1;
				break;
			}
		}
		if (f) break;
	}

	if (!f) ans[firstValue]++;
	else {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) Soultion({ cd.y + size / 3 * i, cd.x + size / 3 * j }, size / 3);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) cin >> arr[i][j];
	}

	Soultion({ 0,0 }, N);

	cout << ans[-1] << '\n' << ans[0] << '\n' << ans[1];
}

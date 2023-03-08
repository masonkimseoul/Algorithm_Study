#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int d;
string init, ans = "";
long long x, y;
long long i = 0, j = 0;

void RFindInitIdx(long long size, int idx) {
	int current = init[idx] - '0';

	switch (current)
	{
	case 1:
		j += size;
		break;
	case 2:
		break;
	case 3:
		i += size;
		break;
	case 4:
		i += size; j += size;
		break;
	default:
		break;
	}

	if (size == 1) return;

	RFindInitIdx(size / 2, idx + 1);
}

void RSolution(long long size) {
	if (i >= size && j >= size) {
		i -= size; j -= size;
		ans += 4 + '0';
	}
	else if (i >= size) {
		i -= size;
		ans += 3 + '0';
	}
	else if (j >= size) {
		j -= size;
		ans += 1 + '0';
	}
	else ans += 2 + '0';

	if (size == 1) return;

	RSolution(size / 2);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> d >> init;
	cin >> x >> y;

	RFindInitIdx(pow(2, d - 1), 0);

	i += y * -1; j += x;

	if (i < 0 || j < 0 || i >= pow(2, d) || j >= pow(2, d)) cout << -1;
	else {
		RSolution(pow(2, d - 1));
		cout << ans;
	}
}

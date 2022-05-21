#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

set<string> resultset;
set<string>::iterator iter;
vector<char> arr;
char result[15];
int L, S;

void InputArr() {
	for (int i = 0; i < S; i++) {
		char temp;

		cin >> temp;
		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end());
}

void PrintResult() {
	for (iter = resultset.begin(); iter != resultset.end(); iter++) {
		int cnt = 0;

		string temp = *iter;
		for (int i = 0; i < temp.size(); i++) {
			if (temp[i] == 'a' || temp[i] == 'e' || temp[i] == 'i' || temp[i] == 'o' || temp[i] == 'u')
				cnt++;
		}

		if (cnt >= 1 && 2 <= L - cnt)
			cout << temp << endl;
	}
}

void RecurFind(int index, int subcnt) {
	for (int i = index; i < S; i++) {
		result[subcnt] = arr[i];

		if (subcnt == L - 1) {
			resultset.insert(result);
			subcnt--;
		}

		RecurFind(i + 1, subcnt + 1);
	}
}

void FindPassword() {
	for (int i = 0; i <= S - L; i++) {
		result[0] = arr[i];

		RecurFind(i + 1, 1);
	}
}

int main() {
	cin >> L >> S;
	InputArr();
	FindPassword();
	PrintResult();
}

#include <iostream>

using namespace std;

int n;
int inorder[100001], postorder[100001], idx[100001];

void Solution(int inStart, int inEnd, int postStart, int postEnd) {
	if (inStart > inEnd || postStart > postEnd) return;

	int rootIdx = idx[postorder[postEnd]];
	int leftSize = rootIdx - inStart;
	
	cout << inorder[rootIdx] << ' ';

	Solution(inStart, rootIdx - 1, postStart, postStart + leftSize - 1);
	Solution(rootIdx + 1, inEnd, postStart + leftSize, postEnd - 1);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> inorder[i];
		idx[inorder[i]] = i;
	}
	for (int i = 1; i <= n; i++) cin >> postorder[i];

	Solution(1, n, 1, n);
}

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int N, M, evencnt = 0, oddcnt = 0;
int arr[200];
bool visited[200] = { false };

int IsEven(int a) {
    if (a % 2 == 0)
        return 1;
    else
        return 0;
}

void FindModecnt() {
    for (int i = 0; i < M; i++) {
        if (IsEven(arr[i]))
            evencnt++;
        else
            oddcnt++;
    }
}

int FindRecentIndex(int index, int mode) {
    int i=index-1, j=index+1;

    while (1) {
        if (i < 0 && j >= M)
            return -1;

        if (i >= 0 && !visited[i] && IsEven(arr[i]) == mode)
            return i;

        if (j < M && !visited[j] && IsEven(arr[j]) == mode)
            return j;

        i--;
        j++;
    }
}

int FindCnt() {
    int cnt = 0, startmode;

    FindModecnt();

    if (evencnt > oddcnt)
        startmode = 1;
    else if (oddcnt > evencnt)
        startmode = 0;
    else {
        startmode = IsEven(arr[0]);
    }

    for (int i = 0; i < M; i++) {
        visited[i] = true;

        if (startmode) {
            if (IsEven(i) != IsEven(arr[i])) {
                int recentindex = FindRecentIndex(i, IsEven(arr[i]));

                if (recentindex == -1)
                    continue;

                swap(arr[i], arr[recentindex]);
                cnt += abs(recentindex - i);
            }
        }
        else {
            if (IsEven(i) == IsEven(arr[i])) {
                int recentindex = FindRecentIndex(i, !IsEven(arr[i]));

                if (recentindex == -1)
                    continue;

                swap(arr[i], arr[recentindex]);
                cnt += abs(recentindex - i);
            }
        }
    }

    return cnt;
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> M;
        for (int j = 0; j < M; j++)
            cin >> arr[j];

        cout << "#" << i + 1 << " " << FindCnt() << endl;
    }
}

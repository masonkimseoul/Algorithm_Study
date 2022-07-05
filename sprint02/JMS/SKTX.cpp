#include <iostream>
#include <algorithm>

using namespace std;

typedef struct inf {
    int i, j, distance, visited, interval;
}inf;

char arr[50][50];
int n, m, k;
inf info[50][50];
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };

void InitInfo() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            info[i][j].distance = 2501;
            info[i][j].interval = 2501;
            info[i][j].visited = 0;
        }
    }
}

inf RecurFindDis(inf prev) {
    inf temp, sum = { 0,0,2501,2501 }, temp1 = { -1,-1,2501,2501 };

    if (prev.i == n - 1 && prev.j == m - 1)
        return { prev };

    info[prev.i][prev.j].visited = 1;
    info[prev.i][prev.j].distance = prev.distance;

    for (int i = 0; i < 4; i++) {
        int resi = prev.i + diri[i];
        int resj = prev.j + dirj[i];

        if (resi < 0 || resj < 0 || resi >= n || resj >= m || arr[resi][resj] == '#' || info[resi][resj].visited)
            continue;

        temp = { resi,resj,prev.distance + 1, 2501 };
        inf result = RecurFindDis(temp);

        if (sum.distance > result.distance) {
            sum = result;
            temp1 = temp;
        }
    }

    if (temp1.i == -1)
        return temp1;

    info[prev.i][prev.j].visited = 0;

    if (arr[prev.i][prev.j] == '.') {
        info[prev.i][prev.j].interval = sum.distance - info[prev.i][prev.j].distance;

        if (arr[temp1.i][temp1.j] == '.') {
            info[prev.i][prev.j].i = temp1.i;
            info[prev.i][prev.j].j = temp1.j;
        }
        else {
            info[prev.i][prev.j].i = sum.i;
            info[prev.i][prev.j].j = sum.j;
        }
    }
    else if (arr[prev.i][prev.j] == 'F') {
        info[prev.i][prev.j].distance = sum.distance;
        info[prev.i][prev.j].i = sum.i;
        info[prev.i][prev.j].j = sum.j;
    }

    return info[prev.i][prev.j];
}

int Solution() {
    int i = 0, j = 0, cnt = 0, movecnt = 0;

    while (i != n - 1 || j != m - 1) {
        if (info[i][j].interval + movecnt > k) {
            movecnt = 0;
            cnt++;
        }
        else
            movecnt++;

        int nexti, nextj;

        nexti = info[i][j].i;
        nextj = info[i][j].j;
        i = nexti;
        j = nextj;
    }

    return cnt;
}

void Input() {
    cin >> n >> m >> k;
    getchar();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cin >> arr[i][j];
        getchar();
    }
}

void Print() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    Input();
    InitInfo();
    Print();
    RecurFindDis({ 0,0,0,2501 });
    cout << Solution();
}

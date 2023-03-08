#include <iostream>

using namespace std;

int M, N;

void RecurFindEarthWorm(int arr[][50], int column, int row)
{
    if (arr[column][row] != 1)
        return;

    arr[column][row] = -1;

    if(column - 1 >= 0)
        RecurFindEarthWorm(arr, column - 1, row);
    if(row - 1 >= 0)
        RecurFindEarthWorm(arr, column, row - 1);
    if (column + 1 < N)
        RecurFindEarthWorm(arr, column + 1, row);
    if (row + 1 < M)
        RecurFindEarthWorm(arr, column, row + 1);
}

int FindEarthWorm(int arr[][50])
{
    int cnt = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (arr[i][j] == 1)
            {
                RecurFindEarthWorm(arr, i, j);
                cnt++;
            }
        }
    }

    return cnt;
}

int main()
{
    int T, K;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int arr[50][50] = {0};

        cin >> M >> N >> K;
        for (int j = 0; j < K; j++)
        {
            int column, row;

            cin >> row >> column;

            arr[column][row] = 1;
        }

        cout << FindEarthWorm(arr) << endl;
    }
}

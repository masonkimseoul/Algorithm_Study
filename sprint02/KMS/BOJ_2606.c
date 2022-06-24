#define _CRT_SECURE_NO_WARNINGS


#include <stdio.h>
#include <stdlib.h>
int visit[100] = {0};
int cnt = -1;
void dfs(int G[100][100], int v, int vsize) {
	cnt++;
	visit[v] = 1;
	/*
	printf("visit : %d\n", v);
	for (int i = 0; i < vsize; i++) {
		for (int j = 0; j < vsize; j++) {
			printf(" %d", G[i][j]);
		}
		printf("\n");
	}
	*/
	for (int i = 0; i < vsize; i++) {
		if (G[v][i] == 1 && visit[i] == 0) {
			dfs(G, i, vsize);
		}
	}	
}
int main()
{
	int V, E;
	scanf("%d %d", &V, &E);
	int G[100][100] ={0};
	int a, b;
	for (int i = 0; i < E; i++) {
		scanf("%d %d", &a, &b);
		G[a-1][b-1] = 1;
		G[b - 1][a - 1] = 1;
	}
	dfs(G, 0, V);
	printf("%d", cnt);




	return 0;
}
#define _CRT_SECURE_NO_WARNINGS


#include <stdio.h>
#include <stdlib.h>
int visit[100] = {0};
int visit1[100] = { 0 };


void dfs(int G[100][100], int v, int vsize) {
	visit[v] = 1;
	printf(" %d", v+1);
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

typedef struct Queue {
	int arr[100];
	int front;
	int rear;
}Queue;
int dequeue(Queue *q) {
	if (q->front==q->rear) {
		return 0;
	}
	int data;
	data = q->arr[q->front];
	q->front = (q->front +1) % 100;
	return data;
}
void enqueue(Queue *q,int data) {
	if ((q->rear+1) % 100 == q->front) {
		return;
	}
	q->arr[q->rear] = data;
	q->rear = (q->rear + 1) % 100;
}
Queue q;
void bfs(int G[100][100], int v, int vsize) {
	int t;
	//데이터 추가
	enqueue(&q, v);
	visit1[v] = 1;
	while (q.front != q.rear) {
		t = dequeue(&q);
		for (int i = 0; i < vsize; i++) {
			if (G[t][i] = 1 && visit1[i] == 0) {
				visit1[i] = 1;
				enqueue(&q, i);
			}
		}
		printf(" %d", t+1);
	}
}
int main()
{
	int V, E, start;
	scanf("%d %d %d", &V, &E, &start);
	int G[100][100] ={0};
	int a, b;
	for (int i = 0; i < E; i++) {
		scanf("%d %d", &a, &b);
		G[a-1][b-1] = 1;
		G[b - 1][a - 1] = 1;
	}
	dfs(G, start-1, V);
	
	q.front = 0;
	q.rear = 0;
	printf("\n");
	bfs(G, start - 1, V);




	return 0;
}
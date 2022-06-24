#include <string>
#include <vector>

using namespace std;

int arr[200][200]={0};
int visited[200]={0};

void DFS(int n, int vertex){
    visited[vertex] = 1;
    
    for(int i=0;i<n;i++){
        if(arr[vertex][i] && !visited[i])
            DFS(n,i);
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0, i, j;
    
    vector<vector<int>>::iterator comit;
    for(comit = computers.begin(), i=0; comit != computers.end() ; comit++, i++){
        vector<int>::iterator it;
        for(it = (*comit).begin(), j=0; it != (*comit).end(); it++, j++){
            if(*it)
                arr[i][j]=1;
        }
    }
    
    for(int i=0;i<n;i++){
        if(!visited[i]){
            answer++;
            DFS(n,i);
        }
    }
    
    return answer;
}

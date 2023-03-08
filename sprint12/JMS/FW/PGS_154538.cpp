#include <string>
#include <queue>

using namespace std;


int BFS(int x, int y, int n){
    queue<pair<int,int>> q;
    q.push(make_pair(y,0));
    
    while(!q.empty()){
        pair<int,int> current = q.front();
        q.pop();
        
        if(current.first == x) return current.second;
        else if(current.first < x) continue;
        
        q.push(make_pair(current.first - n, current.second + 1));
        if(current.first % 3 == 0) q.push(make_pair(current.first / 3, current.second + 1));
        if(current.first % 2 == 0) q.push(make_pair(current.first / 2, current.second + 1));
    }
    
    return -1;
}

int solution(int x, int y, int n) {
    return BFS(x,y,n);
}

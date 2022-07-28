#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

map<int, vector<int>> adjacentList;
map<int, int> dismap;
vector<int> disV;
bool visited[20000];

void BFS(int index){
    queue<int> q;
    
    q.push(index);
    visited[index] = true;
    
    while(!q.empty()){
        int currentIndex = q.front();
        q.pop();
        
        for(auto p : adjacentList[currentIndex]){
            if(!visited[p]){
                dismap[p] = dismap[currentIndex] + 1;
                disV.push_back(dismap[p]);
                q.push(p);
                visited[p] = true;
            }
        }
    }
}

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    
    for(auto p : edge){
        adjacentList[p[0]].push_back(p[1]);
        adjacentList[p[1]].push_back(p[0]);
    }
    
    dismap[1] = 0;
    BFS(1);
    
    sort(disV.begin(), disV.end());
    
    for(int i = disV.size() - 1; i>=0;i--){
        if(disV[disV.size()-1] == disV[i])
            answer++;
        else
            return answer;
    }
}

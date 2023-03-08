#include <vector>
#include <queue>

using namespace std;

typedef struct coordinate{
    int i,j,dis;
}coordinate;

bool visited[100][100];
int diri[4] = {-1,1,0,0};
int dirj[4] = {0,0,-1,1};

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    queue<coordinate> q;
    
    q.push({0,0,1});
    visited[0][0] = true;
    
    while(!q.empty()){
        coordinate temp = q.front();
        q.pop();
        
        if(temp.i == maps.size()-1 && temp.j == maps[0].size()-1)
            return temp.dis;
        
        for(int i=0;i<4;i++){
            coordinate nextcoordinate = {temp.i + diri[i], temp.j + dirj[i]};
            
            if(nextcoordinate.i < 0 || nextcoordinate.j < 0 || nextcoordinate.i >= maps.size() 
               || nextcoordinate.j >= maps[0].size() || visited[nextcoordinate.i][nextcoordinate.j] 
               || !maps[nextcoordinate.i][nextcoordinate.j])
                continue;
            
            q.push({nextcoordinate.i,nextcoordinate.j,temp.dis+1});
            visited[nextcoordinate.i][nextcoordinate.j] = true;
        }
    }
    
    return -1;
}

#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cstring>

using namespace std;

typedef struct coordinate{
    int i,j,dis;
}coordinate;

int diri[4] = {-1,1,0,0};
int dirj[4] = {0,0,-1,1};
int arr[101][101] = {0};
bool visited[101][101];

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    for(int i=0; i<rectangle.size(); i++){
        int x1 = rectangle[i][0] *2, x2 = rectangle[i][2]*2, y1 = rectangle[i][1]*2, y2 = rectangle[i][3]*2;
        for(int i=x1;i<=x2;i++){
            arr[y1][i] = 1;
            arr[y2][i] = 1;
        }
        for(int i=y1;i<=y2;i++){
            arr[i][x1]=1;
            arr[i][x2]=1;
        }
    }
    for(int i=0; i<rectangle.size(); i++){
        int x1 = rectangle[i][0] *2, x2 = rectangle[i][2]*2, y1 = rectangle[i][1]*2, y2 = rectangle[i][3]*2;
        for(int i =y1+1;i<y2;i++){
            for(int j=x1+1;j<x2;j++)
                arr[i][j]=0;
        }
    }
    
    queue<coordinate> q;
    
    q.push({characterY*2, characterX*2,0});
    visited[characterY*2][characterX*2] = true;
    
    while(!q.empty()){
        coordinate temp = q.front();
        q.pop();
        
        if(temp.i == itemY*2 && temp.j == itemX*2)
            return temp.dis / 2;
        
        for(int i=0;i<4;i++){
            coordinate nextcoordinate = {temp.i + diri[i], temp.j + dirj[i], temp.dis + 1};
            
            if(nextcoordinate.i < 0 || nextcoordinate.j <0 || nextcoordinate.i >= 101 || 
               nextcoordinate.j >= 101 || visited[nextcoordinate.i][nextcoordinate.j] ||
               !arr[nextcoordinate.i][nextcoordinate.j])
                continue;
            
            q.push(nextcoordinate);
            visited[nextcoordinate.i][nextcoordinate.j] = true;
        }
    }
    
    return 0;
}

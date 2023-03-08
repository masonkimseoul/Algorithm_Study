#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> cv;
vector<int> tv;
int discount[4] = {10, 20, 30, 40};
int m;
bool visited[4] = {false};

void FindC(int index){
    if(index == m){
        cv.push_back(tv);
        return;
    }
    
    for(int i=0;i<4;i++){
        tv.push_back(discount[i]);
        FindC(index+1);
        tv.pop_back();
    }
}

vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    vector<int> answer;
    int maxnum = 0, maxsum =0;
    vector<int> usersum;
    float discountemo[7];
    
    m = emoticons.size();
    FindC(0);
    
    for(int i=0;i<cv.size();i++){
        int num =0, sum=0;
        for(int j=0;j<users.size();j++){
            int tempsum=0;
            for(int k=0;k<emoticons.size();k++){
                if(users[j][0] <= cv[i][k])
                    tempsum += emoticons[k] * (1- cv[i][k]*0.01);
            }
            
            if(tempsum >= users[j][1])
                num++;
            else
                sum+=tempsum;
        }
        
        if(num > maxnum){
            maxnum = num;
            maxsum = sum;
        }
        else if(num == maxnum && sum > maxsum)
            maxsum = sum;
            
    }
    
    answer.push_back(maxnum);
    answer.push_back(maxsum);
    
    return answer;
}

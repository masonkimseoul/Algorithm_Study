#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

vector<unordered_set<int>> dp(8);

int GetNRept(int N, int cnt){
    int num = 0;
    for(int i=0;i<cnt;i++)
        num = num * 10 + N;
    
    return num;
}

int solution(int N, int number) {
    if(N==number)
        return 1;
    
    dp[0].insert(N);
    for(int i=1;i<8;i++){
        dp[i].insert(GetNRept(N,i+1));
        for(int j=0;j<i;j++){
            for(int k=0;k<i;k++){
                if(j+k+1 != i) 
                    continue;
                
                for(auto a : dp[j]){
                    for(auto b : dp[k]){
                        dp[i].insert(a+b);
                        dp[i].insert(a-b);
                        dp[i].insert(a*b);
                        if(b!=0)
                            dp[i].insert(a/b);
                    }
                }
            }
        }
        
        if(find(dp[i].begin(), dp[i].end(), number) != dp[i].end())
            return i+1;
    }
    
    return -1;
}

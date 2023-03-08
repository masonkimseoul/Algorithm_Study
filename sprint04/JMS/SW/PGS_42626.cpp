#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> scoville, int K) {
    multiset<int> s;
    int answer = 0;
    
    for(auto p : scoville)
        s.insert(p);
    
    while(1){
        int sum=0;
        
        sum += *s.begin();
        s.erase(s.begin());
        
        if(sum >= K)
            return answer;
        
        if(s.size() == 0)
            return -1;
        
        sum = sum + *s.begin() * 2;
        answer++;
        s.erase(s.begin());
        s.insert(sum);
    }
}

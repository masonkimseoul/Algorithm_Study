#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max1=0, max2=0;

    for(auto p : sizes){
        max1 = max(max1, min(p[0],p[1]));
        max2 = max(max2, max(p[0],p[1]));
    }
    
    return max1*max2;
}

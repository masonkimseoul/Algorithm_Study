#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef pair<string, int> si;

unordered_map<string, vector<ii>> albom;
unordered_map<string, int> genrecount;
unordered_map<int, int> playid;



vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    for(int i=0;i<genres.size();i++){
        albom[genres[i]].push_back(make_pair(i, plays[i]));
        genrecount[genres[i]] += plays[i];
    }
    
    vector<si> v1(genrecount.begin(), genrecount.end());
    sort(v1.begin(), v1.end(), [](si a, si b) {
		return a.second > b.second;
		});
    
    for(auto p : v1){
        string genre = p.first;
        
        vector<ii> v2(albom[genre].begin(), albom[genre].end());
        sort(v2.begin(), v2.end(), [](ii a, ii b) {
		        return a.second > b.second;
		    });
        
        answer.push_back(v2[0].first);
        if(v2.size() > 1)
            answer.push_back(v2[1].first);
    }
    
    return answer;
}

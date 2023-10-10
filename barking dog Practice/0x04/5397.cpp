//
// Created by 소승수 on 10/10/23.
//

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    while(n--){
        list<char> l;
        string s;
        auto cursor = l.begin();
        cin >> s;
        for(char c : s){
            if(c == '-'){
                if(cursor != l.begin()){
                    cursor--;
                    cursor = l.erase(cursor);
                }
            } else if(c == '<'){
                if(cursor != l.begin()){
                    cursor--;
                }
            } else if(c == '>'){
                if(cursor != l.end()){
                    cursor++;
                }
            } else{
                l.insert(cursor, c);
            }
        }

        for(auto c : l) cout << c;
        cout<<'\n';
    }
    return 0;
}



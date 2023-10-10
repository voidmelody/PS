//
// Created by 소승수 on 10/10/23.
//

#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    list<char> l;
    string input; int m;
    cin >> input;
    for(char i : input){
        l.push_back(i);
    }
    cin >> m;
    auto cursor = l.end();
    for(int i = 0; i < m; i++){
        char cmd; char s;
        cin >> cmd;
        switch(cmd){
            case 'L':
                if(cursor == l.begin()) break;
                cursor--;
                break;
            case 'D':
                if(cursor == l.end()) break;
                cursor++;
                break;
            case 'B':
                if(cursor == l.begin()) break;
                cursor--;
                cursor = l.erase(cursor);
                break;
            case 'P':
                cin >> s;
                l.insert(cursor,s);
                break;
        }
    }

    for(auto i : l){
        cout << i;
    }
}

//
// Created by 소승수 on 2023/09/19.
//
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int array[26] = {};
        string a, b;
        cin >> a >> b;
        for(char c : a){
            array[c-'a']++;
        }
        for(char c : b){
            array[c-'a']--;
        }
        for(int index = 0; index < 26; index++){
            if(array[index] != 0){
                cout << "Impossible" << '\n';
                break;
            }
            if(index == (26 - 1)){
                cout << "Possible" << '\n';
            }
        }
    }
}


//
// Created by 소승수 on 2023/09/13.
//
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> v;
    int input;
    int sum = 0;
    for(int i = 0; i < 7; i++){
        cin >> input;
        if(input % 2 != 0){
            v.push_back(input);
            sum += input;
        }
    }

    if(v.empty()){
        cout << -1;
    }else{
        cout << sum <<'\n';
        cout << *min_element(v.begin(), v.end());
    }

}


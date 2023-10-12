//
// Created by 소승수 on 10/12/23.
//
#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int t;
    cin >> t;
    while(t--){
        // 초기화
        string func;
        vector<int> v; string arr;
        int n;
        cin >> func;
        cin >> n;
        cin >> arr;

        string input;
        for(int i = 0; i < arr.length(); i++){
            if(n == 0){
                break;
            }
            if(arr[i] != '[' && arr[i] != ']' && arr[i] != ',')
                input += arr[i];
            else if(arr[i] == ',' || arr[i] == ']'){
                v.push_back(stoi(input));
                input.clear();
            }
        }

        // 계산
        bool is_reverse = false;
        bool finish = false;
        int l = 0;
        int r = n;
        for(int i = 0; i < func.length(); i++){
            char c = func[i];
            if(c == 'R'){
                is_reverse = !is_reverse;
                continue;
            }else{
                if(!is_reverse) l++;
                else r--;
            }
        }
        if(l <= r){
            cout << "[";
            if(!v.empty()){
                vector<int> tmp(v.begin()+l, v.begin()+r);
                if(is_reverse){
                    reverse(tmp.begin(), tmp.end());
                }
                for(int i = 0; i < tmp.size(); i++){
                    cout << to_string(tmp[i]);
                    if(i != tmp.size() - 1) cout << ",";
                }
            }
            cout <<"]" << '\n';
        }else{
            cout <<"error\n";
        }
    }
}
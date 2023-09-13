#include <bits/stdc++.h>

using namespace std;

int main() {
    for(int i = 0; i < 3; i++){
        int zero= 0; int input = 0;
        for(int j = 0; j < 4; j++){
            cin >> input;
            if(input == 0)
                zero++;
        }
        switch(zero)
        {
            case 0:
                cout << "E\n";
                break;
            case 1:
                cout << "A\n";
                break;
            case 2:
                cout << "B\n";
                break;
            case 3:
                cout << "C\n";
                break;
            case 4:
                cout << "D\n";
                break;
        }
    }
}

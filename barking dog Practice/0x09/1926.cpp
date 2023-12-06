//
// Created by 소승수 on 12/6/23.
//
#include <bits/stdc++.h>
using namespace std;

int board[502][502];
int vis[502][502];
int n, m;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    int max_num = 0;
    int num = 0;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(board[i][j] == 0 || vis[i][j] == 1) continue;
            num++;
            queue<pair<int,int> > q;

            vis[i][j] = 1;
            q.push(make_pair(i,j));

            int width = 0;
            while(!q.empty()) {
                pair<int,int> cur = q.front();
                q.pop();
                width++;

                for(int dir = 0; dir < 4; dir++) {
                    int nx = cur.first + dx[dir];
                    int ny = cur.second + dy[dir];

                    if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if(vis[nx][ny] == 1 || board[nx][ny] != 1) continue;
                    vis[nx][ny] = 1;
                    q.push(make_pair(nx,ny));
                }
            }
            max_num = max(max_num, width);
        }
    }
    cout << num << '\n' << max_num;
}

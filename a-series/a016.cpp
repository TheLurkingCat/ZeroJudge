#include <iostream>
#include <cstring>
using namespace std;
int check(int* chk)
{
    int i;
    for(i=0;i<9*3;i++)
    if(chk[i]!=1)
    return 0;
    return 1;
}
int main()
{
    int x,y,sd[9][9];
    bool chk[9*3],error;
    while ( cin >> sd[0][0] >> sd[1][0] >> sd[2][0]
                 >> sd[3][0] >> sd[4][0] >> sd[5][0]
                 >> sd[6][0] >> sd[7][0] >> sd[8][0] ) {

    for(y=1;y<9;y++)
    for(x=0;x<9;x++)
    cin>>sd[x][y];
    for(y=0,error=false;y<9&&!error;y++)
{
    memset(chk,false,9*3);
    for(x=0;x<9;x++)
{
    error = chk[9*0+sd[x][y]-1] ||
    chk[9*1+sd[y][x]-1] ||
    chk[9*2+sd[x%3+y%3*3][x/3+y/3*3]-1];
    if(error) break;
    chk[9*0+sd[x][y]-1] = true;
    chk[9*1+sd[y][x]-1] = true;
    chk[9*2+sd[x%3+y%3*3][x/3+y/3*3]-1] = true;
}
}
    if(error) cout<<"no"<<endl;
    else cout<<"yes"<<endl;
}
    return 0;
}
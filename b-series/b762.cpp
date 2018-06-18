#include <iostream>
using namespace std;
int main(){
	int a,s[4]={0,0,0,0};
	string b;
cin >>a;
while (a>0){
 cin >>b;
 if (b=="Get_Kill"){
  s[3]++;
  s[0]++;
  if (s[3]<3)   cout<<"You have slain an enemie."<<endl;
  else if (s[3]==3)   cout<<"KILLING SPREE!"<<endl;
  else if (s[3]==4)   cout<<"RAMPAGE~"<<endl;
  else if (s[3]==5)   cout<<"UNSTOPPABLE!"<<endl;
  else if (s[3]==6)   cout<<"DOMINATING!"<<endl;
  else if (s[3]==7)   cout<<"GUALIKE!"<<endl;
  else if (s[3]>=8)   cout<<"LEGENDARY!"<<endl;
}
 else if (b=="Get_Assist")  s[2]++;
 else{
  s[1]++;
  if (s[3]<3)   cout<<"You have been slained."<<endl;
  else   cout<<"SHUTDOWN."<<endl;
  s[3]=0;
 }
 a--;
}
cout<<s[0]<<"/"<<s[1]<<"/"<<s[2];
}



# include <iostream>
using namespace std;
int main()
{
   int i,j;
   for (i = 0 ; i < 10 ; ++i)
   {
      for (j = 0 ; j < 140 ; ++j)
      {
         if (((j - 0) == 0 || ((i == 0 || i == 4) && (j - 0) >= 0 && (j - 0) < 9) || ((j - 0) == 9 && i > 0 && i < 4)) || (((i == 0 || i == 9) && (j - 11) >= 0 && (j - 11) < 9) || (j - 11) == 4) || (((i == (j - 22) || i + (j - 22) == 9) && (j - 22) >= 0 && (j - 22) <= 9 && i < 5) || (((j - 22) == 4 || (j - 22) == 5) && i >= 5)) || ((((j - 33) == 0 || (j - 33) == 9) && i != 9) || (i == 9 && (j - 33) > 0 && (j - 33) < 9)) || (((i == 0 || i == 4 || i == 9) && (j - 44) > 0 && (j - 44) < 9) || ((j - 44) == 0 && i > 0 && i < 4) || ((j - 44) == 9 && i > 4 && i < 9)) || ((i == 4 && (j - 55) >= 0 && (j - 55) <= 9) || (j - 55) == 0 || (j - 55) == 9)) cout<<"#"; 
         else cout<<' ';
      }
      cout<<endl;
   }
   return 0;
}
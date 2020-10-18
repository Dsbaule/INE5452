#include <iostream>
using namespace std;

bool tryPath(int gameMap[5][5], int row, int column, bool tried[5][5]){
  if (gameMap[row][column] == 1)
    return false;
  if ((row == 4) && (column == 4))
    return true;

  tried[row][column] = true;
  bool found = false;


  if ((row < 4) && (!tried[row + 1][column]) && (gameMap[row + 1][column] == 0))
      found |= tryPath(gameMap, row + 1, column, tried);
  if ((!found) && (column < 4) && (!tried[row][column + 1]) && (gameMap[row][column + 1] == 0))
      found |= tryPath(gameMap, row, column + 1, tried);
  if ((!found) && (row >= 1) && (!tried[row - 1][column]) && (gameMap[row - 1][column] == 0))
      found |= tryPath(gameMap, row - 1, column, tried);
  if ((!found) && (column >= 1) && (!tried[row][column - 1]) && (gameMap[row][column - 1] == 0))
      found |= tryPath(gameMap, row, column - 1, tried);
  
  tried[row][column] = false;
  return found;
}

bool tryPath(int gameMap[5][5]){
  bool tried[5][5];
  for (int j = 0; j < 5; j++)
    for (int k = 0; k < 5; k++)
      tried[j][k] = false;
  return tryPath(gameMap, 0, 0, tried);
}

int n;
int gameMap[5][5];

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n;

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < 5; j++)
      for (int k = 0; k < 5; k++)
        cin >> gameMap[j][k];

    if (tryPath(gameMap))
      cout << "COPS" << endl;
    else
      cout << "ROBBERS" << endl;
  }
  return 0;
}

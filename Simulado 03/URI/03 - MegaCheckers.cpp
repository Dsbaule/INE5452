#include <iostream>
using namespace std;

int maxCapture(int newBoard[20][20], int rows, int columns, int row, int column){
    int maxCaptures = 0, curCaptures = 0;

    if ((row - 2) >= 0) {
        if ((column - 2) >= 0) {
            if((newBoard[row - 1][column - 1] == 2) && (newBoard[row - 2][column - 2] == 0)) {
                newBoard[row][column] = 0;
                newBoard[row - 1][column - 1] = 0;
                newBoard[row - 2][column - 2] = 1;
                curCaptures = maxCapture(newBoard, rows, columns, row - 2, column - 2) + 1;
                if (curCaptures > maxCaptures)
                    maxCaptures = curCaptures;
                newBoard[row][column] = 1;
                newBoard[row - 1][column - 1] = 2;
                newBoard[row - 2][column - 2] = 0;                
            }
        }
        if ((column + 2) < columns) {
            if((newBoard[row - 1][column + 1] == 2) && (newBoard[row - 2][column + 2] == 0)) {
                newBoard[row][column] = 0;
                newBoard[row - 1][column + 1] = 0;
                newBoard[row - 2][column + 2] = 1;
                curCaptures = maxCapture(newBoard, rows, columns, row - 2, column + 2) + 1;
                if (curCaptures > maxCaptures)
                    maxCaptures = curCaptures;
                newBoard[row][column] = 1;
                newBoard[row - 1][column + 1] = 2;
                newBoard[row - 2][column + 2] = 0;
            }
        }
    }
    if ((row + 2) < rows) {
        if ((column - 2) >= 0) {
            if((newBoard[row + 1][column - 1] == 2) && (newBoard[row + 2][column - 2] == 0)) {
                newBoard[row][column] = 0;
                newBoard[row + 1][column - 1] = 0;      
                newBoard[row + 2][column - 2] = 1;
                curCaptures = maxCapture(newBoard, rows, columns, row + 2, column - 2) + 1;
                if (curCaptures > maxCaptures)
                    maxCaptures = curCaptures;
                newBoard[row][column] = 1;
                newBoard[row + 1][column - 1] = 2;      
                newBoard[row + 2][column - 2] = 0;                
            }
        }
        if ((column + 2) < columns) {
            if((newBoard[row + 1][column + 1] == 2) && (newBoard[row + 2][column + 2] == 0)) {
                newBoard[row][column] = 0;
                newBoard[row + 1][column + 1] = 0;
                newBoard[row + 2][column + 2] = 1;
                curCaptures = maxCapture(newBoard, rows, columns, row + 2, column + 2) + 1;
                if (curCaptures > maxCaptures)
                    maxCaptures = curCaptures;
                newBoard[row][column] = 1;
                newBoard[row + 1][column + 1] = 2;
                newBoard[row + 2][column + 2] = 0;
            }
        }        
    }
    return maxCaptures;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    int board[20][20];

    while (cin >> n >> m && (n | m))
    {
        for(int i = 0; i < n; i += 1)
            for(int j = i % 2; j < m; j += 2) {
                cin >> board[i][j];
            }
        int maxCaptures = 0, curCapture;
        
        for(int i = 0; i < n; i += 1)
            for(int j = i % 2; j < m; j += 2)
                if(board[i][j] == 1) {
                    curCapture = maxCapture(board, n, m, i, j);
                    if(curCapture > maxCaptures)
                        maxCaptures = curCapture;
                }
        
        cout << maxCaptures << endl;
    }
    return 0;
}
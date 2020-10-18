#include <iostream>
using namespace std;

long long calc_price(long long n) {
  if (n <= 100)
    return 2 * n;
  if (n <= 10000)
    return 2 * 100 + 3 * (n  - 100);
  if (n <= 1000000)
    return 2 * 100 + 3 * 9900 + 5 * (n - 10000);
  return 2 * 100 + 3 * 9900 + 5 * (1000000 - 10000) + 7 * (n - 1000000);
}

int find_total_consumption(int a) {
  int low = 0, high = a;

  while (low < high) {
    int mid = (low + high)/2;
    if (calc_price(mid) >= a)
      high = mid;
    else
      low = mid + 1;
  }

  return low;
}

int find_consumption_with_diff(int total_consumption, int diff) {
    int low = 1;
    int high = total_consumption - 1;

    while (low < high) {
        int mid = (low + high + 1)/2;
        if (calc_price(total_consumption - mid) - calc_price(mid) >= diff)
            low = mid;
        else
            high = mid - 1;
    }

    return low;
}

int a, b;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  while (cin >> a >> b && (a | b)) {
    int total_consumption = find_total_consumption(a);
    int result = find_consumption_with_diff(total_consumption, b);
    cout << calc_price(result) << endl;
  }
  return 0;
}

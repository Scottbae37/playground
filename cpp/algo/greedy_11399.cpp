#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  /// Input
  int n;
  vector<int> input(1000);
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> input[i];
  }

  /// Sort
  sort(input.begin(), input.begin() + n);

  /// Sum
  int sum = input[0];
  int prev = input[0];

  for (int i = 1; i < n; ++i) {
    prev = prev + input[i];
    sum += prev;
  }
  cout << sum << endl;
  return 0;
}
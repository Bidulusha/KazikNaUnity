#include <iostream>
#include <string>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    
    int pattern[128] = {0};
    for (char c : b) {
        pattern[c]++;
    }
    
    for (size_t i = 0; i < a.length() - b.length() + 1; i++) {
        bool found = true;
        
        int temp[128] = {0};
        for (size_t j = 0; j < b.length(); j++) {
            char c = a[i + j];
            if (++temp[c] > pattern[c]) {
                found = false;
                break;
            }
        }
        
        if (found) {
            cout << i + 1 << endl;
            return 0;
        }
    }
    
    cout << 0 << endl;
    return 0;
}

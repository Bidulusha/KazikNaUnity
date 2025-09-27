#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string a, b;
    cin >> a >> b;
    
    int n = a.size(), m = b.size();
    if (m > n) {
        cout << "0\n";
        return 0;
    }
    
    int pattern[128] = {0};
    for (char c : b) pattern[c]++;
    
    int window[128] = {0};
    int bad_chars = 0;
    
    // Считаем плохие символы в первом окне
    for (int i = 0; i < m; i++) {
        unsigned char c = a[i];
        if (window[c]++ >= pattern[c]) bad_chars++;
    }
    
    if (bad_chars == 0) {
        cout << "1\n";
        return 0;
    }
    
    for (int i = m; i < n; i++) {
        // Удаляем левый символ
        unsigned char left = a[i - m];
        if (window[left]-- > pattern[left]) bad_chars--;
        
        // Добавляем правый символ
        unsigned char right = a[i];
        if (window[right]++ >= pattern[right]) bad_chars++;
        
        if (bad_chars == 0) {
            cout << i - m + 2 << '\n';
            return 0;
        }
    }
    
    cout << "0\n";
    return 0;
}

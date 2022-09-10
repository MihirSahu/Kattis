#include <iostream>
#include <string>

int main() {
    std::string x;
    int temp = 1;
    
    std::cin >> x;

    while (std::stoi(x) > 9) {
        for (int i = 0; i < x.length(); i++) {
            if (x[i] == "0") {
                temp = temp * std::stoi(x[i]);
            }
        }
        x = temp;
        temp = 1;
    }

    std::cout << x << std::endl;
}

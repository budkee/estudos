#include <stdio.h>

int repetidos(int n, int v[]) {

        for (int i = 0; i < n; i++) 
            for (int j = 0; j < n; j++)
                if (v[i] == v[j])
                    return 1;
        return 0;
    };

int main() {

    

}


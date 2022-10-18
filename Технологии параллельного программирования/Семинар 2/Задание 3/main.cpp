#include <omp.h>
#include <iostream>
#include <stdio.h>
#include <locale>
#include <time.h>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");

    std::size_t array_size = 100000000;
    int *a = new int[array_size];
    int *b = new int[array_size];
    int *c = new int[array_size];
    clock_t start_t, end_t, total_t;
    start_t = clock();
    printf("������ ����� ������������� �������� , start_t = %ld\n", start_t);

#pragma omp parallel for
    for (int i = 0; i < 100000000; i++)
    {
        a[i] = i;
        b[i] = i;
    }

    end_t = clock();
    printf("����� ����� ������������� �������� , end_t = %ld\n", end_t);

    total_t = end_t - start_t;
    cout << "����� ����� ������ ���������� �� ������������� �������� " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;

    start_t = clock();
    printf("������ ����� �������� �������� , start_t = %ld\n", start_t);

#pragma omp parallel for
    for (int i = 0; i < 100000000; i++)
        c[1] = a[i] + b[i];
    end_t = clock();
    printf("����� ����� �������� �������� , end_t = %ld\n", end_t);
    total_t = end_t - start_t;
    cout << "����� ����� ������ ���������� �� �������� �������� " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;

    delete[] a;
    delete[] b;
    delete[] c;
    return (0);
}
#include <stdio.h>
#include <locale>

int main()
{
    setlocale(LC_ALL, "Russian");
    printf("���������������� ������� 1\n");
#pragma omp parallel
    {
        printf("������������ �������\n");
    }
    printf("���������������� ������� 2\n");
}
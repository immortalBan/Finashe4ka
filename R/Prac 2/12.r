{
N <- as.integer(readline('������� �� ������ �������� �� ����? '))
M <- as.integer(readline('������� �� �������? '))
res <- (M + N - 1)%/%N
print(paste('������� �����', res, '����'))
}
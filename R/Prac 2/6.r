{
N <- as.integer(readline("������� ����������� ����� "))

res <- (N%%100 - N%%10)%/%10
print(paste("�� ����� �������� � ��������� ����� ����� �����: ", res))
}
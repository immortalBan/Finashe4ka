{
N <- as.integer(readline('������� ����� (������� ����� ������ � ������ �����)'))
hours <- N%/%60%%24
minutes <- N%%60
print(paste0('�� ����� ', hours, ' ����� ', minutes, ' �����'))
}

{
N <- as.integer(readline('Введите число (сколько минут прошло с начала суток)'))
hours <- N%/%60%%24
minutes <- N%%60
print(paste0('На часах ', hours, ' часов ', minutes, ' минут'))
}

{
N <- as.integer(readline('¬ведите количество школьников: '))
K <- as.integer(readline('¬ведите количество €блок: '))

res <- K%%N
print(paste('¬ корзинке осталось ', res, '€блок'))
}
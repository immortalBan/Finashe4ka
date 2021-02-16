{
N <- as.integer(readline('Сколько км турист проходит за день? '))
M <- as.integer(readline('Сколько км маршрут? '))
res <- (M + N - 1)%/%N
print(paste('Туристу нужен', res, 'день'))
}
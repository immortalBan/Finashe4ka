{
N <- as.integer(readline("Введите трехзначное число "))
third_digit <- N%%10
second_digit <- (N%%100 - third_digit)%/%10
first_digit <- (N%%1000 - second_digit - third_digit)%/%100
res <- third_digit + second_digit + first_digit
print(paste("Сумма цифр в ввденном числе: ", res))
}
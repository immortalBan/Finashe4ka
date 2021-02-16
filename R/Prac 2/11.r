{
n <- as.integer(readline('¬ведите четырехзначное число '))
temp1 <- (10*(n%/%1000) + (n%/%100)%%10)
temp2 <- (10*(n%%10) + (n%%100)%/%10)
res <- 1+temp1-temp2
print(res)
} 
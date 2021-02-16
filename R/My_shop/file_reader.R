#install.packages('rJava')
#install.packages('xlsx')

library("xlsx")

setwd('C:/Users/ivanb/Desktop/R/Final_test/My_shop/Analysis')
getwd()
dir()
products <- c("Сыр", "Молоко", "Хлеб", "Шоколад")
tovar_prices = c(400, 120, 70, 100)
supply_prices = c(150, 30, 25, 50)
util_prices = c(70, 15, 15, 10)

for (product in products){
  
  product_index = which(products == product)
  tovar_price = tovar_prices[product_index]
  supply_price = supply_prices[product_index]
  util_price = util_prices[product_index]


  magas <- c()
  rev <- c()
  profit <- c()
  sale <- c()
  spis <- c()
  ravnom <- c()
  max_sale <- c()
  max_sale_index <- c()
  min_sale <- c()
  min_sale_index <- c()
  spis_max <- c()
  
  for (i in 1:10){
    in_data <- read.table(file = paste0("store",as.character(i),"_in.txt"), head=TRUE)
    out_data <- read.table(file = paste0("store",as.character(i),"_out.txt"), head=TRUE)
    magas <- append(magas, paste0('Магазин ', as.character(i)))
    rev <- append(rev, tovar_price * sum(out_data[,product]))
    profit <- append(profit, tovar_price * sum(out_data[,product]) - supply_price * sum(in_data[,product])) - util_price * (sum(in_data[,product]) - sum(out_data[,product]))
    sale <- append(sale, sum(out_data[,product]))
    spis <- append(spis, sum(in_data[,product]) - sum(out_data[,product]))
    ravnom <- append(ravnom, sd(out_data[,product]))
    max_sale <- append(max_sale, max(out_data[,product]))
    max_sale_index <- append(max_sale_index, out_data[which.max(out_data[,product]), 1])
    min_sale <- append(min_sale, min(out_data[,product]))
    min_sale_index <- append(min_sale_index, out_data[which.min(out_data[,product]), 1])
    spis_max <- append(spis_max, max(c(in_data[,product] - out_data[,product])))
  }

  magas <- append(magas, c('Итого','Среднее'))
  rev <- append(rev, c(sum(rev), mean(rev)))
  profit <- append(profit, c(sum(profit), mean(profit)))
  sale <- append(sale, c(sum(sale), mean(sale)))
  spis <- append(spis, c(sum(spis), mean(spis)))
  ravnom <- append(ravnom, c(sum(ravnom), mean(ravnom)))
  max_sale <- append(max_sale, c('',''))
  max_sale_index <- append(max_sale_index, c('',''))
  min_sale <- append(min_sale, c('',''))
  min_sale_index <- append(min_sale_index, c('',''))
  spis_max <- append(spis_max, c('',''))
  
  res_tab <- data.frame('Магазин' = magas, 'Выручка' = rev, 'Прибыль' = profit, 'Реализация' = sale, 'Списание' = spis, 'Равномерность продаж' = ravnom, 'Максимальная продажа' = max_sale, 'День максимальной продажи' = max_sale_index, 'Минимальная продажа' = min_sale, 'День минимальной продажи' = min_sale_index, 'Максимальное списание' = spis_max)
  
  write.xlsx(
    res_tab,
    'C:/Users/ivanb/Desktop/R/Final_test/My_shop/res_tab.xlsx',
    product,
    TRUE,
    FALSE,
    TRUE
  )
  
}

#####График данных по одному из магазинов (Объём продаж)

i <- 1

in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)

png(file=paste0("C:/Users/ivanb/Desktop/R/Final_test/My_shop/Объём продаж магазин ",as.character(i),".png"),width=600, height=350)

xrange = range(seq(1,7))
yrange = range(in1[,"Сыр"], in1[,"Молоко"], in1[,"Хлеб"])

graph <- plot(xrange,
              yrange,
              main=paste0('Объём продаж в магазине ',as.character(i)), 
              xlab="День недели", 
              ylab="Количество проданного товара, шт",
              type = "n",
              ylim=c(1,160)
) 

points(seq(1,7),out1[, "Сыр"], pch=22, col="red3")
lines(seq(1,7),out1[, "Сыр"], pch=22, col="red3")
points(seq(1,7),out1[, "Молоко"], pch=24, col="forestgreen")
lines(seq(1,7),out1[, "Молоко"], pch=24, col="forestgreen")
points(seq(1,7),out1[, "Хлеб"], pch=20, col="steelblue")
lines(seq(1,7),out1[, "Хлеб"], pch=20, col="steelblue")
legend("topright", legend=c("Сыр", "Молоко", "Хлеб"),col=c("red3", "forestgreen", "steelblue"), pch=c(22,24,20))
dev.off()

#####График данных по одному из магазинов (Выручка)

i <- 1

in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)

png(file=paste0("C:/Users/ivanb/Desktop/R/Final_test/My_shop/Выручка ",as.character(i),".png"),width=600, height=350)

xrange = range(seq(1,7))
yrange = range(in1[,"Сыр"], in1[,"Молоко"], in1[,"Хлеб"])

graph <- plot(xrange,
              yrange,
              main=paste0('Выручка с проданного товара в магазине ',as.character(i)), 
              xlab="День недели", 
              ylab="Выручка, тыс. руб",
              type = "n",
              ylim=c(0,max(tovar_prices)*140/1000)
) 

points(seq(1,7),tovar_prices[1] * out1[, "Сыр"] / 1000, pch=22, col="red3")
lines(seq(1,7),tovar_prices[1] * out1[, "Сыр"]/ 1000, pch=22, col="red3")
points(seq(1,7),tovar_prices[2] * out1[, "Молоко"]/ 1000, pch=24, col="forestgreen")
lines(seq(1,7),tovar_prices[2] *out1[, "Молоко"]/ 1000, pch=24, col="forestgreen")
points(seq(1,7),tovar_prices[3] *out1[, "Хлеб"]/ 1000, pch=20, col="steelblue")
lines(seq(1,7),tovar_prices[3] *out1[, "Хлеб"]/ 1000, pch=20, col="steelblue")
legend("topright", legend=c("Сыр", "Молоко", "Хлеб"),col=c("red3", "forestgreen", "steelblue"), pch=c(22,24,20))
dev.off()

#####График данных по одному из магазинов (Прибыль)

i <- 1

in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)

png(file=paste0("C:/Users/ivanb/Desktop/R/Final_test/My_shop/Прибыль ",as.character(i),".png"),width=600, height=350)

xrange = range(seq(1,7))
yrange = range(in1[,"Сыр"], in1[,"Молоко"], in1[,"Хлеб"])

graph <- plot(xrange,
              yrange,
              main=paste0('Прибыль в магазине ',as.character(i)), 
              xlab="День недели", 
              ylab="Прибыль с проданного товара, руб",
              type = "n",
              ylim=c(-max(tovar_prices)*120,max(tovar_prices)*120)
) 

points(seq(1,7),tovar_prices[1] * out1[, "Сыр"] - supply_prices[1] * in1[, "Сыр"] - util_prices[1] * (in1[, "Сыр"] - out1[, "Сыр"]), pch=22, col="red3")
lines(seq(1,7),tovar_prices[1] * out1[, "Сыр"] - supply_prices[1] * in1[, "Сыр"] - util_prices[1] * (in1[, "Сыр"] - out1[, "Сыр"]), pch=22, col="red3")
points(seq(1,7),tovar_prices[2] * out1[, "Молоко"] - supply_prices[2] * in1[, "Молоко"] - util_prices[2] * (in1[, "Молоко"] - out1[, "Молоко"]), pch=24, col="forestgreen")
lines(seq(1,7),tovar_prices[2] * out1[, "Молоко"] - supply_prices[2] * in1[, "Молоко"] - util_prices[2] * (in1[, "Молоко"] - out1[, "Молоко"]), pch=24, col="forestgreen")
points(seq(1,7),tovar_prices[3] * out1[, "Хлеб"] - supply_prices[3] * in1[, "Хлеб"] - util_prices[3] * (in1[, "Хлеб"] - out1[, "Хлеб"]), pch=20, col="steelblue")
lines(seq(1,7),tovar_prices[3] * out1[, "Хлеб"] - supply_prices[3] * in1[, "Хлеб"] - util_prices[3] * (in1[, "Хлеб"] - out1[, "Хлеб"]), pch=20, col="steelblue")
legend("topright", legend=c("Сыр", "Молоко", "Хлеб"),col=c("red3", "forestgreen", "steelblue"), pch=c(22,24,20))
dev.off()

#####График данных по одному из магазинов (Списание)

i <- 1

in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)

png(file=paste0("C:/Users/ivanb/Desktop/R/Final_test/My_shop/Списание ",as.character(i),".png"),width=600, height=350)

xrange = range(seq(1,7))
yrange = range(in1[,"Сыр"], in1[,"Молоко"], in1[,"Хлеб"])

graph <- plot(xrange,
              yrange,
              main=paste0('Списание в магазине ',as.character(i)), 
              xlab="День недели", 
              ylab="Списание непроданного товара, шт",
              type = "n",
              ylim=c(0,150)
) 

points(seq(1,7),in1[, "Сыр"] - out1[, "Сыр"], pch=22, col="red3")
lines(seq(1,7),in1[, "Сыр"] - out1[, "Сыр"], pch=22, col="red3")
points(seq(1,7),in1[, "Молоко"] - out1[, "Молоко"], pch=24, col="forestgreen")
lines(seq(1,7),in1[, "Молоко"] - out1[, "Молоко"], pch=24, col="forestgreen")
points(seq(1,7),in1[, "Хлеб"] - out1[, "Хлеб"], pch=20, col="steelblue")
lines(seq(1,7),in1[, "Хлеб"] - out1[, "Хлеб"], pch=20, col="steelblue")
legend("topright", legend=c("Сыр", "Молоко", "Хлеб"),col=c("red3", "forestgreen", "steelblue"), pch=c(22,24,20))
dev.off()

#####График данных по одному из магазинов (Рентабельность)

i <- 1

in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)

png(file=paste0("C:/Users/ivanb/Desktop/R/Final_test/My_shop/Рентабельность ",as.character(i),".png"),width=600, height=350)

xrange = range(seq(1,7))
yrange = range(in1[,"Сыр"], in1[,"Молоко"], in1[,"Хлеб"])

graph <- plot(xrange,
              yrange,
              main=paste0('Рентабельность в магазине ',as.character(i)), 
              xlab="День недели", 
              ylab="Рентабельность товара, %",
              type = "n",
              ylim=c(-500,100)
) 

points(seq(1,7),(tovar_prices[1] * out1[, "Сыр"] - supply_prices[1] * in1[, "Сыр"] - util_prices[1] * (in1[, "Сыр"] - out1[, "Сыр"])) / (tovar_prices[1] * out1[, "Сыр"]) * 100, pch=22, col="red3")
lines(seq(1,7),(tovar_prices[1] * out1[, "Сыр"] - supply_prices[1] * in1[, "Сыр"] - util_prices[1] * (in1[, "Сыр"] - out1[, "Сыр"])) / (tovar_prices[1] * out1[, "Сыр"]) * 100, pch=22, col="red3")
points(seq(1,7),(tovar_prices[2] * out1[, "Молоко"] - supply_prices[2] * in1[, "Молоко"] - util_prices[2] * (in1[, "Молоко"] - out1[, "Молоко"])) / (tovar_prices[2] * out1[, "Молоко"]) * 100, pch=24, col="forestgreen")
lines(seq(1,7),(tovar_prices[2] * out1[, "Молоко"] - supply_prices[2] * in1[, "Молоко"] - util_prices[2] * (in1[, "Молоко"] - out1[, "Молоко"])) / (tovar_prices[2] * out1[, "Молоко"]) * 100, pch=24, col="forestgreen")
points(seq(1,7),(tovar_prices[3] * out1[, "Хлеб"] - supply_prices[3] * in1[, "Хлеб"] - util_prices[3] * (in1[, "Хлеб"] - out1[, "Хлеб"])) / (tovar_prices[3] * out1[, "Хлеб"]) * 100, pch=20, col="steelblue")
lines(seq(1,7),(tovar_prices[3] * out1[, "Хлеб"] - supply_prices[3] * in1[, "Хлеб"] - util_prices[3] * (in1[, "Хлеб"] - out1[, "Хлеб"])) / (tovar_prices[3] * out1[, "Хлеб"]) * 100, pch=20, col="steelblue")
legend("bottomright", legend=c("Сыр", "Молоко", "Хлеб"),col=c("red3", "forestgreen", "steelblue"), pch=c(22,24,20))
dev.off()

#####Диаграмма данных по одному товару по всем магазинам (Объём продаж)

data <- c()

for (i in 1:10) {
  in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
  out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)
  data <- append(data, c(out1[, "Сыр"]))
}

data_matrix <- matrix(data, nrow = 10, ncol = 7, byrow = TRUE)

colnames(data_matrix) <- c("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

png(file=paste0("C:/Users/ivanb/Desktop/R/Final_test/My_shop/Объём продаж общая таблица.png"),width=1200, height=800)


barplot(data_matrix, beside = FALSE,
        col = topo.colors(10),
        xlab = "День недели", ylab = "Объём продаж, шт",
        main = "Объём продаж по магазинам сети по товару Сыр",
        legend.text = c("Магазин1","Магазин2","Магазин3","Магазин4","Магазин5",
                   "Магазин6","Магазин7","Магазин8","Магазин9","Магазин10"),
        ylim = c(0, 100 * 11),
        las = 1,
        width = 300,
        args.legend = list(x = 'topleft', ncol = 10, text.width = 200, x.intersp = 0.25))

dev.off()

#####График данных по двум товарам по всем магазинам (Объём продаж)

xrange = range(seq(1,7))

graph <- plot(x = xrange,
              main=paste0('Объём продаж в магазинах'), 
              xlab="День недели", 
              ylab="Количество проданного товара, шт",
              type = "n",
              ylim=c(1,160),
              xlim = c(1, 7)
)

colors = topo.colors(20)
for (i in 1:10) {
  in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
  out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)
  data1 <- c(out1[, "Сыр"])
  points(seq(1,7), data1, pch=22, col=colors[i*2])
  lines(seq(1,7), data1, pch=22, col=colors[i*2])
}

for (i in 1:10) {
  in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
  out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)
  data2 <- c(out1[, "Молоко"])
  points(seq(1,7), data2, pch=24, col=colors[i*2])
  lines(seq(1,7), data2, pch=24, col=colors[i*2])
}




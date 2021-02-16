data_generator_in <- function(days_number = 7, min_value = 40, max_value = 120) {
  return (floor(runif(days_number) * (max_value - min_value + 1) + min_value))
}

data_generator_out <- function(input_data, saleLevel = 50, MAX_ITERATION = 500000) {
  n <- 0
  output_data <- c()
  temp_output_data <- c()
  temp_ratio <- 200
  repeat {
    for (i in 1:length(input_data)) {
      output_data[i] <- as.integer(runif(1, 0, input_data[i]))
    }
    ratio = (sum(output_data) / sum(input_data)) * 100
    if ((ratio >= saleLevel * 0.9975) && (ratio <= saleLevel * 1.0025)){
      temp_output_data = output_data
      temp_ratio = ratio
      break
    
    } else if (n == MAX_ITERATION){
      break
    } else if (abs(ratio - saleLevel) <= abs(temp_ratio - saleLevel)) {
      temp_output_data = output_data
      temp_ratio = ratio
      n <- n + 1
    } else {
      n <- n + 1
    }
  
  }
  print(paste(n, ' ', temp_ratio))
  return (temp_output_data)
}

week_days <- c("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

products <- c("Сыр", "Молоко", "Хлеб", "Шоколад")

saleLevels <- floor(runif(10) * 50 + 50)

for (i in 1:10){
  
  in_tab <- data.frame("День недели" = week_days)
  out_tab <- data.frame("День недели" = week_days)
  
  for (product in products) {
  
    dataIn <- data_generator_in(days_number = length(week_days), min_value = 40, max_value = 150)
    dataOut <- data_generator_out(dataIn, saleLevel = saleLevels[i])
  
    in_tab <- data.frame(in_tab, dataIn)
    out_tab <- data.frame(out_tab, dataOut)
  }
  colnames(in_tab) <- c("День недели", products)
  colnames(out_tab) <- c("День недели", products)
  
  write.table(
    in_tab,
    file = paste(
      'C:/Users/ivanb/Desktop/R/Final_test/My_shop/Shop',
      as.character(i),
      '/in.txt',
      sep = ''
      ),
    col.names = TRUE,
    row.names = FALSE,
    sep = ' ',
    dec = ','
  )
  
  write.table(
    out_tab,
    file = paste(
      'C:/Users/ivanb/Desktop/R/Final_test/My_shop/Shop',
      as.character(i),
      '/out.txt',
      sep = ''
    ),
    col.names = TRUE,
    row.names = FALSE,
    sep = ' ',
    dec = ','
  )

}
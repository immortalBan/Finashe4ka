{-

Выполнил Бедак Иван

Задание №2
Построить список коэффициентов ряда Тэйлора для функции ln(x)

-}

--Задание
import Ratio

taylorExp n
  | n < 1 = []
  | otherwise = [(-1)^(m+1) % m | m <- [1 .. n]]

-- Тесты
main = do print "Задание №2"
          print (taylorExp 3)
          print (taylorExp 10)



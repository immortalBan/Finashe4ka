{-

Вариант №1
Выполнил Бедак Иван

Задание 3.
(Задание по варианту)
1) Функция, принимающая на входе список вещественных чисел и вычисляющую их арифметическое среднее. 
Постарайтесь, чтобы функция осуществляла только один проход по списку.
(Задание по выбору)
8) Функция countTrue :: [Bool] -> Integer, возвращающая количество элементов списка, равных True.

-}

--Задание 3
--(Задание по варианту)
task2_1 :: [Double] -> Double
task2_1 s = avg s 0 0
            where avg [] 0 0 = error "Empty arrays are not allowed"
                  avg [] sum num = sum/num
                  avg (x:xs) sum num = avg xs (x+sum) (1.0+num)

--(Задание по выбору)
countTrue :: [Bool] -> Integer
countTrue s = countBool s 0
              where countBool [] num = num
                    countBool (x:xs) count | x == True = countBool xs (1+count)
                                           | otherwise = countBool xs count

--Тесты
main :: IO()
main = do print "t-3"
          print "Var1"
          print (task2_1 [1])
          print (task2_1 [1, 2])
          print (task2_1 [1, 2, 3, 4, 1000])
          print "Var8"
          print (countTrue [])
          print (countTrue [False])
          print (countTrue [False, False, False, True])
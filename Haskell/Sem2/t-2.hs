{-

Вариант №1
Выполнил Бедак Иван

Задание 2. Определите функцию, принимающую на вход целое число n и возвращающую список, 
содержащий n элементов, упорядоченных по возрастанию.
(Задание по варианту)
1) Список натуральных чисел
(Задание по выбору)
6) Список степеней двойки

-}

--Задание 2
--(Задание по варианту)
task1_1 :: Int -> [Int]
task1_1 n | n < 0 = error "Only positive integers are allowed"
          | n == 0 = [] 
          | otherwise = (task1_1 (n-1)) ++ [n]

--(Задание по выбору)
task1_2 :: Int -> [Int]
task1_2 n | n < 0 = error "Only positive integers are allowed"
          | n == 0 = [] 
          | otherwise = (task1_2 (n-1)) ++ [2^n]

--Тесты
main :: IO()
main = do print "t-2"
          print "Var1"
          print (task1_1 0)
          print (task1_1 10)
          print "Var6"
          print (task1_2 0)
          print (task1_2 10)
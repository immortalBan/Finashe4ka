{-

Выполнил Бедак Иван

Задание №37
Выделить из списка положительные элементы, стоящих на нечетных местах

-}

--Задание
evens (x:xs) = x:odds xs
evens _ = []

odds (_:xs) = evens xs
odds _ = []

removeNegative :: [Double] -> [Double]
removeNegative [] = []
removeNegative (x:xs) = if x <= 0 then removeNegative xs else x : removeNegative xs

removePositiveOdd :: [Double] -> [Double]
removePositiveOdd [] = []
removePositiveOdd s = removeNegative (evens s)

--Тесты
main :: IO()
main = do print "Task 37"
          print (removePositiveOdd [-1.0, 2.0, 3.0, 4.0, 5.0])
          print (removePositiveOdd [-1.0, 2.0, -3.0, 4.0, 5.0])
          print (removePositiveOdd [1.0, 2.0, 3.0, 4.0, 5.0])
{-

Выполнил Бедак Иван

Задание №25
Найти в списке два элемента, которые равны сумме соседних

-}

--Задание
findSums :: [Double] -> [Double]
findSums [_, _] = []
findSums (x:xs) = if head xs == x + head (tail xs) then head xs: findSums xs else findSums xs

findTwoSums :: [Double] -> [Double]
findTwoSums [] = []
findTwoSums [a] = [a]
findTwoSums (x:xs) = [x, head xs]

main :: IO()
main = do print "Task 25"
          print (findSums [-1.0, 2.0, 3.0, 4.0, 5.0])
          print (findSums [-1.0, 2.0, 3.0, 1.0, -2.0])
          print (findTwoSums (findSums [-1.0, 2.0, 3.0, 4.0, 5.0]))
          print (findTwoSums (findSums [-1.0, 2.0, 3.0, 1.0, -2.0]))
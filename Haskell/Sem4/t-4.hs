data Product = Book String String | Casette String  | Disk String String Int deriving (Eq,Show)
 
getTitle :: Product -> String
getTitle (Book x _) = x
getTitle (Casette x) = x
getTitle (Disk x _ _) = x
 
getTitles :: [Product] -> [String]
getTitles [] = []
getTitles (x:xs) = (getTitle x) : getTitles xs
 
bookAuthor :: Product -> Maybe String
bookAuthor (Book _ x) =  Just x
bookAuthor (Casette _) = Nothing
bookAuthor (Disk _ _ _) = Nothing
 
bookAuthors :: [Product] -> [String]
bookAuthors [] = []
bookAuthors ((Book _ x):ps)   =  x : bookAuthors ps
bookAuthors ((Casette _):ps)  =  bookAuthors ps
bookAuthors ((Disk _ _ _):ps) =  bookAuthors ps
 
getType :: Product -> String
getType (Book _ _)   = "Book"
getType (Casette _)  = "Casette"
getType (Disk _ _ _) = "Disk"
 
lookupTitle :: String -> [Product] -> Maybe Product
lookupTitle x [] = Nothing
lookupTitle x (p:ps) | (x == (getTitle p)) = Just p
                     | otherwise = lookupTitle x ps
 
lookupTitles :: [String] -> [Product] -> [Maybe Product]
lookupTitles [] _ = []
lookupTitles _ [] = []
lookupTitles (x:xs) p = if xn == Nothing then (lookupTitles xs p) else xn : (lookupTitles xs p) 
                        where xn = (lookupTitle x p)

main :: IO()
main = do print "t-4"
          print (getTitle (Book "Harry Potter" "Joanne Rowling"))
          print (getTitles [(Book "Harry Potter" "Joanne Rowling"),
                            (Casette "Home Alone"),
                            (Disk "High Voltage" "AC/DC" 8)])
          print (bookAuthor (Book "Harry Potter" "Joanne Rowling"))
          print (bookAuthors [(Book "Harry Potter" "Joanne Rowling"),
                            (Casette "Home Alone"),
                            (Disk "High Voltage" "AC/DC" 8),
                            (Book "Beauty and the Beast" "Gabrielle-Suzanne Barbot de Villeneuve")])
          print (getType (Disk "High Voltage" "AC/DC" 8))
          print (lookupTitle "Home Alone" [(Book "Harry Potter" "Joanne Rowling"),
                                        (Casette "Home Alone"),
                                        (Disk "High Voltage" "AC/DC" 8),
                                        (Book "Beauty and the Beast" "Gabrielle-Suzanne Barbot de Villeneuve")])
          print (lookupTitles ["Home Alone", "Harry Potter"] [(Book "Harry Potter" "Joanne Rowling"),
                                                            (Casette "Home Alone"),
                                                            (Disk "High Voltage" "AC/DC" 8),
                                                            (Book "Beauty and the Beast" "Gabrielle-Suzanne Barbot de Villeneuve")])
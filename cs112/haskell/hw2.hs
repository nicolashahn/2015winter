--Nicolas Hahn
--hw2.hs

-- f is function to operate on
-- z is base case
-- x:xs is list
myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl  f z []     =  z
myFoldl  f z (x:xs) =  myFoldl f (f z x) xs


myReverse :: [a] -> [a]
myReverse xs = foldl (\acc x -> x:acc) [] xs


myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f z []      = z
myFoldr f z (x:xs)  = f x (myFoldr f z xs)


--myFoldl2 :: (a -> b -> a) -> a -> [b] -> a
--myFoldl2 f z []     = z
--myFoldl2 f z (x:xs) = f (foldr f z xs) x


isUpper :: Char -> Bool
isUpper x = elem x ['A'..'Z']


onlyCapitals1 :: String -> String
onlyCapitals1 [] = []
onlyCapitals1 xs = filter isUpper xs


onlyCapitals2 :: String -> String
onlyCapitals2 [] = []
onlyCapitals2 xs = [x | x <- xs, isUpper x]


onlyCapitals3 :: String -> String
onlyCapitals3 [] = []
onlyCapitals3 (x:xs) =  if (isUpper x) then (x: onlyCapitals3 xs) else (onlyCapitals3 xs)


divRemainder :: Int -> Int -> (Int, Int)
divRemainder x y = (div x y, mod x y)


digitSum :: Int -> Int
digitSum 0 = 0
digitSum x = if (div x 10) == 0 then mod x 10 else digitSum (div x 10) + mod x 10


sayNum :: Integer -> String
sayNum 0 = "zero "
sayNum 1 = "one "
sayNum 2 = "two "
sayNum 3 = "three "
sayNum 4 = "four "
sayNum 5 = "five "
sayNum 6 = "six "
sayNum 7 = "seven "
sayNum 8 = "eight "
sayNum 9 = "nine "
sayNum 10 = "ten "
sayNum 11 = "eleven "
sayNum 12 = "twelve "
sayNum 13 = "thirteen "
sayNum 14 = "fourteen "
sayNum 15 = "fifteen "
sayNum 16 = "sixteen "
sayNum 17 = "seventeen "
sayNum 18 = "eighteen "
sayNum 19 = "nineteen "
sayNum 20 = "twenty "
sayNum 30 = "thirty "
sayNum 40 = "forty "
sayNum 50 = "fifty "
sayNum 60 = "sixty "
sayNum 70 = "seventy "
sayNum 80 = "eighty "
sayNum 90 = "ninety "
sayNum x 
    | x < 100 = 
        sayNum ((div x 10) * 10) ++ sayNum (mod x 10)
    | x < 1000 = 
        sayNum (div x 100) ++ "hundred " ++ if ((mod x 100) /= 0) 
                                            then sayNum (mod x 100) 
                                            else ""
    | x < 1000000 = 
        sayNum (div x 1000) ++ "thousand " ++ if ((mod x 1000) /= 0) 
                                              then sayNum (mod x 1000) 
                                              else ""
    | x < 1000000000 = 
        sayNum (div x 1000000) ++ "million " ++ if ((mod x 1000000) /= 0) 
                                                then sayNum (mod x 1000000) 
                                                else ""
    | x >= 1000000000 = "not yet supported"

-- there has to be a smarter way to do this...
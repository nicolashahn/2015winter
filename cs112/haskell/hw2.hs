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


myFoldl2 :: (a -> b -> a) -> a -> [b] -> a
myFoldl2 f z xs = foldr step id xs z
    where step x g a = g (f a x)


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


--helper for sayNum
--x: takes the integer, 
--m: a multiple of 1000 that is 1/1000th the "illion", 
--s: the "illion" string of that, 
--and returns the whole number in string form
illion :: Integer -> Integer -> String -> String
illion x m s = sayNum (div x m) ++ s ++ if ((mod x m) /= 0)
                                        then sayNum (mod x m)
                                        else ""

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
-- there has to be a smarter way to do this
    | x < 1000000000000 = 
        illion x 1000000000 "billion "
    | x < 1000000000000000 = 
        illion x 1000000000000 "trillion "
    | x < 1000000000000000000 = 
        illion x 1000000000000000 "quadrillion "
    | x < 1000000000000000000000 = 
        illion x 1000000000000000000 "quintillion "
    | x < 1000000000000000000000000 = 
        illion x 1000000000000000000000 "sextillion "
    | x < 1000000000000000000000000000 = 
        illion x 1000000000000000000000000 "septillion "
    | x < 1000000000000000000000000000000 = 
        illion x 1000000000000000000000000000 "octillion "
    | x < 1000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000 "nonillion "
    | x < 1000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000 "decillion "
    | x < 1000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000 "undecillion "
    | x < 1000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000 "duodecillion "
    | x < 1000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000 "tredecillion "
    | x < 1000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000 "quattuordecillion "
    | x < 1000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000 "quindecillion "
    | x < 1000000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000000 "sexdecillion "
    | x < 1000000000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000000000 "septendecillion "
    | x < 1000000000000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000000000000 "octodecillion "
    | x < 1000000000000000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000000000000000 "novemdecillion "
    | x < 1000000000000000000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000000000000000000 "vigintillion "
    | x < 1000000000000000000000000000000000000000000000000000000000000000000000 = 
        illion x 1000000000000000000000000000000000000000000000000000000000000000000 "centillion "
    | x >= 1000000000000000000000000000000000000000000000000000000000000000000000 = "nah"
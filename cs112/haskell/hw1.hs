-- hw1.hs
-- Nicolas Hahn


citeAuthor :: String -> String -> String
citeAuthor x y = y ++ ", " ++ x


initials :: String -> String -> String
initials x y = head x : "." ++ head y : "."


title :: (String, String, Int) -> String
title (auth,book,date) = book


citeBook :: (String, String, Int) -> String
citeBook (auth,book,date) = book ++ " (" ++ auth ++ ", " ++ (show date :: String) ++ ")"


--list of 3-tuples into a string
bibliography_rec :: [(String, String, Int)] -> String
bibliography_rec [] = ""
bibliography_rec [(auth,book,date)] = citeBook (head [(auth,book,date)])
bibliography_rec (x:xs) = citeBook x ++ "\n" ++ bibliography_rec (xs)


--foldl takes 3 arguments:
	--what to do with the current element
	--starting element
	--list to deal with
--inner function in foldl takes 2:
	--the accumulator (result of all previous foldl's)
	--the current element
bibliography_fold :: [(String, String, Int)] -> String
bibliography_fold [] = ""
bibliography_fold xs = foldl(\acc x -> acc ++ citeBook x ++ "\n") "" xs


--helper function to get third element of 3-tuples
thd :: (c, b, a) -> a
thd (c, b, a) = a

--helper for averageYear
sumYear :: [(String, String, Int)] -> Int
sumYear [] = 0
sumYear (x:xs) = thd x + sumYear xs

averageYear :: [(String, String, Int)] -> Int
averageYear [] = 0
averageYear [(_,_,z)] = z
averageYear xs = div (sumYear xs) (length xs)


--sample argument for references
txt :: String
txt = "[1] and [2] both feature characters who will do whatever it takes to " ++
      "get to their goal, and in the end the thing they want the most ends " ++
      "up destroying them.  In case of [2] this is a whale..."

references :: String -> Int

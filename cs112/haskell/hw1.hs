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

--bibliography_fold :: [(String, String, Int)] -> String
--bibliography_fold [] = ""
--bibliography_fold
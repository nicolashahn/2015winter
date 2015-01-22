--anyPos.hs
--Nicolas Hahn

anyPos :: [Int] -> Bool
anyPos [] = False
anyPos xs = if (filter (>0) xs) == [] then False else True

--anyPos :: [Int] -> Bool
--anyPos [] = False
--anyPos (x:xs) = foldl (\a -> \x -> if x>0 then True else False) 0 xs
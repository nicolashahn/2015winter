--Nicolas Hahn
--hw2.hs


myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl  f z []     =  z
myFoldl  f z (x:xs) =  myFoldl f (f z x) xs
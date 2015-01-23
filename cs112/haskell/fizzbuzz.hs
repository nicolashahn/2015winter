--fizzbuzz.hs
--Nicolas Hahn

fizzBuzz :: Int -> String
fizzBuzz x 
	   | ((mod x 3) == 0) && ((mod x 5) == 0) 	= "fizzbuzz\n"
	   | (mod x 3) == 0							= "fizz\n"
	   | (mod x 5) == 0 						= "buzz\n"
	   | x >= 0 								= show x

fizzBuzzList 


buzz :: Int -> String
buzz x = if mod x 5 == 0 then "buzz\n" else show x

--fizzbuzz :: Int -> String
--fizzbuzz x = 
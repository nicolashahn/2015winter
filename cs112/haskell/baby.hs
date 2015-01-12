doubleMe x = x + x
doubleSmallNumber x = if x > 100
						then x
						else x * 2
removeNonUppercase st = [ c | c <- st , c ‘elem ‘ [’A ’.. ’Z ’]]
let triangles = [(a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]
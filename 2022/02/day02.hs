import Data.List
import Data.List.Split
import System.IO


parseStrings :: [String] -> [(Int, Int)]
parseStrings = map (encode . splitOn " ")
    where 
        encode :: [String] -> (Int, Int)
        encode [x, y] = (parseStringToPoints x, parseStringToPoints y)


parseStringToPoints :: String -> Int
parseStringToPoints x
    | x == "A" || x == "X" = 0
    | x == "B" || x == "Y" = 1
    | x == "C" || x == "Z" = 2


outcome :: Int -> Int -> Int
outcome x y = ((y - x + 1) `mod` 3) * 3


force :: Int -> Int -> Int
force x y = (x + y - 1) `mod` 3 


score :: Int -> Int -> Int
score x y = outcome x y + y + 1


scoreWithForce :: Int -> Int -> Int
scoreWithForce x y = score x (force x y)


solvePartOne :: [String] -> Int
solvePartOne xs = sum $ map (\(x, y) -> score x y) $ parseStrings xs


solvePartTwo :: [String] -> Int
solvePartTwo xs = sum $ map (\(x, y) -> scoreWithForce x y) $ parseStrings xs


main = do
    handle <- readFile "input.txt" 
    let chunks = lines handle 
    
    putStrLn $ show $ solvePartOne chunks
    putStrLn $ show $ solvePartTwo chunks

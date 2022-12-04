import System.IO
import Data.List.Split
import Data.Char(digitToInt)


splitStringIntoIntervals :: String -> [(Int, Int)]
splitStringIntoIntervals s = map (toIntTuple . splitOn "-") $ splitOn "," s
    where
        toIntTuple :: [String] -> (Int, Int)
        toIntTuple [a, b] = (read a :: Int, read b :: Int)


solvePartOne :: [String] -> Int
solvePartOne xs = length $ filter (
        \[(a, b), (x, y)] -> a <= x && b >= y || x <= a && y >= b) intervals
    where 
        intervals = map splitStringIntoIntervals xs 


solvePartTwo :: [String] -> Int
solvePartTwo xs = length $ filter (
        \[(a, b), (x, y)] -> a <= x && x <= b || x <= a && a <= y) intervals
    where 
        intervals = map splitStringIntoIntervals xs 


main :: IO()
main = do
    handle <- readFile "input.txt"
    let chunks = lines handle

    putStrLn $ show $ solvePartOne chunks
    putStrLn $ show $ solvePartTwo chunks

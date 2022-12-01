import Data.List
import System.IO


groupCalories :: [String] -> [[String]]
groupCalories [] = []
groupCalories xs = 
    let head = takeWhile (\s -> s /= "") xs
        tail = drop ((length head) + 1) xs
    in head : groupCalories tail


parseToInts :: [[String]] -> [[Int]]
parseToInts xs = (map (\arr -> map read arr)) xs


findMaximumSublistSum :: [[Int]] -> Int
findMaximumSublistSum xs = maximum $ map (\arr -> sum arr) xs


findSumOfTopKSublists :: [[Int]] -> Int -> Int
findSumOfTopKSublists xs k = 
    sum . take k . reverse . sort $ map (\arr -> sum arr) xs


main :: IO()
main = do
    handle <- readFile "input.txt" 
    let chunks = parseToInts $ groupCalories $ lines handle 
    let solution_1 = findMaximumSublistSum chunks
    let solution_2 = findSumOfTopKSublists chunks 3

    putStrLn $ show $ solution_1
    putStrLn $ show $ solution_2

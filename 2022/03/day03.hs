import Data.List
import Data.List.Split
import System.IO
import Data.Char (isLower, ord)


splitStringInHalf :: String -> (String, String)
splitStringInHalf x = splitAt (length x `div` 2) x


parseStringsInTriples :: [String] -> [(String, String, String)]
parseStringsInTriples [] = []
parseStringsInTriples (x : y : z : xs) = (x, y, z) : parseStringsInTriples xs


findDuplicate :: (String, String) -> Maybe Char
findDuplicate ([], ys) = Nothing
findDuplicate (x:xs, ys) = if x `elem` ys then (Just x) else findDuplicate (xs, ys)


findDuplicateOfTriples :: (String, String, String) -> Maybe Char
findDuplicateOfTriples ([], ys, zs) = Nothing
findDuplicateOfTriples (x:xs, ys, zs) = 
    if x `elem` ys && x `elem` zs then (Just x) else findDuplicateOfTriples (xs, ys, zs)


getValueOfChar :: Maybe Char -> Int
getValueOfChar Nothing = 0
getValueOfChar (Just a)
    | isLower a = ord a - ord 'a' + 1
    | otherwise = ord a  - ord 'A' + 27


solvePartOne :: [String] -> Int
solvePartOne xs = sum $ map getValueOfChar duplicates
    where 
        duplicates = map (findDuplicate . splitStringInHalf) xs


solvePartTwo :: [String] -> Int
solvePartTwo xs = sum $ map getValueOfChar duplicates 
    where
        duplicates = map findDuplicateOfTriples triples
        triples = parseStringsInTriples xs


main :: IO()
main = do
    handle <- readFile "input.txt" 
    let chunks = lines handle

    putStrLn $ show $ solvePartOne chunks 
    putStrLn $ show $ solvePartTwo chunks
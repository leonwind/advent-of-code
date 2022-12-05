import System.IO
import Data.List (transpose, foldl', isPrefixOf)
import Data.List.Split
import Data.Char (isUpper, isSpace, isDigit)
import Control.Lens (element, (&), (.~))


parseStack :: [String] -> [String]
parseStack xs = filter (not . null) $ map (takeWhile isUpper) $ map (dropWhile isSpace) transposed
    where transposed = transpose xs


tokenize :: String -> Maybe [String]
tokenize s 
    | isPrefixOf "move" s = Just (splitOn " " s)
    | otherwise = Nothing


isNumber :: String -> Bool
isNumber s = all (== True) $ map isDigit s


parseMove :: Maybe [String] -> [Int] 
parseMove Nothing = []
parseMove (Just s) = map (\w -> read w :: Int) $ filter isNumber s


parseMoves :: [String] -> [[Int]]
parseMoves xs =  filter (not . null) $ map (parseMove . tokenize) xs


performMoves :: [String] -> [[Int]] -> (String -> String) -> [String]
performMoves stacks moves func = foldl' performMove stacks moves
    where
        performMove stacks [c, f, t] = 
            let from = f - 1
                to = t - 1
                fromStack = stacks !! from
                toStack = stacks !! to
                (movePart, rest) = splitAt c fromStack
            in stacks & (element from .~ rest) & (element to .~ (func movePart <> toStack))


solvePartOne :: [String] -> [[Int]] -> String
solvePartOne stacks moves = map head $ performMoves stacks moves reverse


solvePartTwo :: [String] -> [[Int]] -> String
solvePartTwo stacks moves = map head $ performMoves stacks moves id 


main :: IO() 
main = do
    handle <- readFile "input.txt"
    let chunks = lines handle
    let stacks = parseStack chunks
    let moves = parseMoves chunks

    putStrLn $ show $ solvePartOne stacks moves
    putStrLn $ show $ solvePartTwo stacks moves

import System.IO


allUnique :: String -> Bool
allUnique [] = True
allUnique (s:sx) = not (s `elem` sx) && allUnique sx


findMarkerPos :: String -> Int -> Int
findMarkerPos sx l = if allUnique (take l sx) then l else 1 + findMarkerPos (tail sx) l


solvePartOne :: String -> Int
solvePartOne sx = findMarkerPos sx 4


solvePartTwo :: String -> Int
solvePartTwo sx = findMarkerPos sx 14


main :: IO()
main = do
    handle <- readFile "input.txt"

    putStrLn $ show $ solvePartOne handle
    putStrLn $ show $ solvePartTwo handle

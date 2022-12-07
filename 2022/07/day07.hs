import System.IO
import Control.Arrow ((***))
import Control.Monad (void)
import Data.Char (isAlphaNum, isDigit)
import Data.List (foldl', sort, break)
import Text.ParserCombinators.ReadP (ReadP, char, eof, many, many1, munch1, readP_to_S, satisfy, string, (<++))

{- 
    Solution based on the tutorial about Zippers on FileSystem:
    http://learnyouahaskell.com/zippers
-}

type Name = String
type Size = Int

data FSItem = File Size Name | Folder Name [FSItem] deriving (Show)
data FSCrumb = FSCrumb Name [FSItem] [FSItem] deriving (Show)
type FSZipper = (FSItem, [FSCrumb])


data Command = GoRoot | GoUp | GoDown Name | List [FSItem] deriving (Show)

{- Parser based on ReadP -}
pEndOfLine :: ReadP ()
pEndOfLine = void (char '\n') <++ eof


pName :: ReadP Name
pName = many1 $ satisfy (\c -> isAlphaNum c || c == '.')


pSize :: ReadP Size
pSize = read <$> munch1 isDigit


pGoRoot :: ReadP Command
pGoRoot = GoRoot <$ string "$ cd /" <* pEndOfLine


pGoUp :: ReadP Command
pGoUp = GoUp <$ string "$ cd .." <* pEndOfLine


pGoDown :: ReadP Command
pGoDown = GoDown <$> (string "$ cd " *> pName) <* pEndOfLine


pList :: ReadP Command
pList = List <$ string "$ ls" <* pEndOfLine <*> many (pDir <++ pFile)
  where
    pDir :: ReadP FSItem
    pDir = Folder <$> (string "dir " *> pName) <*> pure [] <* pEndOfLine

    pFile :: ReadP FSItem
    pFile = File <$> pSize <*> (char ' ' *> pName) <* pEndOfLine


parse :: String -> [Command]
parse = fst . head . filter (null . snd) . readP_to_S pCommands
  where
    pCommands :: ReadP [Command]
    pCommands = many1 $ pGoRoot <++ pGoUp <++ pGoDown <++ pList


{- FS traversal -}
fsUp :: FSZipper -> FSZipper
fsUp (item, FSCrumb name ls rs : bs) = (Folder name (ls ++ [item] ++ rs), bs)


fsRoot :: FSZipper -> FSZipper
fsRoot (item, []) = (item, [])
fsRoot x = fsRoot . fsUp $ x


nameOf :: FSItem -> Name
nameOf (File _ name) = name
nameOf (Folder name _) = name


createFS :: FSZipper -> Command -> FSZipper
createFS t GoRoot = fsRoot t
createFS t GoUp = fsUp t
createFS t (GoDown name) = (dir, FSCrumb parent ls rs : bs)
  where
    (Folder parent items, bs) = t
    (ls, dir : rs) = break ((== name) . nameOf) items

createFS t (List items) = (Folder name items, bs)
  where
    (Folder name _, bs) = t


{- Solution -}
recSum :: FSItem -> (Int, Int)
recSum (File size _) = (0, size)
recSum (Folder _ items) = if y <= 100000 then (x + y, y) else (x, y)
    where
        (x, y) = foldr ((\(a, b) -> (+a) *** (+b)) . recSum) (0, 0) items 


solvePartOne :: FSItem -> Int
solvePartOne fs = fst . recSum $ fs


recSumCollector :: FSItem -> ([Int], Int)
recSumCollector (File size _) = ([], size)
recSumCollector (Folder _ items) = (y : xs, y)
  where
    (xs, y) = foldr ((\(a, b) -> (++ a) *** (+ b)) . recSumCollector) ([], 0) items


solvePartTwo :: FSItem -> Int
solvePartTwo fs = 
    let free_space = 70000000 - maximum xs
    in let missing_space = 30000000 - free_space in minimum . filter (>= missing_space) $ xs
    where (xs, _) = recSumCollector fs


main :: IO()
main = do
    content <- readFile "input.txt"
    let fs = fst . fsRoot $ foldl' createFS (Folder "/" [], []) $ parse content 

    putStrLn $ show $ solvePartOne fs
    putStrLn $ show $ solvePartTwo fs
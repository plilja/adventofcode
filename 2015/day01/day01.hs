import Control.Monad

toInt '(' = 1
toInt ')' = -1
toInt _ = 0

solve1 = foldl (+) 0 . map toInt

solve2 xs = length $ takeWhile (>= 0) $ scanl (+) 0 $ map toInt xs

main = do lines <- liftM lines getContents
          mapM_ print (map solve1 lines)
          mapM_ print (map solve2 lines)


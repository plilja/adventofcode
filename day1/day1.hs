import Control.Monad

toInt '(' = 1
toInt ')' = -1
toInt _ = 0

solve = foldl (+) 0 . map toInt

main = do lines <- liftM lines getContents
          mapM_ print (map solve lines)


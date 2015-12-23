import Kattio

toInt '(' = 1
toInt ')' = -1
toInt _ = 0

solve = foldl (+) 0 . map toInt

main = do line <- getLineOp
          case line of
               [] -> return ()
               [x]  -> print (solve x)


import Kattio
import Data.Set
import Control.Monad

type Point = (Int, Int)

direction '^' = (0, 1)
direction '<' = (-1, 0)
direction '>' = (1, 0)
direction 'v' = (0, -1)

solve :: String -> Point -> Set Point -> Int
solve [] _ visited = size visited
solve (z:zs) (x,y) visited = let dx = fst $ direction z
                                 dy = snd $ direction z
                                 nextPoint = (x + dx, y + dy)
                             in solve zs nextPoint (insert nextPoint visited)

main = do lineOp <- getLineOp
          case lineOp of
             [] -> return ()
             [line] -> do print $ solve line (0, 0) (singleton (0, 0))
                          main


import qualified Data.Set as S
import Control.Monad

type Point = (Int, Int)

direction '^' = (0, 1)
direction '<' = (-1, 0)
direction '>' = (1, 0)
direction 'v' = (0, -1)

solve :: String -> Point -> S.Set Point -> Int
solve [] _ visited = S.size visited
solve (z:zs) (x,y) visited = let dx = fst $ direction z
                                 dy = snd $ direction z
                                 nextPoint = (x + dx, y + dy)
                             in solve zs nextPoint (S.insert nextPoint visited)

main = do lines <- liftM lines getContents
          mapM_ print $ map (\l -> solve l (0, 0) (S.singleton (0, 0))) lines


import qualified Data.Set as S
import Control.Monad

type Point = (Int, Int)

direction '^' = (0, 1)
direction '<' = (-1, 0)
direction '>' = (1, 0)
direction 'v' = (0, -1)

solve :: String -> Point -> S.Set Point -> S.Set Point
solve [] _ visited = visited
solve (z:zs) (x,y) visited = let dx = fst $ direction z
                                 dy = snd $ direction z
                                 nextPoint = (x + dx, y + dy)
                             in solve zs nextPoint (S.insert nextPoint visited)

main = do -- Step 1
          line <- getLine
          print $ S.size $ solve line (0, 0) (S.singleton (0, 0))
          -- Step 2
          let santa = map (line !!) [0, 2 .. (length line) - 1]
              robo = map (line !!) [1, 3 .. (length line) - 1]
              santaVisits = solve santa (0, 0) (S.singleton (0, 0))
              step2Visits = solve robo (0, 0) santaVisits
          print $ S.size step2Visits

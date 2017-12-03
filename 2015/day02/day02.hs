import Control.Monad
import Data.List.Split
import Data.List

calcArea [l, w, h] = 2*l*w + 2*w*h + 2*h*l

calcSlack [l, w, h] = minimum [l*w, w*h, h*l]

dim :: String -> [Int]
dim xs = map read $ splitOn "x" xs

step1 :: String -> Int
step1 xs = let asInts = dim xs
           in calcArea asInts + calcSlack asInts

step2 :: String -> Int
step2 xs = let asInts = sort $ dim xs
            in 2 * (asInts !! 0) + 2 * (asInts !! 1) + (product asInts)

main = do lines <- liftM lines getContents
          let res1 = foldl (+) 0 (map step1 lines)
          print res1
          let res2 = foldl (+) 0 (map step2 lines)
          print res2

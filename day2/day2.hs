import Control.Monad
import Data.List.Split

calcArea [l, w, h] = 2*l*w + 2*w*h + 2*h*l

calcSlack [l, w, h] = minimum [l*w, w*h, h*l]

solve :: String -> Int
solve xs = let splitted = splitOn "x" xs
               asInts = map (\x -> read x :: Int) splitted
           in calcArea asInts + calcSlack asInts

main = do lines <- liftM lines getContents
          let res = foldl (+) 0 (map solve lines)
          print res

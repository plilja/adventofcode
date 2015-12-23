module Kattio where 

import Data.Char
import System.IO

getUntil :: (Char -> Bool) -> IO [String]
getUntil predicate = do done <- isEOF
                        case done of
                             True -> return []
                             _ -> do c <- getChar
                                     if predicate c
                                        then return [[]]
                                        else do xss <- getUntil predicate
                                                return [(c:xs) | xs <- xss]


getWord :: IO String
getWord = do r <- getUntil isSpace
             return (r !! 0)


getIntOp :: IO [Int]
getIntOp = do x <- getWord
              if null x 
                 then return []
                 else return [(read x :: Int)]

getInt :: IO Int
getInt = do x <- getIntOp
            return (x !! 0)


getInts :: Int -> IO [Int]
getInts 0 = return []
getInts n = do x <- getInt
               xs <- getInts (n - 1)
               return (x:xs)
               


getLineOp :: IO [String]
getLineOp = getUntil (\ c -> c == '\n')

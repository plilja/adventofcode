import Data.List

hasThreeWovels = (>=3) . length . filter (\c -> c `elem` "aeiou")

pairs s = zip s (tail s)

hasTwoInARow s = 1 <= length [(x,y) | (x, y) <- pairs s, x==y]

doesNotContainUnwantedPattern s = let unwanted_patterns = [('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]
                                      unwanted = filter (\p -> p `elem` unwanted_patterns) (pairs s)
                                  in null unwanted

isNice1 s = hasThreeWovels s && hasTwoInARow s && doesNotContainUnwantedPattern s

containsTwoPairs [] = False
containsTwoPairs (x:[]) = False
containsTwoPairs (x:y:xs) = ((x, y) `elem` (pairs xs)) || containsTwoPairs (y:xs)

repeatsWithOneInBetween [] = False
repeatsWithOneInBetween (x:[]) = False
repeatsWithOneInBetween (x:y:[]) = False
repeatsWithOneInBetween (x:y:xs) | x == (head xs) = True
                                 | otherwise = repeatsWithOneInBetween (y:xs)

isNice2 s = containsTwoPairs s && repeatsWithOneInBetween s

main = do l <- fmap (lines) getContents
          let niceLines1 = filter isNice1 l
          print $ length niceLines1

          let niceLines2 = filter isNice2 l
          print $ length niceLines2

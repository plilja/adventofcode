
hasThreeWovels = (>=3) . length . filter (\c -> c `elem` "aeiou")

pairs s = [[x]++[y] | (x, y) <- zip s (tail s)]

hasTwoInARow s = 1 <= length [(x,y) | [x, y] <- pairs s, x==y]

doesNotContainUnwantedPattern s = let unwanted_patterns = ["ab", "cd", "pq", "xy"]
                                      unwanted = filter (\p -> p `elem` unwanted_patterns) (pairs s)
                                  in null unwanted

isNice s = hasThreeWovels s && hasTwoInARow s && doesNotContainUnwantedPattern s

main = do l <- fmap (lines) getContents
          let niceLines = filter isNice l
          print $ length niceLines

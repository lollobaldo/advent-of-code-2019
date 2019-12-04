module Main where

import Data.Set (Set, empty, insert , member)
import Control.Monad

data Wire = [Direction] deriving (Eq, Show)
data Direction = U | D | L | R deriving (Eq,Show)
data Path = Direction Int deriving (Eq, Show)

main = do
        contents <- liftM parse . readFile $ "input.txt"
        print . execA $ contents
        print . execB $ contents

parse :: [String] -> []
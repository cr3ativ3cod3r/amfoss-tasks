isPrime :: Int -> Bool
isPrime n
  | n <= 1 = False
  | n == 2 = True
  | otherwise = all (\x -> n `mod` x /= 0) [2..intSqrt n]
  where
    intSqrt = floor . sqrt . fromIntegral

primesUpToN :: Int -> [Int]
primesUpToN n = filter isPrime [2..n]

main :: IO ()
main = do
  putStrLn "Enter a number :"
  input <- getLine
  let n = read input :: Int
  let primes = primesUpToN n
  print primes

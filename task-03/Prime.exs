defmodule PrimeArray do
  def get_primes do
    IO.puts("Enter a number:")
    input = IO.gets("") |> String.trim() |> String.to_integer()
    
    case input do
      n when n < 2 ->
        IO.puts("Please enter a valid number greater than or equal to 2.")
        get_primes()
      n ->
        primes = Enum.filter(2..n, &is_prime(&1))
        IO.puts("#{Enum.join(primes, ", ")}")
    end
  end

  defp is_prime(n) when n in [2, 3], do: true
  defp is_prime(n) do
    floored_sqrt = :math.sqrt(n)
      |> Float.floor
      |> round
    !Enum.any?(2..floored_sqrt, &(rem(n, &1) == 0))
  end
end


PrimeArray.get_primes()

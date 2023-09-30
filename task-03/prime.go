package main

import "fmt"

func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scan(&n)

    L := []int{2}

    for i := 3; i <= n; i++ {
        isPrime := true
        for j := 2; j < i; j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        if isPrime {
            L = append(L, i)
        }
    }

    if n>=2 {
        for _, L := range L {
            fmt.Print(L, " ")
        }}
}

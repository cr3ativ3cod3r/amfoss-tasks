use std::io;

fn is_prime(num: u32) -> bool {
    if num == 2 {
        return true;
    }
    let mut i = 2;
    while i * i <= num {
        if num % i == 0 {
            return false;
        }
        i += 1;
    }
    true
}

fn primes_up_to_n(n: u32) -> Vec<u32> {
    (2..=n).filter(|&x| is_prime(x)).collect()
}

fn main() {
    println!("Enter a number:");
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n);
    let n: u32 = n
        .trim()
        .parse()
        .expect("Please enter a valid positive integer");
    

    let primes = primes_up_to_n(n);

    println!("Prime numbers up to {}: {:?}", n, primes);
}

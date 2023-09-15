fn fib(n: u8) -> u64 {
    if n <= 1 {
        return n as u64;
    }

    let mut prev = 0;
    let mut cur = 1;

    for _ in 2..=n {
        let next = prev + cur;
        prev = cur;
        cur = next;
    }

    cur
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let n: u8 = input.trim().parse().unwrap();

    println!("{}", fib(n))
}

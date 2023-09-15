fn fib(n: usize) -> usize {
    let mut a = 1;
    let mut b = 1;
    let mut c = 0;

    for _ in 2..n {
        c = a + b;
        a = b;
        b = c;
    }

    c
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    match n {
        1 => println!("1"),
        2 => println!("1"),
        _ => println!("{}", fib(n)),
    }
}

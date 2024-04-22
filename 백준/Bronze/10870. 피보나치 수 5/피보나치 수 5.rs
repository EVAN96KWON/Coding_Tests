use std::io::stdin;

fn fibonacci(n: i32) -> i32 {
    match n {
        0 => return 0,
        1 => return 1,
        2 => return 1,
        _ => return fibonacci(n - 1) + fibonacci(n - 2),
    };
}

fn main() {
    // get input
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();
    let n = buffer.trim().parse::<i32>().unwrap();
    buffer.clear();

    // print output
    println!("{}", fibonacci(n));
}

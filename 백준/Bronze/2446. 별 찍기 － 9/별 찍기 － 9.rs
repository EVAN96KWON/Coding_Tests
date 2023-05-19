fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();

    for i in 1..=n {
        for _ in 1..i {
            print!(" ");
        }
        for _ in i..=2 * n - i {
            print!("*");
        }
        println!();
    }
    for i in (1..n).rev() {
        for _ in 1..i {
            print!(" ");
        }
        for _ in i..=2 * n - i {
            print!("*");
        }
        println!();
    }
}
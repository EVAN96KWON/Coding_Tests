fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let n = input.trim().parse::<i32>().unwrap();

    for i in 1..n + 1 {
        for _ in 0..i {
            print!("*");
        }
        println!();
    }
}
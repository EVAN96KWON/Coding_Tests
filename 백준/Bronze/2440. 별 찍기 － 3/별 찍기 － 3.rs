fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let number = input.trim().parse::<u8>().unwrap();

    for i in 0..number {
        for _ in 0..(number - i) {
            print!("*");
        }
        println!();
    }
}

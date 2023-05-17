fn main() {
    let mut hex = String::new();
    std::io::stdin().read_line(&mut hex).unwrap();
    let dec = i64::from_str_radix(&hex.trim(), 16).unwrap();
    println!("{}", dec);
}
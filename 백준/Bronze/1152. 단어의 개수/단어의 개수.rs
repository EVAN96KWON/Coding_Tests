fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    let cnt = s.split_whitespace().count();
    println!("{}", cnt);
}
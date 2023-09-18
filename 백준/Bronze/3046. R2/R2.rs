fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let r1: i32 = iter.next().unwrap().parse().unwrap();
    let s: i32 = iter.next().unwrap().parse().unwrap();

    // s = (r1 + r2) / 2
    // so r2 = 2 * s - r1
    println!("{}", 2 * s - r1);
}

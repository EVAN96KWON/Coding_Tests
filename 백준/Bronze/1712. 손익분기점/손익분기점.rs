fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    let v: Vec<&str> = s.split_whitespace().collect();
    let a: i64 = v[0].parse().unwrap();
    let b: i64 = v[1].parse().unwrap();
    let c: i64 = v[2].parse().unwrap();

    let n = if c - b > 0 { a / (c - b) + 1 } else { -1 };
    println!("{}", n);
}
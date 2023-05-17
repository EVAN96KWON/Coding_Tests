fn main() {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    let mut v: Vec<i32> = Vec::new();
    for i in line.trim().split_whitespace() {
        v.push(i.parse().unwrap());
    }
    v.sort();
    for i in v {
        print!("{} ", i);
    }
}
fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut inputs = input.split_whitespace();
    let a: i32 = inputs.next().unwrap().parse().unwrap();
    let b: i32 = inputs.next().unwrap().parse().unwrap();
    let n: i32 = inputs.next().unwrap().parse().unwrap();
    let mut result: i32 = 0;
    let mut remain: i32 = a % b;
    for _ in 0..n {
        remain *= 10;
        result = remain / b;
        remain = remain % b;
    }
    println!("{}", result);
}
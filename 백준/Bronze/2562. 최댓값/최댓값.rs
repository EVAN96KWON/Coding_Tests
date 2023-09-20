fn main() {
    let mut input = String::new();
    for _ in 0..9 {
        std::io::stdin().read_line(&mut input).unwrap();
    }
    let numbers: Vec<i32> =
        Vec::from_iter(input.split_whitespace().map(|x| x.parse::<i32>().unwrap()));

    let max = numbers.iter().max().unwrap();
    let max_idx = numbers.iter().position(|x| x == max).unwrap();
    println!("{}", max);
    println!("{}", max_idx + 1);
}

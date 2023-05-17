fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();

    let map: Vec<String> = (0..n)
        .map(|_| {
            let mut input = String::new();
            std::io::stdin().read_line(&mut input).unwrap();
            input = input.trim().to_string();
            input.chars().rev().collect()
        })
        .collect();

    map.iter().for_each(|x| println!("{}", x));
}
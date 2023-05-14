fn main() {
    let mut test_cases = String::new();
    std::io::stdin().read_line(&mut test_cases).unwrap();
    let test_cases: i32 = test_cases.trim().parse().unwrap();

    for _ in 0..test_cases {
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let input = input.trim();

        let first_char = input.chars().nth(0).unwrap();
        let last_char = input.chars().nth(input.len() - 1).unwrap();

        println!("{}{}", first_char, last_char);
    }
}
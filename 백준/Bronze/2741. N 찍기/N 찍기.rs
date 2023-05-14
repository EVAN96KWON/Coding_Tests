fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let n = input.trim().parse::<i32>().unwrap();

    let mut output = String::new();
    for i in 1..n + 1 {
        output.push_str(&format!("{}\n", i));
    }
    println!("{}", output.trim());
}
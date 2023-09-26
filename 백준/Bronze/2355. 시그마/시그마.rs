fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut vars = input.split_whitespace().map(|x| x.parse::<i64>().unwrap());

    let mut a = vars.next().unwrap();
    let mut b = vars.next().unwrap();

    if a > b {
        std::mem::swap(&mut a, &mut b);
    }

    println!("{}", (b - a + 1) * (a + b) / 2);
}

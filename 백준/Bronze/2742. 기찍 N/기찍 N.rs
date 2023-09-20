use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let number = input.trim().parse::<usize>().unwrap();
    let string = (0..number)
        .rev()
        .map(|i| (i + 1).to_string())
        .collect::<Vec<_>>()
        .join("\n");

    println!("{}", string);
}

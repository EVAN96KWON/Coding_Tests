use std::{io, iter};

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let number = input.trim().parse::<usize>().unwrap();

    let stars: String = (0..number)
        .flat_map(|i| iter::repeat("*").take(number - i).chain(iter::once("\n")))
        .collect();

    println!("{}", stars);
}

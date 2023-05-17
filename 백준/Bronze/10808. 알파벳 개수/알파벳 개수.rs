fn main() {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();

    let mut map = std::collections::HashMap::new();
    for c in line.chars() {
        if c.is_alphabetic() {
            let count = map.entry(c).or_insert(0);
            *count += 1;
        }
    }

    for c in 'a'..='z' {
        let count = map.get(&c).unwrap_or(&0);
        print!("{} ", count);
    }
}
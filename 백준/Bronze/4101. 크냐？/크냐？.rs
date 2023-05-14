fn main() {
    while true {
        // get n and m from stdin
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let n: u32 = iter.next().unwrap().parse().unwrap();
        let m: u32 = iter.next().unwrap().parse().unwrap();

        // break if n and m are both 0
        if n == 0 && m == 0 {
            break;
        }

        if n > m {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
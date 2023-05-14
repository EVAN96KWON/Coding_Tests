fn main() {
    let mut possible = String::new();
    let mut required = String::new();
    std::io::stdin().read_line(&mut possible).unwrap();
    std::io::stdin().read_line(&mut required).unwrap();
    let cnt_possible = possible.matches("a").count();
    let cnt_required = required.matches("a").count();

    if cnt_possible >= cnt_required {
        println!("go");
    } else {
        println!("no");
    }
}
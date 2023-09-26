fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut vars = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse::<f64>().unwrap());

    let d = vars.next().unwrap();
    let ratio_h = vars.next().unwrap();
    let ratio_w = vars.next().unwrap();

    let x = (d.powi(2) / (ratio_h.powi(2) + ratio_w.powi(2))).sqrt();

    println!("{} {}", (x * ratio_h).floor(), (x * ratio_w).floor());
}

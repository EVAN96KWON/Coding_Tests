fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();

    let mut array = vec![false; 3 as usize];
    array[0] = true;

    for _ in 0..n {
        // input int x int y
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.trim().split_whitespace();
        let x: i32 = iter.next().unwrap().parse().unwrap();
        let y: i32 = iter.next().unwrap().parse().unwrap();

        // swap value of list[x-1] and list[y-1]
        array.swap((x - 1) as usize, (y - 1) as usize);
    }

    println!("{}", array.iter().position(|&x| x).unwrap() + 1);
}

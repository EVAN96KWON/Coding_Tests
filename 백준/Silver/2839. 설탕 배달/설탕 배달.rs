fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut num = input.trim().parse::<i32>().unwrap();
    let mut answer: i32 = 0;

    while num >= 0 {
        if num % 5 == 0 {
            answer += num / 5;
            println!("{}", answer);
            return;
        }

        num -= 3;
        answer += 1;
    }
    println!("{}", -1);
}

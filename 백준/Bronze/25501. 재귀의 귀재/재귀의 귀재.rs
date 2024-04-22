use std::io::stdin;

fn recursion(s: String, l: usize, r: usize) -> usize {
    unsafe {
        cnt += 1;
    }
    if l >= r {
        return 1;
    } else if s.chars().nth(l).unwrap() != s.chars().nth(r).unwrap() {
        return 0;
    } else {
        return recursion(s, l + 1, r - 1);
    }
}

fn is_palindrome(s: String) -> usize {
    return recursion(s.clone(), 0, s.len() - 1);
}

static mut cnt: usize = 0;

fn main() {
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();
    let n = buffer.trim().parse::<usize>().unwrap();
    buffer.clear();

    for _ in 0..n {
        unsafe {
            cnt = 0;
            stdin().read_line(&mut buffer).unwrap();
            let s = buffer.trim().to_string();
            println!("{} {}", is_palindrome(s), cnt);
            buffer.clear();
        }
    }
}

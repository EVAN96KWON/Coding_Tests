use std::io::stdin;

fn cantorian(line: String) -> String {
    if line.len() == 1 {
        return line;
    }

    let s: usize = line.len() / 3;
    let prefix = line.chars().take(s).collect::<String>();
    let suffix = line.chars().skip(2 * s).collect::<String>();
    let space = " ".repeat(s);

    return format!("{}{}{}", cantorian(prefix), space, cantorian(suffix));
}

fn main() {
    loop {
        let mut buffer = String::new();
        stdin().read_line(&mut buffer).unwrap();
        let ret = buffer.trim().parse::<usize>();
        if ret.is_err() {
            break;
        }
        buffer.clear();

        let n = ret.unwrap();
        let line = "-".repeat(3_usize.pow(n as u32));

        println!("{}", cantorian(line));
    }
}

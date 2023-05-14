fn get_array(n: usize, m: usize) -> Vec<Vec<i32>> {
    let mut array = Vec::new();
    for _ in 0..n {
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        let mut row = Vec::new();
        for _ in 0..m {
            row.push(iter.next().unwrap().parse().unwrap());
        }
        array.push(row);
    }
    array
}

fn sum_array(array_a: Vec<Vec<i32>>, array_b: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let mut array = Vec::new();
    for i in 0..array_a.len() {
        let mut row = Vec::new();
        for j in 0..array_a[i].len() {
            row.push(array_a[i][j] + array_b[i][j]);
        }
        array.push(row);
    }
    array
}

fn print_array(array: Vec<Vec<i32>>) {
    for i in 0..array.len() {
        for j in 0..array[i].len() {
            print!("{} ", array[i][j]);
        }
        println!();
    }
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let array_a = get_array(n, m);
    let array_b = get_array(n, m);

    let array = sum_array(array_a, array_b);

    print_array(array)
}
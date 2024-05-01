use std::{collections::VecDeque, io};

fn infect(network: &Vec<Vec<usize>>, node: usize, n: usize) -> usize {
    let mut cnt = 0;

    let mut queue = VecDeque::new();
    queue.push_back(node);

    let mut visited = vec![false; n + 1];
    visited[node] = true;

    while let Some(idx) = queue.pop_front() {
        for &next in &network[idx] {
            if visited[next] {
                continue;
            }

            queue.push_back(next);
            visited[next] = true;
            cnt += 1;
        }
    }
    return cnt;
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let [n, m]: [usize; 2] = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect::<Vec<_>>()
        .try_into()
        .unwrap();
    input.clear();

    let mut network: Vec<Vec<usize>> = vec![vec![]; n + 1];
    for _ in 0..m {
        io::stdin().read_line(&mut input).unwrap();
        let [a, b]: [usize; 2] = input
            .trim()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect::<Vec<_>>()
            .try_into()
            .unwrap();
        network[b].push(a);
        input.clear();
    }

    let mut max_infection: usize = 0;
    let mut infection = vec![];
    for idx in 1..n + 1 {
        let curr = infect(network.as_ref(), idx, n);
        if curr > max_infection {
            max_infection = curr;
            infection.clear();
            infection.push(idx);
        } else if curr == max_infection {
            infection.push(idx);
        }
    }
    let ret = infection
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join(" ");
    println!("{}", ret);
}

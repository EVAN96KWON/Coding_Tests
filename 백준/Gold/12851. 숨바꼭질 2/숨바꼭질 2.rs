use std::{collections::VecDeque, io};

const MAX: usize = 100001;

fn bfs(n: usize, k: usize) -> (usize, usize) {
    let mut queue = VecDeque::from([n]);
    let mut visited = [0; MAX + 1];
    let (mut res, mut cnt) = (0, 0);

    while let Some(x) = queue.pop_front() {
        if x == k {
            res = visited[x];
            cnt += 1;
            continue;
        }

        let dirs: [i32; 3] = [x as i32 + 1, x as i32 - 1, x as i32 * 2];
        for nx in dirs {
            if 0 > nx {
                continue;
            }

            let nx = nx as usize;

            if MAX < nx {
                continue;
            }

            if visited[nx] == 0 || visited[nx] == visited[x] + 1 {
                visited[nx] = visited[x] + 1;
                queue.push_back(nx);
            }
        }
    }

    (res, cnt)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let [n, k]: [usize; 2] = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect::<Vec<_>>()
        .try_into()
        .unwrap();
    input.clear();

    let (res, cnt) = bfs(n, k);
    println!("{}", res);
    println!("{}", cnt);
}

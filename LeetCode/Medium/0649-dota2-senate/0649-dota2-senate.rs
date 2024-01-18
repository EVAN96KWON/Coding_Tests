use std::collections::VecDeque;

impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let n = senate.len();
        let mut rad = VecDeque::new();
        let mut dir = VecDeque::new();

        for i in 0..n {
            match senate.chars().nth(i).unwrap() {
                'R' => rad.push_back(i),
                'D' => dir.push_back(i),
                _ => panic!("invalid input"),
            }
        }

        while !rad.is_empty() && !dir.is_empty() {
            let r = rad.pop_front().unwrap();
            let d = dir.pop_front().unwrap();
            if r < d {
                rad.push_back(r + n);
            } else {
                dir.push_back(d + n);
            }
        }

        if rad.is_empty() {
            return "Dire".to_string();
        } else {
            return "Radiant".to_string();
        }
    }
}
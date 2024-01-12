use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let roman = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);
        let mut res = 0;

        for i in 0..s.len() {
            if i + 1 < s.len()
                && roman[&s.chars().nth(i).unwrap()] < roman[&s.chars().nth(i + 1).unwrap()]
            {
                res -= roman[&s.chars().nth(i).unwrap()];
            } else {
                res += roman[&s.chars().nth(i).unwrap()];
            }
        }
        res
    }
}

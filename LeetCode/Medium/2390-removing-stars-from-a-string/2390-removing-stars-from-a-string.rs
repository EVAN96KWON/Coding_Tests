impl Solution {
    pub fn remove_stars(s: String) -> String {
        let mut stack = vec![];
        for c in s.chars() {
            match c {
                '*' => { stack.pop(); }
                _ => { stack.push(c); }
            }
        }
        return stack.iter().collect();
    }
}

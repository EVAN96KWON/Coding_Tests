impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split_whitespace()
            .rev()
            .clone()
            .collect::<Vec<_>>()
            .join(" ")
    }
}
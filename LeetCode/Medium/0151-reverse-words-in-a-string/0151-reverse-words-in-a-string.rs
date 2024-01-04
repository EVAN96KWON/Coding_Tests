impl Solution {
    pub fn reverse_words(s: String) -> String {
        let words = s.split_whitespace().rev();
        words.clone().collect::<Vec<_>>().join(" ")
    }
}
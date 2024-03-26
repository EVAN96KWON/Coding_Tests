impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s = s
            .chars()
            .into_iter()
            .filter(|x| x.is_alphanumeric())
            .collect::<String>()
            .to_lowercase();
        s.chars().rev().collect::<String>() == s
    }
}

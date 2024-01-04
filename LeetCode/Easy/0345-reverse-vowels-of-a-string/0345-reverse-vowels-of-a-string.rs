impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let mut result: Vec<char> = s.chars().collect();
        let (mut i, mut j) = (0, s.len() - 1);
        while i < j {
            if Self::is_vowel(result[i]) {
                while j > i {
                    if Self::is_vowel(result[j]) {
                        (result[i], result[j]) = (result[j], result[i]);
                        j -= 1;
                        break;
                    }
                    j -= 1;
                }
            }
            i += 1;
        }
        result.iter().collect()
    }

    pub fn is_vowel(c: char) -> bool {
        "aeiouAEIOU".contains(c)
    }
}

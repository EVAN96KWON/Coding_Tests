impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let vec_s = s.chars().collect::<Vec<char>>();
        let mut ans = vec_s[0..k as usize]
            .iter()
            .filter(|&&c| Self::is_vowel(c))
            .count() as i32;
        let mut tmp = ans;

        for i in k as usize..vec_s.len() {
            if Self::is_vowel(vec_s[i - k as usize]) {
                tmp -= 1;
            }

            if Self::is_vowel(vec_s[i]) {
                tmp += 1;
            }
            ans = ans.max(tmp);
        }

        ans
    }

    fn is_vowel(c: char) -> bool {
        c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }
}

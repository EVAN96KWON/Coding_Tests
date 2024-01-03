impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let mut gathers = vec![];

        for c in s.chars() {
            if "aeiouAEIOU".contains(c) {
                gathers.push(c);
            }
        }
        gathers.reverse();

        let mut result = String::from("");

        for c in s.chars() {
            if "aeiouAEIOU".contains(c) {
                result.push(gathers.remove(0));
            } else {
                result.push(c);
            }
        }

        result
    }
}
 
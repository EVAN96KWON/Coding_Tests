use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let roman: HashMap<char, i32> = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);
        let mut result = 0;
        let chars: Vec<char> = s.chars().collect();

        for i in 0..chars.len() {
            let current_value = *roman.get(&chars.get(i).cloned().unwrap()).unwrap_or(&0);
            let next_value = *roman
                .get(&chars.get(i + 1).cloned().unwrap_or('\0'))
                .unwrap_or(&0);

            result += if current_value < next_value {
                -current_value
            } else {
                current_value
            };
        }

        result
    }
}

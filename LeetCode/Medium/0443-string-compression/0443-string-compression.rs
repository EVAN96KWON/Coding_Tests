use std::collections::VecDeque;

impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut stack = VecDeque::from(chars.clone());
        let mut compressed: VecDeque<char> = VecDeque::new();
        while !stack.is_empty() {
            compressed.push_back(stack.pop_front().unwrap());

            let mut count = 1;
            while !stack.is_empty() && stack[0] == compressed[compressed.len() - 1] {
                count += 1;
                stack.pop_front();
            }

            if count == 1 {
                continue;
            }

            compressed.extend(count.to_string().chars().collect::<Vec<char>>());
        }

        chars.clear();
        chars.extend(compressed);

        return chars.len() as i32;
    }
}

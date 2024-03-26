use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hm: HashMap<Vec<char>, Vec<String>> = HashMap::new();

        for s in strs {
            let mut key: Vec<char> = s.chars().collect();
            key.sort();
            if hm.contains_key(&key) {
                hm.get_mut(&key).unwrap().push(s);
            } else {
                hm.insert(key, vec![s]);
            }
        }

        return hm.values().cloned().collect();
    }
}

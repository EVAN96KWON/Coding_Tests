impl Solution {
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        let str1_str2 = str1.clone() + &str2;
        let str2_str1 = str2.clone() + &str1;

        if str1_str2 != str2_str1 {
            return "".to_string();
        }

        let gcd = Self::gcd(str1.len() as i32, str2.len() as i32);
        let res = &str1_str2[0..gcd as usize];

        res.to_string()
    }

    fn gcd(mut a: i32, mut b: i32) -> i32 {
        assert!(a != 0 && b != 0);
        while b != 0 {
            if b < a {
                std::mem::swap(&mut a, &mut b);
            }
            b %= a;
        }
        a
    }
}

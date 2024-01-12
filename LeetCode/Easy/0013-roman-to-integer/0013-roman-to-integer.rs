impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut res = 0;

        for i in 0..s.len() {
            let cur = Self::get_roman(s.chars().nth(i).unwrap());
            let next = Self::get_roman(s.chars().nth(i + 1).unwrap_or('0'));

            res += if cur < next { -cur } else { cur }
        }
        res
    }

    fn get_roman(roman_char: char) -> i32 {
        match roman_char {
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
            _ => 0,
        }
    }
}

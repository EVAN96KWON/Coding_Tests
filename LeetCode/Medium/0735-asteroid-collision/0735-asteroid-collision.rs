impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::new();
        for asteroid in asteroids {
            if asteroid > 0 {
                stack.push(asteroid);
            } else {
                while !stack.is_empty()
                    && stack.last().unwrap() > &0
                    && stack.last().unwrap() < &-asteroid
                {
                    stack.pop();
                }

                if stack.is_empty() || stack.last().unwrap() < &0 {
                    stack.push(asteroid);
                } else if stack.last().unwrap() == &-asteroid {
                    stack.pop();
                }
            }
        }
        return stack;
    }
}

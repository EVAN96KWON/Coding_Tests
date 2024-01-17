struct RecentCounter {
    counter: usize,
    queue: Vec<i32>,
}

impl RecentCounter {
    fn new() -> Self {
        RecentCounter {
            counter: 0,
            queue: Vec::new(),
        }
    }

    fn ping(&mut self, t: i32) -> i32 {
        self.queue.push(t);
        self.counter += 1;

        while self.queue[0] < t - 3000 {
            self.queue.remove(0);
            self.counter -= 1;
        }

        return self.counter as i32;
    }
}

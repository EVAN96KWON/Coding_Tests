impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let (mut max_altitude, mut altitude) = (0, 0);
        for g in gain {
            altitude += g;
            max_altitude = max_altitude.max(altitude);
        }
        return max_altitude;
    }
}

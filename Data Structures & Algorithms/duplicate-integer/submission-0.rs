use std::collections::{hash_set, HashSet};

impl Solution {
    // O(n) time, O(n) space
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut seen_nums = HashSet::new();
        for num in nums {
            if seen_nums.contains(&num) {
                return true;
            } else { seen_nums.insert(num); }
        }
        return false;
    }
}

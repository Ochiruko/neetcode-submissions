impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut max_ones = 0;
        let mut running_ones = 0;
        for num in nums {
            if num == 1 { running_ones += 1; }
            else {
                max_ones = max(max_ones, running_ones);
                running_ones = 0; 
            }
        }
        return max(max_ones, running_ones);
    }
}

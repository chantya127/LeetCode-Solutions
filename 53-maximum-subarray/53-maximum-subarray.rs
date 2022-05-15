impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut prev_sum = 0;
        let mut curr_sum = 0;
        let mut max_sum = i32::MIN;
        
        for num in nums{
            if (prev_sum > 0){
                prev_sum +=num;
            }
            else{
                prev_sum = num;
            }
            
            if(prev_sum > max_sum){
                max_sum = prev_sum;
            }
        }
        
        max_sum
    }
}
impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        
        match nums.is_empty(){
            true => 0,
            false => {
                let mut prev = 0;
                
                for index in 1..nums.len(){
                    if (nums[index] != nums[prev]){
                        prev +=1;
                        nums[prev] = nums[index];
                    }
                }
                (prev+1) as i32
            }
            
        }
    }
}
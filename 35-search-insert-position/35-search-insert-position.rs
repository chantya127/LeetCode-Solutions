impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        
        if (nums.len() == 0){
            return 0;
        }
        if (target < nums[0]){
            return 0;
        }
        let mut low = 0;
        let mut high = nums.len() -1;
        
        while low <= high {
            let mut mid = low + (high-low)/2;
            if nums[mid] == target{
                return mid as i32;
            }
            else if nums[mid] > target {
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        
        low as i32
        
    }
}
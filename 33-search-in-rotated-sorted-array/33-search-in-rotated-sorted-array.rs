impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
 

    let (mut low ,mut high) = (0 as usize, nums.len()-1);
    let mut mid = 0;

    while low <= high{

        mid = low + ((high-low) )/2;
        
        // println!("{} , {} ,{}" , mid , low, high);

        if nums[mid] == target{
            return mid as i32;
        }

        if nums[low] <= nums[mid]{

            if nums[low] <= target && target <= nums[mid]{
                high = mid-1;
            }
            else {
                low =mid+1;
            }
        }
        else{
            if nums[mid] <= target && target <= nums[high]{
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }

    }
    return -1;
}
}
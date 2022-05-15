impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        
        let mut prev = 0;
        let mut flag:bool = true;
        // let mut val = &val;
        
        for index in 0..nums.len(){
            if (nums[index] != val){
                if (flag){
                    flag = false;
                }
                else{
                    prev +=1;
                }
                nums[prev] = nums[index];
                
            }
        }
        // println!("{:?}" , nums);
        if (flag){
            return 0;
        }
        else{
            (prev+1) as i32
        }
    }
}
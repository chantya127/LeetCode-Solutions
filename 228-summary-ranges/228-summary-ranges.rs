impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut answer = Vec::new();
        
        let mut index = 0;
        
        while index < nums.len(){
            
            let curr = nums[index];
            
            while index < nums.len()-1 && nums[index+1] == nums[index]+1{
                index +=1;
            }
            let mut s = curr.to_string();
            
            if nums[index] != curr{
                s += "->";
                s += &nums[index].to_string();
            }
            answer.push(s);
            index +=1;
        }
        answer
    }
}
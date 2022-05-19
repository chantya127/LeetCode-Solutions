impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
    
    let mut ans = vec![];

    nums.sort();

    let size = nums.len();
    if size <3{
        return ans;
        }

    let mut low = 0;
    let mut high = 0;

    for idx in 0..size-2{

        if (idx>0 && nums[idx] == nums[idx-1]){
            continue;
        }
        let curr_ele = nums[idx];

        low = idx+1;
        high = size-1;

        while low < high{

            let sum = curr_ele + nums[low] + nums[high];

            if sum == 0 {
                let mut res = vec![nums[idx], nums[low] , nums[high]];
                ans.push(res);

                low +=1;
                high -=1;

                while low < high && nums[low] == nums[low-1]{
                    low = low+1;
                }

                while high > low && nums[high] == nums[high+1]{
                    high -=1;
                }
            }

            else if sum > 0{
                high -=1;
            }
            else{
                low +=1
            }
        }

    }

    return ans;
}
}
impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut ans:Vec<String> = Vec::new();
    
    for idx in 1..n+1{

        let mut curr_ans = String::new();

        if idx%3 ==0 && idx%5 ==0{
            curr_ans += "FizzBuzz";
        }
        else if idx%3 == 0 {
            curr_ans += "Fizz";
        }
        else if idx %5 == 0{
            curr_ans += "Buzz";
        }
        else{
            curr_ans += &idx.to_string();
        }

        ans.push(curr_ans)

    }
    ans
    }
}
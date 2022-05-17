
use std::cmp::max;
use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let size = s.len();

    if size <2{
        return size as i32;
    }
    let mut counting = HashMap::new();

    for chars in s.chars(){

        let count = counting.entry(chars).or_insert(0);
        *count +=1;
    }

    let mut even_c = 0;
    let mut odd_c = 0;
    let mut odds = 0;
        
    for (_ ,val) in counting.iter(){
        if val%2 ==0 {
            even_c+=val;
        }
        else{
            odd_c += val-1;
            odds+=1;
        }
    }

    let mut ans = even_c + odd_c;
    if (odds>0){
        ans +=1;
        }
    return ans;
    }
}
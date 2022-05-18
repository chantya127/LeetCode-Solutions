use std::collections::HashMap;
use std::cmp::max;

impl Solution {

    pub fn length_of_longest_substring(s: String) -> i32 {
    let mut counting:HashMap<char, u8> = HashMap::new();

    let mut ans = 0;

    let mut prev = 0;

    let ss:Vec<char> = s.chars().collect();
    let mut curr_len;


    for idx in 0..ss.len(){
        
        let  curr_char = ss[idx];

        if counting.contains_key(&curr_char){

            while prev < idx && counting.contains_key(&curr_char) {

                let count = counting.entry(ss[prev]).or_insert(0);
                
                counting.remove(&ss[prev]);

                prev+=1;

            }
        }
        counting.insert(curr_char ,1);

        curr_len = idx - prev+1;

        ans = max(ans , curr_len as i32)
    }    
    ans 
}

}


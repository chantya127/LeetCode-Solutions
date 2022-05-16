impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
     
        let mut start = 0;
        let mut end = s.len()-1;
        
        while start <end{
            let c1 = s[start];
            let c2 = s[end];
            
            s[start] = c2;
            s[end] = c1;
            
            start +=1;
            end -=1;
        }
    }
}
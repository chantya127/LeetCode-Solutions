impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        
        let mut rev_num :i32 = 0;
        
        let mut num = x;
        
        while num >0{
            
            let rem = num%10;
            
            rev_num = rev_num*10 + rem;
            num = num/10;
        }
        
        return (x == rev_num);
        
    }
}
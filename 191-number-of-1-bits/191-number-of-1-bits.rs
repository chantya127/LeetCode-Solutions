impl Solution {
    pub fn hammingWeight (mut n: u32) -> i32 {
        let mut res= 0;
        
        while n>0{
            
            res += (n&1) as i32;
            n = n>>1;
        }
        res
    }
}
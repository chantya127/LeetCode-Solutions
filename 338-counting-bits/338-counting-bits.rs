impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        
        let n = (n+1) as usize;
        let mut ans = vec![0;n];
        
        for idx in 1..n{
            ans[idx] = if idx%2 == 0{
                ans[idx/2]
            }
            else{
                ans[idx-1] +1
            }
        }
        ans
    }
}
impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
     
        let mut digits = digits;
        
        for idx in (0..digits.len()).rev(){
            println!("{}" , idx);
            
            if (digits[idx] == 9){
                digits[idx] = 0;
            }
            else{
                digits[idx] +=1;
                return digits;
            }
        }
        digits.insert(0,1);
        digits
    }
}
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        
        if strs.len() == 0{
            return "".to_string();
        }
        
        let mut common:&str = &strs[0];
        
        for s in strs.iter().skip(1) {
            for i in (0 .. common.len()+1).rev(){
                if (s.starts_with(&common[..i])){
                    common = &common[..i];
                    break;
                }
            
            
            // println!("{}" , s);
            }
        }
            common.to_string()
    }
}
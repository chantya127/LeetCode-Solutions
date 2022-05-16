use std::collections::HashMap;


impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        
        let mut mapping_s_t = HashMap::new();
        
        let mut mapping_t_s = HashMap::new();
        
        let s1:Vec<char> =  s.chars().collect();
        let s2:Vec<char> =  t.chars().collect();
        
        for index in 0..s1.len(){
            
            let mut c1 = s1[index];
            let mut c2 = s2[index];
            
            if (mapping_s_t.contains_key(&c1) && mapping_s_t[&c1] != c2){
                return false;
            }
            
            if (mapping_t_s.contains_key(&c2) && mapping_t_s[&c2] != c1){
                return false;
            }
            mapping_s_t.insert(c1,c2);
            mapping_t_s.insert(c2,c1);
        }
        true
        
    }
}
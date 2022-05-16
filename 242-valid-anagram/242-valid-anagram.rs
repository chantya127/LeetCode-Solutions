use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        
        let mut mapping = HashMap::new();
        
        for ch in s.chars(){
            let  count = mapping.entry(ch).or_insert(0);
            *count +=1;
        }
        
        for ch in t.chars(){
            
            match mapping.get(&ch){
                Some(val) => {
                    mapping.insert(ch , mapping[&ch]-1);
                },
                None => {return false;}
            }
        }
        
        for (key,val) in mapping.iter(){
            if (*val !=0){
                return false;
            }
        }
        true
    }
}
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        
    let mut ans:Vec<String> = vec![String::new();num_rows as usize];

    let mut index = 0;

    let mut step = if num_rows==1{0} else{ -1};

    for c in s.chars(){
        
        ans[index as usize].push(c);

        if (index == 0 || index == (num_rows-1)){
            step = -step;
        }
        index +=step;
    }
    
    ans.join("")

}
}
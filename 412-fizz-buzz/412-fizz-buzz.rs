impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        return (1..=n).map(|x| {
        let by3 = x%3==0;
        let by5 = x%5==0;
        
        match (by3 , by5){
            (true,true) => "FizzBuzz".to_string(),
            (true,false) =>"Fizz".to_string(),
            (false,true) => "Buzz".to_string(),
            _ => x.to_string(),
        }
    }).collect();
    }
}
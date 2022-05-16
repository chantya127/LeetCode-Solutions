use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_binary_matrix(mut grid: Vec<Vec<i32>>) -> i32 {
        let l = grid.len();
        let mut queue = VecDeque::new();
        
        if (grid[0][0] == 1){
            return -1;
        }
        let dx:Vec<i32> = vec![0, 0, 1, -1, -1, -1, 1, 1];
        let dy:Vec<i32> = vec![1, -1, 0, 0, 1, -1, -1, 1];
        
        queue.push_back((0,0,1));
        grid[0][0] = 1;
        
        while let Some((i,j,dis)) = queue.pop_front(){
            if i == l-1 && j == l-1{
                return dis;
            }
            
            for (&r,&c) in dx.iter().zip(dy.iter()){
                let ii:i32 = i as i32 + r;
                let jj:i32 = j as i32 + c;
                
                if ii as usize >=0 && (ii as usize) < (l as usize) && jj as usize >=0 && (jj as usize) < (l as usize) && grid[ii as usize][jj as usize] == 0{
                    queue.push_back((ii as usize, jj as usize, dis+1));
                    grid[ii as usize][jj as usize] = 1;
                }
                
            }
        }
        -1
        
    }
}
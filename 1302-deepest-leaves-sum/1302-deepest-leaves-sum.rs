// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }



// use std::rc::Rc;
// use std::cell::RefCell;

// impl Solution {
//     pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
//         let mut res: i32 = 0;
//         let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
//         if let Some(node) = root {
//             queue.push_front(node);
//         }
//         while !queue.is_empty()  {
//             res = 0;
//             for i in 0..queue.len() {
//                 if let Some(n) = queue.pop_back() {
//                     let mut node = n.borrow_mut();
//                     res += node.val;
//                     if node.right.is_some() {
//                         queue.push_front(node.right.take().unwrap());
//                     }
//                     if node.left.is_some() {
//                         queue.push_front(node.left.take().unwrap());
//                     }
//                 }
//             }
//         }
//         res
//     }
// }




use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
     
        let mut res = 0;
        let mut ququ = VecDeque::new();
        
        if let Some(node) = root {
            ququ.push_front(node);
        }
        
        while ! ququ.is_empty(){
            res = 0;
            for i in 0..ququ.len() {
                if let Some(n) = ququ.pop_back() {
                    let mut node = n.borrow_mut();
                    res += node.val;
                    
                    if (node.right.is_some()){
                        ququ.push_front(node.right.take().unwrap());
                    }
                    
                    if node.left.is_some(){
                        ququ.push_front(node.left.take().unwrap());
                    }
                }
            }
        }
        
        res
    }
}
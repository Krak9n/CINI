use std::io;

fn main() {
    let (mut length, mut s, mut q, mut cases) = (String::new(), String::new(), String::new(), String::new());

    io::stdin()
        .read_line(&mut length)
        .unwrap();
    let length: u16 = length.trim().parse().unwrap();
    io::stdin()
        .read_line(&mut s)
        .unwrap();
    io::stdin()
        .read_line(&mut q)
        .unwrap();
    let q: u32 = q.trim().parse().unwrap(); 
    for i in (0..q).rev() {
        io::stdin()
            .read_line(&mut cases)
            .unwrap();
        let mut a_b: Vec<u32> = cases
            .split_whitespace()
            .map(|x| x.trim().parse().unwrap())
            .collect();
        // logic starts here
    }
}

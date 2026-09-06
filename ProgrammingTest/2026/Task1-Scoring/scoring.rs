use std::io;

fn sum(input: &mut Vec<u32>) -> u32 {
    if input.len() <= 10 {
        return input.iter().sum();
    }
    input.sort_by(|a, b| b.cmp(a));
    let temp = input
        .drain(..10).collect::<Vec<u32>>()
        .into_iter().sum();
    temp
}

fn main() {
    let (mut T, mut N, mut S) = (String::new(), String::new(), String::new());
    io::stdin()
        .read_line(&mut T)
        .unwrap();
    let T: u32 = T.trim().parse().unwrap();
    for i in (0..T).rev() {
        io::stdin()
            .read_line(&mut N)
            .unwrap();
        let mut n: u32 = N.trim().parse().unwrap();
        io::stdin()
            .read_line(&mut S)
            .unwrap();
        let mut scores: Vec<u32> = S
            .split_whitespace()
            .map(|x| x.trim().parse().unwrap())
            .collect();
        println!("{}", sum(&mut scores));
        N.clear();
        S.clear();
    }
}

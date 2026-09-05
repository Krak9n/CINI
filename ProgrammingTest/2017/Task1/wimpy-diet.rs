use std::io;

fn main() {
    let (mut N, mut W) = (String::new(), String::new());
    io::stdin()
        .read_line(&mut N)
        .unwrap();
    let N: u32 = N.trim().parse().unwrap();

    io::stdin()
        .read_line(&mut W)
        .unwrap();
    let W: Vec<u32> = W
        .split_whitespace()
        .map(|x| x.trim().parse().unwrap())
        .collect();

    for (index, value) in W.into_iter().rev().enumerate() {
        println!("{}: {}", index, value);
    }
}

use std::fs::File;
use std::{io, io::BufReader, io::BufRead};
    
fn read_file(path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let output_file = File::open(path)?;
    let output_file_buffer = BufReader::new(output_file);

    for line in output_file_buffer.lines() {
        println!("Expected output: {}", line?);
    }

    Ok(())
}

// input
// Line 1: N, number of sandwiches on the menu
// Line 2: N integers

// output
// Line 1: number of sandwiches in the solution
// Line 2: weights of the remaining sandwiches 
fn main() -> io::Result<()> {
    let file = File::open("input/input2.txt")?;
    let file_buffer = BufReader::new(file);

    let mut N: u32 = 0;
    let mut sandwiches: Vec<u32> = vec![];

    for line in file_buffer.lines() {
        let line = line?;
        println!("Given: {}", line);
        // check if this is a single N, if it is then just push everything in a single line
        // check: if the N is empty; if the sanwiches is empty; if line contains whitespaces;  
        if N == 0 {
            N = line.trim().parse().expect("Failed to parse N");
        }
        else {
            let holder: Vec<u32> = line
                .split_whitespace()
                .map(|x| x.parse().expect("Failed to parse"))
                .collect();
            sandwiches = holder
                .into_iter().rev()
                .collect::<Vec<_>>()
                .array_windows::<2>()
                .filter_map(|&[x, y]| (x > y).then_some(y))
                .rev()
                .collect();
        }
    }
    println!("Size: {}", sandwiches.len());
    print!("Result: ");
    for sandwich in &sandwiches {
        print!("{} ", sandwich)
    }

    println!();
    read_file("output/output2.txt");

    Ok(())
}

fn main() {
    use std::io;

    let mut entrada = String::new();
    io::stdin().read_line(&mut entrada).expect("Erro ao ler a entrada");

    let notas: Vec<f32> = entrada.split_whitespace()
        .map(|x| x.parse().expect("Entrada não é um número!"))
        .collect();

    let media = notas.iter().sum::<f32>() / notas.len() as f32;
    println!("A média é  {:?}", media);
}
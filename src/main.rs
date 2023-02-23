use std::error::Error;
use std::fs::File;
use std::io::BufReader;

use rodio::Decoder;
use rppal::{gpio::Gpio, system::DeviceInfo};

fn load_sound_source(file_path: &str) -> Result<Decoder<BufReader<File>>, Box<dyn Error>> {
    let file = BufReader::new(
        File::open(file_path)
            .map_err(|e| format!("Unable to open file '{}': {}", file_path, e))?,
    );
    Decoder::new(file).map_err(|e| e.into())
}

fn main() -> Result<(), Box<dyn Error>> {
    let device_info = DeviceInfo::new()?;
    println!("Device: {:?}\nStarting piano...", device_info);

    let a_major_sound = load_sound_source("notes/A_major.wav").unwrap();
    let b_major_sound = load_sound_source("notes/B_major.wav").unwrap();
    let c_major_sound = load_sound_source("notes/C_major.wav").unwrap();
    let d_major_sound = load_sound_source("notes/D_major.wav").unwrap();
    let e_major_sound = load_sound_source("notes/E_major.wav").unwrap();
    let f_major_sound = load_sound_source("notes/F_major.wav").unwrap();
    let g_major_sound = load_sound_source("notes/G_major.wav").unwrap();

    let a_sharp_sound = load_sound_source("notes/A_sharp.wav").unwrap();
    let c_sharp_sound = load_sound_source("notes/C_sharp.wav").unwrap();
    let d_sharp_sound = load_sound_source("notes/D_sharp.wav").unwrap();
    let f_sharp_sound = load_sound_source("notes/F_sharp.wav").unwrap();
    let g_sharp_sound = load_sound_source("notes/G_sharp.wav").unwrap();

    Ok(())
}

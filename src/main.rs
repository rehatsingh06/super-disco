use std::error::Error;
use std::fs::File;
use std::io::BufReader;

use rodio::{source::Source, Decoder, OutputStream};
use rppal::{gpio::Gpio, system::DeviceInfo};

fn load_sound_source(file_path: &str) -> Result<Decoder<BufReader<File>>, Box<dyn Error>> {
    let file = BufReader::new(
        File::open(file_path).map_err(|e| format!("Unable to open file '{}': {}", file_path, e))?,
    );
    Decoder::new(file).map_err(|e| e.into())
}

fn main() -> Result<(), Box<dyn Error>> {
    let device_info = DeviceInfo::new()?;
    println!("Device: {:?}\nStarting piano...", device_info);

    let (_stream, stream_handle) = OutputStream::try_default()?;

    let a_major_sound = load_sound_source("notes/A_major.wav")?;
    let b_major_sound = load_sound_source("notes/B_major.wav")?;
    let c_major_sound = load_sound_source("notes/C_major.wav")?;
    let d_major_sound = load_sound_source("notes/D_major.wav")?;
    let e_major_sound = load_sound_source("notes/E_major.wav")?;
    let f_major_sound = load_sound_source("notes/F_major.wav")?;
    let g_major_sound = load_sound_source("notes/G_major.wav")?;

    let a_sharp_sound = load_sound_source("notes/A_sharp.wav")?;
    let c_sharp_sound = load_sound_source("notes/C_sharp.wav")?;
    let d_sharp_sound = load_sound_source("notes/D_sharp.wav")?;
    let f_sharp_sound = load_sound_source("notes/F_sharp.wav")?;
    let g_sharp_sound = load_sound_source("notes/G_sharp.wav")?;

    stream_handle.play_raw(a_major_sound.convert_samples())?;

    Ok(())
}

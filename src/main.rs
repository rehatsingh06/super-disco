use rppal::{gpio::Gpio, system::DeviceInfo};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let device_info = DeviceInfo::new()?;
    println!("Device: {:?}\nStarting piano...", device_info);

    Ok(())
}

#![no_std]
#![no_main]
#![feature(type_alias_impl_trait)]

use embassy_executor::Spawner;
use embassy_rp::gpio;

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    let p = embassy_rp::init(Default::default());

    let a_major = gpio::Input::new(p.PIN_14, gpio::Pull::Down);
    let a_sharp = gpio::Input::new(p.PIN_17, gpio::Pull::Down);

    let b_major = gpio::Input::new(p.PIN_15, gpio::Pull::Down);

    let c_major = gpio::Input::new(p.PIN_18, gpio::Pull::Down);
    let c_sharp = gpio::Input::new(p.PIN_27, gpio::Pull::Down);

    let d_major = gpio::Input::new(p.PIN_23, gpio::Pull::Down);
    let d_sharp = gpio::Input::new(p.PIN_12, gpio::Pull::Down);

    let e_major = gpio::Input::new(p.PIN_24, gpio::Pull::Down);

    let f_major = gpio::Input::new(p.PIN_25, gpio::Pull::Down);
    let f_sharp = gpio::Input::new(p.PIN_10, gpio::Pull::Down);

    let g_major = gpio::Input::new(p.PIN_8, gpio::Pull::Down);
    let g_sharp = gpio::Input::new(p.PIN_9, gpio::Pull::Down);
}

# Alexa-Raspberry-Smart-Plug-433MHz

Emulated Belkin WeMo (UPNP Emulation) smart plug for Amazon Echo working with 433MHz plug 

## Requirements

* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* fauxmo - [makermusings/fauxmo](https://github.com/makermusings/fauxmo)
* fork fauxmo - [n8henrie/fauxmo](https://github.com/n8henrie/fauxmo)
* 433Utils - [ninjablocks/433Utils](https://github.com/ninjablocks/433Utils)
* rfoutlet - [timleland/rfoutlet](https://github.com/timleland/rfoutlet)

## codes

[Etekcity ZAP 2L](https://www.amazon.fr/dp/B01M262058/)
```
pulse 175 (between 175 and 180) 
1:
on: 1054003
off: 1054012

2:
on: 1054147
off: 1054156

3:
on: 1054467
off: 1054476
```

## Installation

```
make ~/433-Alexa
cd ~/433-Alexa
apt-get install git
apt-get install python3-pip

# wiringPi
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build

# 433Utils
git clone --recursive git://github.com/ninjablocks/433Utils.git
cd 433Utils/RPi_utils
make

# fauxmo
git clone https://github.com/makermusings/fauxmo.git
python3 -m pip install fauxmo

# flask
pip3 install Flask
```

## Links

* [fauxmo](https://github.com/n8henrie/fauxmo)
* [Raspberry pins](https://fr.pinout.xyz/pinout/pin1_alimentation_33v)
* [433MHz](https://manipovore.com/raspberry-pi/raspberry-pi-domotique/)
* [433MHz](https://www.fanjoe.be/?p=2301)
* [433MHz](https://www.instructables.com/id/RF-433-MHZ-Raspberry-Pi/)

## Authors

* **Lionel Jouin** - [LionelJouin](https://github.com/LionelJouin)  

See also the list of [contributors](https://github.com/LionelJouin/Alexa-Raspberry-Smart-Plug-433MHz/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

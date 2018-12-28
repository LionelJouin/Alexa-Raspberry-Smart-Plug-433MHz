# Alexa-Raspberry-Smart-Plug-433MHz

Smart plug for Amazon Echo working with 433MHz plug working with ha-bridge

## Requirements

* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* ha-bridge - [bwssytems/ha-bridge](https://github.com/bwssytems/ha-bridge)

## codes

[Etekcity ZAP 2L](https://www.amazon.fr/dp/B01M262058/)
```
pulse 175 (between 175 and 180) 
0:
on: 1054003
off: 1054012

1:
on: 1054147
off: 1054156

2:
on: 1054467
off: 1054476
```

## Installation

```
cd /root/
apt-get install git
apt-get install python3-pip
apt-get install openjdk-8-jre-headless

# wiringPi
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build

# 433Utils
git clone --recursive git://github.com/ninjablocks/433Utils.git
cd 433Utils/RPi_utils
make

# download ha-bridge
wget https://github.com/bwssytems/ha-bridge/releases/download/v5.2.1/ha-bridge-5.2.1.jar

# flask
pip3 install Flask

git clone https://github.com/LionelJouin/Alexa-Raspberry-Smart-Plug-433MHz.git
```

## Services

### ha-bridge (ha-bridge.service)

```
[Unit]
Description=HA Bridge
Wants=network.target
After=network.target

[Service]
Type=simple

WorkingDirectory=/root/ha-bridge
ExecStart=/usr/bin/java -jar -Dconfig.file=/root/ha-bridge/data/habridge.config /root/ha-bridge/ha-bridge-5.2.1.jar

[Install]
WantedBy=multi-user.target
```

### 433MHz (server-433.service)

```
[Unit]
Description=433MHz Flask
Wants=network.target
After=network.target

[Service]
Type=simple

WorkingDirectory=/root/
ExecStart=/usr/bin/python3 /root/Alexa-Raspberry-Smart-Plug-433MHz/server.py

[Install]
WantedBy=multi-user.target
```

### start/enable services

```
# /etc/systemd/system
systemctl daemon-reload
systemctl start ha-bridge.service
systemctl enable ha-bridge.service
systemctl start server-433.service
systemctl enable server-433.service
```

## Links

* fauxmo - [makermusings/fauxmo](https://github.com/makermusings/fauxmo)
* fauxmo (fork) - [n8henrie/fauxmo](https://github.com/n8henrie/fauxmo)
* fork fauxmo - [n8henrie/fauxmo](https://github.com/n8henrie/fauxmo)
* 433Utils - [ninjablocks/433Utils](https://github.com/ninjablocks/433Utils)
* rfoutlet - [timleland/rfoutlet](https://github.com/timleland/rfoutlet)
* [tutoriel ha-bridge (FR)](https://www.lesalexiens.fr/tutoriels/tutoriel-ha-bridge-amazon-alexa-raspberry/)
* [Raspberry pins](https://fr.pinout.xyz/pinout/pin1_alimentation_33v)
* [433MHz](https://manipovore.com/raspberry-pi/raspberry-pi-domotique/)
* [433MHz](https://www.fanjoe.be/?p=2301)
* [433MHz](https://www.instructables.com/id/RF-433-MHZ-Raspberry-Pi/)

## Authors

* **Lionel Jouin** - [LionelJouin](https://github.com/LionelJouin)  

See also the list of [contributors](https://github.com/LionelJouin/Alexa-Raspberry-Smart-Plug-433MHz/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# Water Monitor Sensors Bridge

> Receives data from water quality sensors - Ecotriplets 1, 2, and 3, dissolved oxygen, and co2procv.
> It saves data to a folder and sends it to a server.
>
>
## User Installation

- Copy dist folder in this repository and double click SensorsBridge.exe. Keep all files in dist folder together. 


## Developer Installation

- Install Python 3.6 

``` bash
# Install dependencies
pip install -r requirements.txt

```

Configuration
---
In config.json set:
- `data_path` to your preferred output location
- Change COM3, COM4, COM5, COM6, COM7 to their respective port in which they are connected to your computer.
- If you have data streamed through a UDP port, modify `udp_port`
---
In you would like to send data to your server fill out the following:

- server: "https://servername.org/somepath/"
- server_login = "https://water.geosci.msstate.edu/monitoradmin/signin"
- username: "someusername"
- password: "somepassword"
- If you are not sending data to a server make sure to set `send_data` to `false`.

Usage
---
- Run run.py or double click `start_sensors_bridge.bat` file. It will start reading and saving data to the DATA_PATH.
- You can run the script as a schedule task using `sensors_bridge_task.xml`.

## App Info

### Authors
- Jane Moorhead
- Wondimagegn Tesfaye Beshah

### Version

1.0.0

### License

Copyright@ Mississippi State University

# DCS WebGCI Importer

A Python tool to help handling Hoggit's at War - WebGCI website coordinates and information of targets into DCS (Digital Combat Simulator).
Information must be provided via selection (hold left-click, drag) in a Windows environment (others may work).

[Video demo](https://youtu.be/LLg_pqPNMb8)

### Requirements

In order to build your own, you'll need:
* Python 3.7.x
* [pymgrs](https://pypi.org/project/mgrs/)
* [pyautogui](https://pypi.org/project/PyAutoGUI/)
* [pywin32](https://pypi.org/project/pywin32/)
* [keyboard](https://pypi.org/project/keyboard/)
* [DCS Bios](https://github.com/dcs-bios/dcs-bios/)

### Installing

To ease the install process a requirements file is provided and can be used as follows. This however doesn't install DCS Bios as they have their own setup, please follow their guidelines for a clean install.
```
python -m pip install -r requirements.txt
```

After everything is ready, run the main script.
```
python main.py
```

Expected behaviour is for the the console cursor to hang (as if waiting), that means the script is waiting for user input.

## Getting Started

Extracting target information:
* Navigate to [Persian Gulf at War](https://atwar.online/pgawgci.php) or [Georgia at War](https://atwar.online/gawgci.php)
* (Optional) Configure your keybindings and options on config.json
* Start DCS: A-10C and make sure your CDU is running properly (aligned) and in the waypoint edit page
* Run main.py
```
python main.py
```
* Pick a target on the chosen website, it can be any airfield, unit or building (warehouses) as long as it displays elevation, latitude and longitude
* Select information to be extracted from the popup, example: SA-18 Igla Manpad, Latitude: 25° 19' 22.07" N, Longitude: 055° 31' 52.00" E, Elevation: 98 ft (29 m)
* Press Shift+C (default)
* The script should run and convert your ddmmss.ss coordinates to dd then to MGRS/UTN and send the corresponding key presses to DCS via DCS Bios

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Big thank you to Eagle Dynamics for creating the beautiful game DCS is.
* Huge shoutout for the people who created DCS Bios and the guys at the DCS Bios discord server.
* Blackbird from Hoggit Staff that helped me on basic coordinate principles which in turn inspired me to do this tool for fun.

# DCS WebGCI Importer

A Python tool to help handling Hoggit's at War - WebGCI website coordinates and information of targets into DCS (Digital Combat Simulator).
Information must be provided via selection in a Windows environment, Linux has not been tested as of 12th August 2019 (should work assuming modules are cross-platform).

## Getting Started

See [example.py](example.py) for a working example and basis for code examples below.

Extracting unit coordinates and elevation:
* Choose [Persian Gulf at War](https://atwar.online/pgawgci.php) or [Georgia at War](https://atwar.online/gawgci.php)
* Run example.py
* Open up DCS: A-10C and make sure your CDU is running normally
* Pick a target, can be any airfield, unit or building (warehouses) as long as it displays elevation, latitude and longitude
* Select information to be extracted from the popup, example: Latitude: 25° 19' 22.07" N, Longitude: 055° 31' 52.00" E, Elevation: 98 ft (29 m)
* Press Shift+C
* The script should run and convert your ddmmss.ss coordinates to dd then to MGRS/UTM, and then send the key presses to DCS via the DCS Bios interface

### Prerequisites

In order to build your own, you'll need:
* [pymgrs](https://pypi.org/project/mgrs/)
* [pyautogui](https://pypi.org/project/PyAutoGUI/)
* [pyperclip](https://pypi.org/project/pyperclip/)
* socket
* [DCS Bios](https://github.com/dcs-bios/dcs-bios/)

```
python -m pip install mgrs pyautogui pyperclip
```

### Installing

Follow DCS Bios installation instructions then run the example script provided
```
python example.py
```
## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Big thank you to Eagle Dynamics for creating the beautiful game DCS is.
* Huge shoutout for the people who created DCS Bios and the guys at the DCS Bios discord server.
* Blackbird from Hoggit Staff that helped me on basic coordinate principles which in turn inspired me to do this tool for fun.

# Battery Indicator Dot

A minimal floating dot for Windows that shows your battery charging status using a colored dot overlay. Green means charging, gray means not charging.

## Why use this widget?
If you keep your Windows taskbar set to auto-hide for a true full-screen experience, it can be annoying to move your mouse to the taskbar just to check if your laptop is charging. This widget solves that problem: it displays a tiny always-on-top dot so you can instantly see if your battery is charging (green) or not (gray), without ever opening the taskbar or interrupting your workflow. It's the perfect solution for distraction-free, full-screen setups.

*Planned feature: soon, the dot will also show the battery percentage inside the icon for even more convenience!*

## Features
- Tiny always-on-top indicator
- Green dot when charging, gray when not
- Right-click to close
- Transparent background (Windows only)

## Demo Images

<p align="center">
  <img src="Battery Indicator Dot ON Image.png" alt="Battery Indicator ON" width="300"/>
</p>
<p align="center"><i>Battery Indicator ON: The battery indicator dot is visible, showing the active (ON) state.</i></p>

<p align="center">
  <img src="Battery Indicator Dot OFF Image.png" alt="Battery Indicator OFF" width="300"/>
</p>
<p align="center"><i>Battery Indicator OFF: The battery indicator dot is not illuminated, illustrating the inactive (OFF) state.</i></p>


## Requirements
- Python 3.7+
- [psutil](https://pypi.org/project/psutil/)
- [Pillow](https://pypi.org/project/Pillow/)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/BharathSadineni/Battery-Indicator-Dot.git
   cd Battery-Indicator-Dot
   ```
2. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the indicator:
```sh
python battery.py
```
- The dot appears in the top-right corner of your screen.
- Right-click the dot to close it.
- You can also close the app with Ctrl+C in the terminal.

## Notes
- For transparency, this app uses a Windows-only Tkinter feature. 

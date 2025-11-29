![DemWiiFlowTools-logo](https://github.com/user-attachments/assets/008589b5-fb7b-43e7-ad86-5d1d1d231842)



 
#  Below Average Gaming Wiiflow Scripts Collection 

Welcome to the **BAG** repository for Wiiflow!
This collection of Python scripts helps retro gaming enthusiasts organize, rename, de-duplicate, and transfer their game files and cover art across **45 systems**—with support for auto-copying directly to your SD/USB drive.

You can see them in action on the [Below Average Gaming YouTube channel](https://youtu.be/0eYDwNgxgVk?si=qoaPJ_W4FqCY_KPm).

---

## 🔑 Key Features

* **Automated File Renaming**
  Detects and renames ROMs and cover art (`.zip`, `.bin`, `.cue`, `.a26`, `.d64`, etc.) based on curated text lists.

* **Special Naming Conventions**

  * Converts Roman numerals → Arabic numerals
  * Retains disc numbers `(Disc 1), (Disc 2, …)`
  * Cleans up complex title structures

* **Duplicate Title Detection**
  Scripts scan for duplicates (multiple versions of the same game) and let you choose which to keep, ensuring a clean Wiiflow library without clutter.

* **Iterative Processing**
  Runs in loops to ensure all files are renamed correctly—no stragglers left behind.

* **Auto SD/USB Transfer**
  New scripts automatically copy files into the correct structure on your SD or USB device for Wiiflow.

---

## 🎮 Supported Platforms (45 total)

### 🕹️ Arcade

* CPS2
* CPS3
* Final Burn Alpha
* Final Burn Neo
* MAME

### 💾 PC

* Commodore 64

### 🎮 Consoles

* Amstrad GX4000
* Atari 2600
* Atari 5200
* Atari 7800
* Atari XEGS
* Colecovision
* CreatiVision
* Famicom Disk System
* Intellivision
* Neo Geo CD
* NES
* Nintendo 64
* Odyssey²
* PC-FX
* PlayStation 1
* Satellaview
* Sega 32X
* Sega CD
* Sega Genesis / Mega Drive
* Sega Master System
* Sega SG-1000
* SNES / Super Famicom
* SuperGrafx
* Turbo Duo
* TurboGrafx-16
* Vectrex

### 🎮 Handhelds

* Atari Lynx
* Game & Watch
* Game Boy
* Game Boy Advance
* Game Boy Color
* Neo Geo Pocket
* Neo Geo Pocket Color
* Pokémon Mini
* Sega Game Gear
* Virtual Boy
* Watara Supervision
* WonderSwan
* WonderSwan Color

---

## 📂 How It Works (depending on the system)

1. Place your ROMs in the system’s `games/` folder.
2. Place unzipped PNG cover art in the `cover art/` folder.
3. Run the script (`DEM Wiiflow Tools Launcher.py`). 
4. Follow the prompts to rename, de-duplicate, organize, and (if wanted) transfer files to your SD/USB device.

Covers must **exactly match the ROM filename (including extension) + `.png`**, or Wiiflow won’t recognize them.

> Example: `SuperGame.zip` → `SuperGame.zip.png`

renamed cover art will be sent to the "renamed cover art" folder
renamed games will stay in the same folder
---





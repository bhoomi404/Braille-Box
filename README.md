# Braille-Box 🔠🔊  
🛠️ Work in progress — Building a dual-mode Braille input/output device for visually impaired users.

## 🔍 Project Overview

The **Braille Box** is a hardware-software assistive device designed to help visually impaired individuals both write and read Braille using tactile buttons and solenoids, enhanced with audio feedback via text-to-speech.

Built using a **Raspberry Pi**, tactile switches, and actuators, the system allows:
- 📝 **Writing Mode** – Users press 6 tactile buttons to form Braille characters. Detected characters are spoken aloud using `espeak` and optionally saved for later reading.
- 📖 **Reading Mode** – Stored text is converted into Braille and physically raised using solenoids, allowing users to read it through touch.

## 🔧 Features
- Dual-mode operation (read/write) controlled by a **toggle switch**
- **6-button Braille keypad** for character input
- **Solenoid-driven Braille cell** for tactile output
- **Text-to-speech** output using `espeak`
- **Offline support** for secure, exam-compatible use
- **Audio toggle** for silent mode

## 🗂️ Project Structure (Planned)
Braille-Box/
├── hardware/
│ └── Circuit Diagram.png
├── software/
│ └── main.py (coming soon)
├── docs/
│ └── block_diagram.png (coming soon)
├── README.md
└── LICENSE


## 🚀 Project Progress

- ✅ Circuit diagram completed (Fritzing)
- ⬜ GPIO mapping and testing of Braille input
- ⬜ Code to convert button presses into characters
- ⬜ Integration of solenoids for Braille output
- ⬜ Text-to-speech setup and audio feedback
- ⬜ USB export/silent mode logic (planned)

## 📷 Preview

![Circuit Diagram](hardware/Circuit%20Diagram.png)

## 🎯 Vision

> "Making accessible technology simple, scalable, and affordable — one tactile dot at a time."

## 👥 Contributions

Suggestions, ideas, and forks are welcome. Let’s collaborate to make assistive tech more inclusive.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

# Binary Bingo
A Binary Bingo toolkit developed by **Zoe Weston** for the **University of Surrey Computer Science Society (CompSoc)** as part of *Belonging Week*.

This project brings together code, creativity, and community — combining binary number generation with colourful, custom bingo cards for a fun interactive event!

## Overview
The repository contains two main components:

### **Bingo Card Generator (`binary bingo card generator.py`)**
Generates unique, printable bingo cards as PDF files.  
Each card:
- Uses numbers **0–127**
- Features a **purple → teal gradient** matching CompSoc’s branding  
- Displays a **binary card ID** (e.g. `Card Number: 0000 0011`) for easy tracking  

### **Binary Number Display (`bingo binary number generator.py`)**
A live display built with **Tkinter**, showing random binary numbers between 0–127.  
- Displays each number in **binary** first, then the **decimal** value  
- Features a **scrolling banner** showing all called numbers  
- Uses the same **gradient colour scheme** for consistency  
- Prevents duplicate numbers via a custom **linked list** structure  

## Features
- Generates globally unique bingo cards (no duplicates)  
- Smooth gradient between CompSoc’s purple `#ae46ea` and teal `#28d6a9`  
- Binary-themed visual design and card numbering  
- Randomised, non-repeating number generation  
- Easy to run and customise for any event  

## Requirements

### General
- **Python 3.8+**

### Bingo Card Generator (`binary bingo card generator.py`)
Used to generate printable bingo cards.

**Libraries:**
- `reportlab` – for creating and exporting PDFs  
- `pillow` – for image and colour gradient handling  

**Install:**
```bash
pip install reportlab pillow


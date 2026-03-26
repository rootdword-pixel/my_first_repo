# Universal Lexicon - Biblical Word Study & Gematria App (v1.0)

## Project Summary
Universal Lexicon is a fully offline single-file HTML web app for biblical word study using gematria across six scripts. It combines live calculation, letter breakdowns, biblical connections, history, export tools, dark mode, and a Hebrew calendar in one portable tool.

## Key Features
- 6 script modes with proper isolation: Hebrew, Aramaic, Greek Isopsephy (including archaic letters), Latin, Roman Numerals, and English Gematria
- Real-time calculator with letter-by-letter breakdown
- Biblical connections panel for meaningful values such as Chai = 18, YHWH = 26, Elohim = 86, 153 fish, Shalom = 376, and Jesus = 888
- Persistent history with script name and safe localStorage fallback
- Export tools: copy JSON, copy CSV, and download history files
- Hebrew calendar display with date gematria
- Dark mode with persistence
- Clean parchment-inspired visual design that works offline

## Technical Foundation
The app is built as a single HTML file with vanilla HTML, CSS, and JavaScript. All datasets, meanings, mappings, and references live directly inside the file. Safe storage wrappers help avoid browser sandbox errors in restricted environments.

## Script Engine
- Hebrew: 22 letters with meanings and values
- Aramaic: full 22-letter set
- Greek: full Isopsephy support including archaic values
- Latin: A-Z sequence
- Roman: explicit Roman numeral mode to avoid overlap with Latin
- English: A = 1 through Z = 26, case-insensitive

## Study Workflow
Users can choose a script, type a word or phrase, see the running total, inspect the per-letter breakdown, review built-in biblical associations, save the study to history, and export the result set for later use.

## Vision For Physical Extension
Future phases may include QR code generation and NFC or RFID tag support so printed cards, bookmarks, or study aids can open directly into a preloaded word study with calculation, breakdown, notes, and biblical links.

## Current Status
Version 1.0 is stable and suitable for personal study, teaching demos, and small-group exploration. The app already supports serious offline use.

## Content Pillars
- Tool introductions and walkthroughs
- Deep dives into biblical numbers and words
- How-to tutorials for study workflows
- Behind-the-scenes build videos
- Physical experiments using QR and NFC study objects

## Launch Angle
This project can be positioned as a free offline biblical word study tool that blends ancient language exploration with modern design and practical study workflows.

# hackUMBC 2025 – The Phantom Check‑in

An offline CTF challenge designed to teach overlooked web application concepts through an engaging narrative.

## Overview

This CTF simulates the hackUMBC 2025 check-in process where a "phantom" entry has slipped through the system. Players must restore the check-in path by solving two interconnected puzzles that teach real-world web security and development concepts.

## Learning Objectives

- **Unicode Security**: Understanding homoglyphs, zero-width characters, and normalization
- **QR Code Generation**: Offline QR creation via canvas and data URLs
- **Fragment Routing**: Using URL fragments for client-side navigation
- **Percent Encoding**: How browsers handle special characters in URLs

## Challenge Flow

### Act I: The Map
- Interactive UMBC campus map with animated hotspots
- Narrative introduction to the phantom check-in mystery
- Learning resources and reference links

### Act II: The Phantom's Phrase (Flag 1)
- **Puzzle**: Derive and normalize a phrase containing homoglyphs and zero-width characters
- **Learning**: Unicode normalization (NFKC) and security considerations
- **Output**: Generate a QR code badge for check-in verification
- **Flag**: `HackUMBC{unicode-security-matters}`

### Act III: The Missing Link (Flag 2)
- **Puzzle**: Decode percent-encoded fragments to locate hidden repository link
- **Learning**: URL encoding, fragment routing, and client-side navigation
- **Output**: Complete the submission process
- **Flag**: `HackUMBC{fragment-routing-mastery}`

## Technical Implementation

- **Pure HTML/CSS/JavaScript**: No server required, runs entirely offline
- **Educational QR Implementation**: Simplified QR generation for learning purposes
- **Fragment-based Routing**: Demonstrates client-side navigation patterns
- **Responsive Design**: Works on desktop and mobile devices

## File Structure

```
ctf/
├── index.html          # Main map and narrative
├── checkin.html        # Flag 1: Unicode normalization + QR generation
├── viewer.html         # Flag 2: Fragment decoding
├── submit.html         # Final submission screen
├── styles/
│   └── main.css        # Shared styling and animations
├── scripts/
│   ├── normalize.js    # Unicode normalization utilities
│   └── qr-lite.js      # Educational QR implementation
└── assets/
    ├── map.svg         # Interactive UMBC campus map
    ├── puzzle-phrase.txt # Homoglyph puzzle phrase
    └── plan📝.txt      # Encoded repository link
```

## How to Run

1. Open `index.html` in any modern web browser
2. Navigate through the interactive map hotspots
3. Follow the narrative to solve both flags
4. Complete the check-in and submission process

## Educational Value

This CTF addresses concepts that are often overlooked in web development education:

- **Unicode Security**: Critical for preventing phishing and spoofing attacks
- **Client-side Routing**: Essential for modern SPAs and offline applications
- **Data Encoding**: Fundamental to web security and data integrity
- **QR Technology**: Increasingly important for mobile-first applications

## Judging Criteria Alignment

- **Creativity**: Unique narrative combining campus lore with technical concepts
- **Technical Complexity**: Multiple interconnected web technologies and security concepts
- **Impact**: Teaches practical skills applicable to real-world web development
- **Execution**: Polished UI/UX with smooth animations and clear learning progression

## References

- [Unicode Security Considerations (TR36)](https://unicode.org/reports/tr36/)
- [Unicode Normalization Forms (W3C)](https://www.w3.org/International/questions/qa-normalization)
- [WHATWG URL Standard](https://url.spec.whatwg.org/)
- [URL.hash documentation (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/URL/hash)

## License

This project is created for educational purposes as part of the hackUMBC 2025 competition.

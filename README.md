# QR Code Generator (From Scratch)

A step-by-step implementation of a QR code generator built from first principles — focusing on understanding the **math, encoding, and structure** behind QR codes rather than relying on libraries.

---

## 🚀 Project Goal

This project aims to:

* Build a QR code generator from scratch
* Understand the **mathematics behind QR codes**
* Implement key concepts like:

  * Binary encoding
  * Matrix construction
  * Zig-zag data placement
  * (Later) Error correction using Reed-Solomon

---

## 🧠 Learning Focus

This project is not just about generating QR codes — it's about understanding:

* Bit manipulation
* Finite field arithmetic (GF(256)) *(planned)*
* Polynomial operations *(planned)*
* Error correction algorithms *(planned)*
* Grid-based data representation

---

## 📁 Project Structure

```
qr_project/
│
├── main.py              # Entry point
├── encoder.py           # Converts input data → binary
├── matrix.py            # Builds QR grid and places data
│
├── gf256.py             # (Planned) Finite field operations
├── reed_solomon.py      # (Planned) Error correction
```

---

## ⚙️ Current Features (Phase 1)

* Convert input string → binary
* Pad binary data
* Create QR matrix (Version 1: 21×21)
* Add finder patterns
* Place bits using zig-zag traversal
* Render QR-like output in terminal

> ⚠️ Note: Output is **QR-like but not yet scannable**

---

## 🧩 How It Works (Current Pipeline)

```
Input Text
   ↓
Binary Encoding
   ↓
Bit Padding
   ↓
Matrix Construction
   ↓
Zig-Zag Placement
   ↓
Terminal Rendering
```

---

## ▶️ How to Run

1. Clone the repository

```
git clone <your-repo-url>
cd qr_project
```

2. Run the program

```
python main.py
```

3. Add text string in the input

```
Enter Text:"HELLO"
```

---

## 🖼️ Sample Output

```
████████      ████    ...
██    ██      ██  ██  ...
... (QR-like grid)
```

---

## 🔜 Upcoming Features

* [ ] Add timing patterns
* [ ] Implement masking
* [ ] Add GF(256) arithmetic
* [ ] Implement Reed-Solomon error correction
* [ ] Generate fully scannable QR codes
* [ ] Support multiple QR versions

---

## 🧠 Key Concepts Covered

| Concept               | Status     |
| --------------------- | ---------- |
| Binary Encoding       | ✅ Done     |
| Bit Manipulation      | ✅ Done     |
| Matrix Construction   | ✅ Done     |
| Zig-Zag Traversal     | ✅ Done     |
| GF(256) Arithmetic    | 🔜 Planned |
| Reed-Solomon Encoding | 🔜 Planned |

---

## ⚠️ Limitations (Current Version)

* Not fully QR standard compliant
* No error correction yet
* No format/version information
* May not be scannable

---

## 💡 Why This Project?

Most QR generators use libraries. This project focuses on:

* **Understanding how QR codes actually work**
* Building everything from the ground up
* Strengthening core CS concepts (DSA + math)

---

## 🚀 Future Scope

* Full QR standard compliance
* Web interface for generation
* Visualization of encoding steps
* Performance optimization

---

## 🤝 Contributing

This is a learning-focused project. Contributions, suggestions, and improvements are welcome!

---

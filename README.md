# 🦠 SneezeScape: A Distance Judgment Framework

> **Upload your group photo. We measure the closeness you had with them.**  
> *Built for pandemic nostalgia. Powered by AI. Judging you silently since 2025.*  

---

![sneezescape-banner](https://user-images.githubusercontent.com/your-image-placeholder/banner.png)

## 📷 What is SneezeScape?

**SneezeScape** is a satirical computer vision tool that analyzes how "socially distant" people were in group photos — especially during the pandemic era. Using AI-powered detection and some light math, we generate a **Distance Score** and deliver **emotional damage** through custom roast messages.

This is a *completely unnecessary* tool that nobody asked for, but everyone deserves.

---

## 🚀 Features

- 🖼 Upload any group photo  
- 🧍 Detects people using MediaPipe  
- 📏 Calculates proximity between individuals  
- 📉 Generates a Social Distance Score (0–100)  
- 🤡 Gives a judgmental roast message  
- 🖌️ Overlays boxes, lines, and violations on the photo  
- ⬇️ Download your judged image  

---

## 🛠 Tech Stack

| Component     | Tool            |
|--------------|-----------------|
| Web App      | [Streamlit](https://streamlit.io) |
| CV Library   | [OpenCV](https://opencv.org/)     |
| AI Detection | [MediaPipe](https://mediapipe.dev) |
| Language     | Python 🐍        |

---

## 📂 Folder Structure

sneezescape/
├── app.py # Streamlit app code
├── requirements.txt # Python dependencies
├── README.md # You're reading it!
├── uploads/ # Uploaded images (auto-created)
├── outputs/ # Processed output images (auto-created)


---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/sneezescape.git
cd sneezescape
pip install -r requirements.txt
streamlit run app.py

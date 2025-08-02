import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
import os
from datetime import datetime

# Setup
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

def detect_people(image):
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    people = []
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        nose = landmarks[mp_pose.PoseLandmark.NOSE]
        if nose.visibility > 0.5:
            h, w, _ = image.shape
            cx, cy = int(nose.x * w), int(nose.y * h)
            people.append((cx, cy))
    return people

def draw_boxes_and_lines(image, people):
    score = 100
    violations = 0
    threshold = 150

    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            x1, y1 = people[i]
            x2, y2 = people[j]
            dist = np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2]))
            color = (0, 255, 0) if dist >= threshold else (0, 0, 255)
            cv2.line(image, (x1, y1), (x2, y2), color, 2)
            if dist < threshold:
                violations += 1

    for x, y in people:
        cv2.rectangle(image, (x - 30, y - 100), (x + 30, y + 100), (255, 255, 0), 2)

    score = max(0, 100 - violations * 20) if len(people) > 1 else 100
    return image, score, violations

def roast_message(score, count):
    if count <= 1:
        return "Solo pic? You’re the CDC’s favorite."
    elif score >= 80:
        return "Social distancing champion 🏆"
    elif score >= 50:
        return "Mild violation. We’ll let it slide. 😷"
    elif score >= 20:
        return "That’s a sneeze away from doom. 🤧"
    else:
        return "Super spreader event confirmed. 🚨"

# Streamlit UI — upgraded
st.set_page_config(page_title="SneezeScape", layout="wide")

# Stylish title
st.markdown("""
    <div style="text-align: center;">
        <h1 style="font-size: 3em; color: #FF4B4B;">😷 SneezeScape</h1>
        <h3>A Distance Judgment Framework</h3>
        <p style="font-size: 18px;">Upload your group photo. We’ll judge your pandemic past. 🫠</p>
        <hr style="margin-top: 1rem; margin-bottom: 2rem;">
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📸 Upload your group photo", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Save upload
    img_path = f"uploads/{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    image = cv2.imread(img_path)

    # Process image
    people = detect_people(image.copy())
    processed_img, score, violations = draw_boxes_and_lines(image.copy(), people)

    # Layout: Columns for side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📷 Original")
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), use_column_width=True)
    with col2:
        st.subheader("🖌️ Judged Output")
        st.image(cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB), use_column_width=True)

    # Stylish score box
    st.markdown(f"""
    <div style="background-color:#f0f0f5; padding: 20px; border-radius: 10px; margin-top:20px;">
        <h2>🧪 Distance Score: <span style="color:#FF4B4B">{score}/100</span></h2>
        <p><strong>👥 People Detected:</strong> {len(people)}</p>
        <p><strong>⚠️ Violations:</strong> {violations}</p>
        <p style="font-size:18px;"><em>{roast_message(score, len(people))}</em></p>
    </div>
    """, unsafe_allow_html=True)

    # Download button
    output_path = img_path.replace("uploads", "outputs")
    cv2.imwrite(output_path, processed_img)
    st.download_button("⬇️ Download Judged Image", open(output_path, "rb"), file_name="sneeze_judged.jpg")

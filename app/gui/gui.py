import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading


class FaceVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Privacy-Preserving Face Verification (MVP)")
        self.root.geometry("800x600")

        # Webcam Frame
        self.video_label = tk.Label(self.root)
        self.video_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.enroll_button = ttk.Button(
            self.buttons_frame, text="Enroll User", command=self.mock_enroll
        )
        self.enroll_button.pack(side=tk.LEFT, padx=10)

        self.verify_button = ttk.Button(
            self.buttons_frame, text="Verify User", command=self.mock_verify
        )
        self.verify_button.pack(side=tk.LEFT, padx=10)

        self.message_label = tk.Label(
            self.root, text="Waiting for action...", font=("Arial", 14)
        )
        self.message_label.pack(pady=20)

        # Webcam
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.update_webcam()

    def update_webcam(self):
        if self.running:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)  # Mirror the frame
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
            self.root.after(10, self.update_webcam)

    def mock_enroll(self):
        self.message_label.config(text="[MOCK] Enrolling user...")

    def mock_verify(self):
        self.message_label.config(text="[MOCK] Verifying user...")

    def stop(self):
        self.running = False
        self.cap.release()
        self.root.quit()

import tkinter as tk

from gui.gui import FaceVerificationApp

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceVerificationApp(root)
    try:
        root.mainloop()
    finally:
        app.stop()

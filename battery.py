import tkinter as tk
import psutil
import time
from PIL import Image, ImageDraw, ImageTk

class BatteryIndicator:
    def __init__(self):
        self.display_size = 15
        self.root = tk.Tk()
        self.root.title("Battery Indicator")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)

        # Make magenta the transparent color (Windows only)
        self.root.configure(bg='magenta')
        self.root.attributes('-transparentcolor', 'magenta')

        screen_width = self.root.winfo_screenwidth()
        x = screen_width - self.display_size - 20
        y = 20
        self.root.geometry(f"{self.display_size}x{self.display_size}+{x}+{y}")

        self.canvas = tk.Canvas(self.root, width=self.display_size, height=self.display_size,
                                highlightthickness=0, bd=0, bg='magenta')
        self.canvas.pack()
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw')

        self.running = True
        self.last_power_plugged = None
        self.root.bind('<Button-3>', lambda e: self.close())
        self.update_dot()  # Start the periodic update

    def draw_indicator(self, color):
        img = Image.new('RGBA', (self.display_size, self.display_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        margin = 2
        draw.ellipse((margin, margin, self.display_size - margin, self.display_size - margin), fill=color)
        return ImageTk.PhotoImage(img)

    def update_dot(self):
        try:
            battery = psutil.sensors_battery()
            if battery is not None:
                power_plugged = battery.power_plugged
                color = '#00FF00' if power_plugged else '#808080'
            else:
                power_plugged = None
                color = '#808080'
            # Only redraw if status changed
            if power_plugged != self.last_power_plugged:
                img = self.draw_indicator(color)
                self.canvas.image = img
                self.canvas.itemconfig(self.image_on_canvas, image=img)
                self.last_power_plugged = power_plugged
        except Exception as e:
            print(f"Error: {e}")
        if self.running:
            self.root.after(2000, self.update_dot)

    def close(self):
        self.running = False
        self.root.destroy()

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.close()

if __name__ == "__main__":
    try:
        app = BatteryIndicator()
        app.run()
    except Exception as e:
        print(f"Error starting application: {e}")
        print("Make sure you have the required packages installed:")
        print("pip install psutil pillow")

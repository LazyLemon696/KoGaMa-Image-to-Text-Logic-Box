import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class KoGaMaImageToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KoGaMa Text To Image Converter")
        self.root.geometry("480x580")
        
        self.image_path = ""
        self.generated_text = ""
        
        self.main_frame = tk.Frame(self.root)
        self.settings_frame = tk.Frame(self.root)
        self.result_frame = tk.Frame(self.root)
        
        self.create_main_screen()
        self.create_settings_screen()
        self.create_result_screen()
        
        self.show_screen(self.main_frame)

    def show_screen(self, frame):
        self.main_frame.pack_forget()
        self.settings_frame.pack_forget()
        self.result_frame.pack_forget()
        frame.pack(fill="both", expand=True, padx=20, pady=20)

    def create_main_screen(self):
        lbl = tk.Label(self.main_frame, text="KoGaMa Image Converter", font=("Arial", 16, "bold"))
        lbl.pack(pady=20)
        
        btn_select = tk.Button(self.main_frame, text="Select Image (PNG, JPG, BMP)", command=self.select_image, height=2, width=30)
        btn_select.pack(pady=20)
        
        btn_credits = tk.Button(self.main_frame, text="Credits", command=self.show_credits)
        btn_credits.pack(side="bottom", pady=10)

    def select_image(self):
        file_types = [("Images", "*.png *.jpg *.jpeg *.bmp")]
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=file_types)
        if self.image_path:
            self.show_screen(self.settings_frame)

    def show_credits(self):
        messagebox.showinfo("Credits", "Made By LazyLemon (2026)")

    def create_settings_screen(self):
        tk.Label(self.settings_frame, text="Conversion Settings", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self.settings_frame, text="Fill Symbol:").pack(anchor="w", pady=2)
        self.char_entry = tk.Entry(self.settings_frame, width=5)
        self.char_entry.insert(0, "#")
        self.char_entry.pack(anchor="w", pady=5)
        
        tk.Label(self.settings_frame, text="Text Size (<size=X>):").pack(anchor="w", pady=2)
        self.size_entry = tk.Entry(self.settings_frame, width=10)
        self.size_entry.insert(0, "10")
        self.size_entry.pack(anchor="w", pady=5)
        
        self.snap_var = tk.BooleanVar()
        self.snap_chk = tk.Checkbutton(self.settings_frame, text="Snap to 256 (add ' | ' every 256 chars)", variable=self.snap_var)
        self.snap_chk.pack(anchor="w", pady=15)
        
        btn_export = tk.Button(self.settings_frame, text="Export", command=self.generate_export_screen, bg="green", fg="white", font=("Arial", 12, "bold"))
        btn_export.pack(fill="x", pady=20)

    def generate_export_screen(self):
        symbol = self.char_entry.get()
        size_val = self.size_entry.get().strip()
        
        if not symbol:
            messagebox.showerror("Error", "Please enter a symbol!")
            return
            
        try:
            size_x = int(float(size_val))
        except ValueError:
            messagebox.showerror("Error", "Size must be a valid number!")
            return

        self.scale_slider.set(100)
        self.process_conversion()
        self.show_screen(self.result_frame)

    def process_conversion(self, *args):
        symbol = self.char_entry.get()
        size_val = self.size_entry.get().strip()
        
        scale_percent = int(float(self.scale_slider.get()))
        size_x = int(float(size_val))

        try:
            img = Image.open(self.image_path).convert("RGB")
            orig_width, orig_height = img.size
            
            new_width = max(1, int(orig_width * (scale_percent / 100.0)))
            new_height = max(1, int(orig_height * (scale_percent / 100.0)))
            
            img = img.resize((new_width, new_height), Image.Resampling.NEAREST)
            pixels = img.load()
            
            result_chunks = [f"<size={size_x}>"]
            
            for y in range(new_height):
                for x in range(new_width):
                    r, g, b = pixels[x, y]
                    hex_code = f"{r:02x}{g:02x}{b:02x}"
                    result_chunks.append(f"<color=#{hex_code}>{symbol}</color>")
                result_chunks.append("\n")
            
            raw_text = "".join(result_chunks)
            
            if self.snap_var.get():
                snapped_text = ""
                for i in range(0, len(raw_text), 256):
                    if i + 256 < len(raw_text):
                        snapped_text += raw_text[i:i+256] + " | "
                    else:
                        snapped_text += raw_text[i:i+256]
                self.generated_text = snapped_text.rstrip()
            else:
                self.generated_text = raw_text
                
            self.result_textbox.delete("1.0", tk.END)
            self.result_textbox.insert("1.0", self.generated_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image:\n{e}")

    def create_result_screen(self):
        tk.Label(self.result_frame, text="Your KoGaMa Text Export:", font=("Arial", 12, "bold")).pack(pady=5)
        
        text_frame = tk.Frame(self.result_frame)
        text_frame.pack(pady=5, fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.result_textbox = tk.Text(text_frame, height=14, width=45, yscrollcommand=scrollbar.set)
        self.result_textbox.pack(side="left", fill="both", expand=True)
        
        scrollbar.config(command=self.result_textbox.yview)
        
        tk.Label(self.result_frame, text="Change Image Scale on the fly (%):").pack(anchor="w", pady=2)
        self.scale_slider = tk.Scale(self.result_frame, from_=1, to=100, orient="horizontal", command=self.process_conversion)
        self.scale_slider.pack(fill="x", pady=5)
        
        btn_frame = tk.Frame(self.result_frame)
        btn_frame.pack(fill="x", pady=10)
        
        btn_copy = tk.Button(btn_frame, text="Copy", command=self.copy_to_clipboard, width=15, bg="lightblue")
        btn_copy.pack(side="left", padx=5)
        
        btn_new = tk.Button(btn_frame, text="Generate New", command=self.generate_new, width=15)
        btn_new.pack(side="right", padx=5)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.generated_text)
        messagebox.showinfo("Success", "Code copied to clipboard!")

    def generate_new(self):
        self.image_path = ""
        self.generated_text = ""
        self.show_screen(self.main_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = KoGaMaImageToTextApp(root)
    root.mainloop()

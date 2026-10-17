# KoGaMa Image-to-Text Logic Box   

<img width="400" height="400" alt="Background (63)" src="https://github.com/user-attachments/assets/aceffd1b-e7a2-4727-b34a-43d021d016f5" />
                                                                                                                                                                                            
A lightweight desktop application that converts image files into formatted text codes specifically designed for KoGaMa logic textboxes. This tool works best with newer versions of KoGaMa that support detailed text coloring and custom font sizes.

## Features
* **Multi-format Support:** Accepts `.png`, `.jpg`, and `.bmp` image files.
* **Custom Fill Symbols:** Use any character (like `#`) to generate your pixel-art style text matrix.
* **Adjustable Text Sizing:** Automatically injects `<size=X>` tags to control how the text renders in-game.
* **Character Limit Splitting:** Optional "Snap to 256" feature inserts a delimiter (`|`) every 256 characters to easily fit within standard textbox constraints.
* **On-the-Fly Scaling:** Resize and regenerate your text export instantly using a simple slider.

---

## How to Use

### 1. Select Your Image
Launch the application and click the **Select Image (PNG, JPG, BMP)** button to upload the graphic you want to convert.

### 2. Configure Your Conversion Settings
Before exporting, customize how your text will be generated:
* **Fill Symbol:** Enter the character that will represent each "pixel" of the image.
* **Text Size:** Set the default tag size for your KoGaMa text output.
* **Snap to 256:** Check this box if you need your text broken down into chunks for easy copying into limits-capped input fields.
* Click **Export** when you are ready.

### 3. Review and Copy Your Export
* Your formatted code will appear in the output window using KoGaMa-compatible rich text tags (e.g., `<color=#ff2828>#</color>`).
* Use the **Change Image Scale on the fly (%)** slider at the bottom if you need to quickly make the output larger or smaller.
* Click **Copy** to save the code directly to your clipboard, or **Generate New** to restart the process.

---

## Compatibility
Optimized for newer versions of **KoGaMa**. Ensure your in-game logic boxes or text zones support hex style color tags before deploying long strings.

## Building

### Prerequisites
* **Python 3.8+** installed on your system.
* Required GUI framework package `Tkinter`

### 1. Setup Environment & Dependencies
Clone the repository, navigate into the project directory, and install the required tools:
```bash
git clone https://github.com
cd KoGaMa-Image-to-Text-Logic-Box
pip install pyinstaller
```

### 2. Run Directly from Source
To test the script instantly without compiling it:
```bash
kogama_converter.py
```

### 3. Compile to an Executable (.exe)
To package everything into a single standalone app that runs without needing Python installed, use **PyInstaller**:

* **For a single executable with no background command console:**
  ```bash
  pyinstaller --onefile --kogama_converter.py
  ```
* **With a custom app icon (optional):**
  ```bash
  pyinstaller --onefile --windowed --icon=app_icon.ico main.py
  ```

Once the building process completes, your finalized application will be generated inside the newly created `/dist` folder.

Made using Python 3.1.12

LazyLemon's Team (2026)

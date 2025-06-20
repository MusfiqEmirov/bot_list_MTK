# Bot List Project

This project automates browser tasks using Selenium WebDriver. It is designed to help users perform automated actions in their browser, such as scraping or testing, by controlling Chrome through chromedriver.

## Setup

1. **Clone the repository** to your local machine.
2. **Install the required dependencies** (usually via `pip install -r requirements.txt`).
3. **Download ChromeDriver** from [the official site](https://sites.google.com/chromium.org/driver/) if you do not have it already.

## Important: Set the ChromeDriver Path

You must specify the correct path to your own `chromedriver.exe` file. The project will not work unless the path is set properly. Make sure to:

- Download `chromedriver.exe` compatible with your Chrome version.
- Place it in a known directory.
- Update the script or configuration to point to the exact location of your `chromedriver.exe`.

**Example in Python:**
```python
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\path\to\your\chromedriver.exe')
```
Replace `C:\path\to\your\chromedriver.exe` with the actual path where you saved the file.

## Usage

1. Ensure all dependencies are installed and the ChromeDriver path is set correctly.
2. Run the main script (e.g., `python main.py`).
3. Follow any additional instructions provided by the script.

---

If you encounter any issues, please check that your ChromeDriver path is correct and matches your Chrome browser version.

import os
import pyautogui

# Menetapkan environment variable XAUTHORITY ke /dev/null
os.environ['XAUTHORITY'] = '/dev/null'

# Inisialisasi pyautogui
pyautogui.init()

# Fungsi untuk membuat mouse bergerak ke posisi tertentu
def move_mouse(x, y):
    pyautogui.moveTo(x, y, duration=0.5)

# Fungsi untuk mengklik mouse
def click_mouse():
    pyautogui.click()

# Fungsi untuk menggerakkan mouse relatif dari posisi saat ini
def move_mouse_relative(dx, dy):
    pyautogui.move(dx, dy, duration=0.5)

# Fungsi untuk menggeser mouse
def drag_mouse(x, y):
    pyautogui.dragTo(x, y, duration=0.5)

# Contoh penggunaan:
if __name__ == "__main__":
    # Menggerakkan mouse ke koordinat (100, 100)
    move_mouse(100, 100)

    # Klik mouse di posisi saat ini
    click_mouse()

    # Menggeser mouse ke koordinat (200, 200)
    drag_mouse(200, 200)

    # Menggerakkan mouse secara relatif sebesar 50 piksel ke kanan dan 50 piksel ke bawah dari posisi saat ini
    move_mouse_relative(50, 50)

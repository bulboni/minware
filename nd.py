import pygetwindow as gw
import pydirectinput as pdi

# Fungsi untuk membuat mouse bergerak ke posisi tertentu
def move_mouse(x, y):
    pdi.moveTo(x, y, duration=0.5)

# Fungsi untuk mengklik mouse
def click_mouse():
    pdi.click()

# Fungsi untuk menggerakkan mouse relatif dari posisi saat ini
def move_mouse_relative(dx, dy):
    pdi.moveRel(dx, dy, duration=0.5)

# Fungsi untuk menggeser mouse
def drag_mouse(x, y):
    pdi.dragTo(x, y, duration=0.5)

# Contoh penggunaan:
if __name__ == "__main__":
    # Mendapatkan window utama
    main_window = gw.getWindowsWithTitle(gw.getActiveWindow().title)[0]

    # Mendapatkan posisi tengah window
    center_x = main_window.left + main_window.width / 2
    center_y = main_window.top + main_window.height / 2

    # Menggerakkan mouse ke posisi tengah window
    move_mouse(center_x, center_y)

    # Klik mouse di posisi saat ini
    click_mouse()

    # Menggeser mouse ke koordinat (200, 200)
    drag_mouse(200, 200)

    # Menggerakkan mouse secara relatif sebesar 50 piksel ke kanan dan 50 piksel ke bawah dari posisi saat ini
    move_mouse_relative(50, 50)

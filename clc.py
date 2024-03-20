import pyautogui
import time
import random

# Rekaman gerakan mouse sebelumnya (ganti dengan rekaman Anda)
recorded_mouse_actions = [
    (580, 157, 0.5),  # Contoh: Gerakan ke koordinat (100, 200) dalam 0.5 detik
    (1020, 634, 0.5),
    (260, 729, 0.5),
    (610, 183, 0.5),
    # ... tambahkan langkah lainnya
]

# Masa aktif (86400 detik = 24 jam)
total_duration = 86400
start_time = time.time()
current_time = time.time()

while current_time - start_time < total_duration:
    random_delay = random.uniform(2, 6)  # Jeda waktu acak antara 2 hingga 6 detik
    time.sleep(random_delay)
    
    # Menemukan koordinat tengah layar
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2

    # Menambahkan langkah gerakan mouse menuju tengah layar dan melakukan klik
    recorded_mouse_actions.extend([
        (center_x, center_y, 0.5),
        # ... tambahkan langkah gerakan lainnya jika diperlukan
    ])

    # Memainkan kembali rekaman gerakan mouse
    for x, y, duration in recorded_mouse_actions:
        pyautogui.moveTo(x, y, duration=duration)
        pyautogui.doubleClick()  # Melakukan double klik pada setiap langkah
    
    # Menunggu sebentar sebelum mengulang langkah berikutnya
    time.sleep(5)
    
    current_time = time.time()

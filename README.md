
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

```bash
python3 PortScanner_1.0.py -t <hedef_ip_adresi> -sp <başlangıç_portu> -ep <bitiş_portu>
```

### Örnek:

```bash
python3 PortScanner_1.0.py -t scanme.nmap.org -sp 20 -ep 100
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

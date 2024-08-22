# **Koyun Sayımı Yapan Sistem**

Bu proje, video görüntülerinden koyunları algılayarak sayım yapan bir sistem sunar. Sistem, YOLO modeli ve Sort algoritması kullanarak her bir koyunu tanımlar ve sayar. Proje özellikle tarım ve hayvancılık sektöründe kullanılmak üzere geliştirilmiştir.

## **Özellikler**

- **Gerçek Zamanlı Koyun Algılama**: Videodaki koyunlar anlık olarak algılanır.
- **Koyun Sayımı**: Algılanan koyunlar benzersiz ID'lerle izlenir ve sayılır.
- **Maskeleme Özelliği**: İlgili bölgeyi analiz etmek için maskeleme uygulanır.
- **Kullanıcı Dostu Arayüz**: Video üzerinde koyunların ID'leri ve sayısı görüntülenir.
- **Kısa Yol Tuşları**: Kullanıcı etkileşimini kolaylaştırmak için kısa yol tuşları tanımlıdır (`q` çıkış, `s` ileri sarma, `space` duraklatma).

## **Kurulum**

1. **Gerekli Kütüphaneleri Yükleyin**:
   ```bash
   pip install ultralytics opencv-python cvzone sort numpy
Proje Dosyalarını İndirin:

bash
Kodu kopyala
git clone https://github.com/kullaniciadi/koyun-sayimi.git
Videoyu ve Model Ağırlıklarını Ekleyin: Videos klasörüne sayım yapılacak videoyu, Yolo-Weights klasörüne ise YOLO model ağırlık dosyasını ekleyin.

Sistemi Çalıştırın:

bash
Kodu kopyala
python sheep-counter2.py
Kullanım
Video Açma: cap = cv2.VideoCapture("../Videos/koy4.mp4") kodunda videonun dosya yolunu belirleyin.
Maske Uygulama: Sayım yapılacak bölgeyi belirlemek için mask dosyasını özelleştirin.
Sonuçları Görüntüleme: Çalıştırdıktan sonra koyunların sayısını ve videodaki yerleşimlerini gerçek zamanlı olarak görüntüleyin.
Ekran Görüntüleri

Sistem ekranı: Koyunların ID'leri ve sayısı görüntüleniyor.
![image](https://github.com/user-attachments/assets/e344cd53-8dc6-46f9-84bf-fdd683eebcfc)


Kullanılan Teknolojiler
YOLO Modeli: Koyunların tespiti için.
OpenCV: Görüntü işleme ve video analizi.
Sort Algoritması: Koyunları benzersiz ID'lerle izlemek için.
cvzone: Koyun tespiti ve izleme işlemlerinde görsel geliştirmeler.
Gelecek Geliştirmeler
Yüksek Performanslı Algılama: Daha büyük veritabanları ve videolar için optimizasyon.
Çoklu Video Desteği: Aynı anda birden fazla videonun analiz edilmesi.
Koyun Sağlık Takibi: Koyunların genel sağlık durumlarını analiz edebilmek için ek modüller.

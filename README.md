# Sesli Yanıt ve Metin İşleme Uygulaması

![Proje Görseli](https://i.pinimg.com/originals/e6/83/f2/e683f29e5eb2d87da457379948533a08.gif)

## Proje Açıklaması

Bu proje, sesli yanıt ve metin işleme yeteneklerine sahip bir Python uygulamasıdır. Kullanıcı sesli komutlar vererek uygulama ile etkileşimde bulunabilir ve yapay zeka destekli cevaplar alabilir. Proje, Google Generative AI API'si, Google Text-to-Speech (gTTS) ve ses tanıma teknolojilerini kullanarak kullanıcı deneyimini zenginleştirir. Uygulama, metin ve sesli yanıtları anlık olarak gösterir ve kullanıcı komutlarını gerçek zamanlı olarak işleyebilir.

## Özellikler

- **Sessiz Komut Tanıma**: Kullanıcının sesli komutlarını dinler ve metne dönüştürür.
- **Metin ve Sesli Yanıtlar**: Sesli yanıtlar oluşturur ve ekranda metin olarak gösterir.
- **Yapay Zeka Destekli İçerik Üretimi**: Google Generative AI ile kullanıcı komutlarına yanıtlar oluşturur.
- **Anlık Yazı Gösterimi**: Metin anlık olarak ekranda görüntülenir.
- **Dinamik Ses Hızı**: Sesli yanıtların hızını ayarlayarak daha hızlı veya yavaş okuma yapabilir.
- **Hata Yönetimi**: Ses tanıma hatalarını yönetir ve kullanıcıya geri bildirim sağlar.

## Teknolojiler

- **Python**: Uygulamanın ana programlama dili.
- **Google Generative AI**: Yapay zeka destekli içerik üretimi için kullanılan API.
- **gTTS (Google Text-to-Speech)**: Metni sesli yanıtlara dönüştürür.
- **pydub**: Ses dosyalarını işlemek için kullanılır.
- **speech_recognition**: Ses tanıma ve metne dönüştürme işlemlerini yapar.
- **pystyle**: Terminal çıktılarının görsel düzenini sağlar.

## Kurulum

1. **Depoyu Klonlayın**: İlk olarak projeyi yerel makinenize klonlayın.
   ```bash
   git clone https://github.com/manigasx/Voice-Ai.git
   cd Voice-Ai.git

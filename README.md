<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesli Yanıt ve Metin İşleme Uygulaması</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #bbb 1px solid;
            text-align: center;
        }
        header h1 {
            margin: 0;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        .main {
            background: #fff;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .section {
            margin-bottom: 20px;
        }
        .section h2 {
            border-bottom: 2px solid #333;
            padding-bottom: 5px;
        }
        footer {
            background: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }
        footer a {
            color: #fff;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Sesli Yanıt ve Metin İşleme Uygulaması</h1>
        </div>
    </header>

    <div class="container">
        <div class="main">
            <div class="section">
                <h2>Proje Özeti</h2>
                <p>Bu proje, sesli yanıt ve metin işleme yeteneklerine sahip bir Python uygulamasıdır. Kullanıcı sesli komutlar vererek uygulama ile etkileşimde bulunabilir ve yapay zeka destekli cevaplar alabilir. Uygulama, Google Generative AI API'si, Google Text-to-Speech (gTTS) ve ses tanıma teknolojilerini kullanarak kullanıcı deneyimini zenginleştirir.</p>
                <img src="your-image-url.jpg" alt="Proje Görseli">
            </div>

            <div class="section">
                <h2>Özellikler</h2>
                <ul>
                    <li><strong>Sessiz Komut Tanıma:</strong> Kullanıcının sesli komutlarını dinler ve metne dönüştürür.</li>
                    <li><strong>Metin ve Sesli Yanıtlar:</strong> Sesli yanıtlar oluşturur ve ekranda metin olarak gösterir.</li>
                    <li><strong>Yapay Zeka Destekli İçerik Üretimi:</strong> Google Generative AI ile kullanıcı komutlarına yanıtlar oluşturur.</li>
                    <li><strong>Anlık Yazı Gösterimi:</strong> Metin anlık olarak ekranda görüntülenir.</li>
                </ul>
            </div>

            <div class="section">
                <h2>Kurulum</h2>
                <ol>
                    <li><strong>Gerekli Paketler:</strong> Projeyi çalıştırmak için gerekli Python paketlerini yükleyin:
                        <pre><code>pip install -r requirements.txt</code></pre>
                    </li>
                    <li><strong>API Anahtarı:</strong> Google Generative AI API anahtarınızı <code>api_key</code> değişkenine atayın:
                        <pre><code>api_key = "GOOGLE_GEMİNNİ_APİ"</code></pre>
                    </li>
                </ol>
            </div>

            <div class="section">
                <h2>Kullanım</h2>
                <ol>
                    <li><strong>Proje Klasörüne Git:</strong>
                        <pre><code>cd &lt;proje_dizini&gt;</code></pre>
                    </li>
                    <li><strong>Uygulamayı Başlat:</strong>
                        <pre><code>python &lt;uygulama_dosyası&gt;.py</code></pre>
                        Uygulama başladığında, mikrofonunuza komut verin. "Çıkış" komutu verildiğinde uygulama kapanacaktır.
                    </li>
                </ol>
            </div>

            <div class="section">
                <h2>Katkıda Bulunanlar</h2>
                <p>[Adınız] - Proje geliştiricisi</p>
            </div>

            <div class="section">
                <h2>Lisans</h2>
                <p>Bu proje <a href="https://opensource.org/licenses/MIT">MIT Lisansı</a> altında lisanslanmıştır.</p>
            </div>

            <div class="section">
                <h2>İletişim</h2>
                <p>Herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen benimle iletişime geçin:</p>
                <ul>
                    <li><strong>E-posta:</strong> <a href="mailto:email@example.com">email@example.com</a></li>
                    <li><strong>GitHub:</strong> <a href="https://github.com/kullanıcı_adı">GitHub Profiliniz</a></li>
                </ul>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 [Adınız]. Tüm hakları saklıdır. <a href="https://github.com/kullanıcı_adı">GitHub</a></p>
    </footer>
</body>
</html>

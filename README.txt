GONAR PORTFOLIO PRO  (сайт для компаний и работодателей)
=========================================================
Запуск локально: start.bat (сервер на http://localhost:8780/ и открытие браузера).
Открывать index.html двойным кликом НЕ нужно: видео и шрифты требуют http-сервера.

ДИЗАЙН (одной строкой): строгий editorial/cinematic: тёплый графит и бумажный тон, один холодный акцент
(#8da2ff), Inter Tight + Instrument Serif + IBM Plex Mono для таймкодов, сетка 12 колонок, швейцарская
типографика и бегущий таймкод шоурила как фирменная деталь, потому что у видеомонтажёра первым
доказательством навыка должен быть сам кадр.

СТРУКТУРА
  index.html            страница (скелет секций)
  css/style.css         стили
  js/content.js         ВЕСЬ контент (кейсы, новости, услуги, тексты RU/EN)  <- править здесь
  js/main.js            логика: Lenis, GSAP/ScrollTrigger, курсор, переходы, RU/EN
  lib/                  gsap, ScrollTrigger, lenis (локально, сайт работает офлайн)
  fonts/                шрифты (локально)
  media/video|poster|loop|img   видео (720p), постеры (webp), hover-лупы, картинки
  tools/                скрипты сборки медиа (ffmpeg): build_media.py, build_reel.py
  screens/              скриншоты проверки

КАК ДОБАВИТЬ КЕЙС
  1) Положите видео media/video/<id>.mp4 (720p, CRF 27, пик звука не выше -6 dB),
     постер media/poster/<id>.webp, луп (4 с, без звука, 480 px) media/loop/<id>.mp4.
     Проще: допишите запись в словарь CASES (или NEWS) в tools/build_media.py и запустите
     python tools/build_media.py cases   (или news) — он сам сделает постер, луп и 720p.
  2) В js/content.js добавьте объект в CASES (вертикальные новости: в NEWS):
     { id:"myid", year:2026, ar:1.778, fmt:"16:9 · 0:30", title:{en:"",ru:""}, type:{...}, role:{...},
       tools:["After Effects"], line:{...}, brief:{...}, solution:{...} }
     ar = ширина/высота видео. Страница кейса создаётся автоматически (адрес  #/work/myid).
  Статистика в блоке «Обо мне» (10 / 8 / 2 / 2) — атрибуты data-count в index.html.

ШОУРИЛ: media/video/reel_full.mp4 (со звуком, пик -7.6 dB) и reel_bg.mp4 (фон hero, без звука).
Пересобрать: python tools/build_reel.py (список склеек вверху файла).

КАК ВЫЛОЖИТЬ
  GitHub Pages: создайте репозиторий, залейте содержимое папки в корень (index.html в корне),
    Settings -> Pages -> Deploy from branch -> main / root.
  Netlify: перетащите папку целиком на app.netlify.com/drop (сборка не нужна).
  Вес сайта см. ниже (папка целиком ~90 МБ) (видео грузятся лениво; первый экран около 2 МБ видео + шрифты ~0.7 МБ).
  Telegram-бот на сайте не публикуется. Основной контакт: https://t.me/aid99999

PDF-ПОРТФОЛИО (A4, 6 страниц, EN и RU)
  Готовые файлы: assets/docs/GONAR_Portfolio_EN.pdf и GONAR_Portfolio_RU.pdf (кнопки "Download portfolio (PDF)" на сайте
  в hero, About и Contacts подставляют файл по выбранному языку).
  Исходники: doc_src/build_pdf.py (все тексты RU/EN в словаре T внутри файла), картинки doc_src/img, HTML генерируется.
  Пересборка: python doc_src/build_pdf.py (нужен установленный Microsoft Edge, профиль пишется на D:).
  SITE_URL в build_pdf.py = https://gonar777-prog.github.io/portfolio-pro/ (стр. Selected work и контакты).
  Кейс "Furniture & Apartment Project": media/*/mebel.*, источник D:\Рабочий стол СКА\Новая папка (4)\проект мебель и квартира 14.10.24\готово прав.mp4

АРХИВ И ГАЛЕРЕЯ (все работы первого сайта)
  js/archive.js  - список видео архива (ARCH: id, категория, подписи RU/EN). Файлы: media/archive/{video,loop,poster} (хардлинки на
                   D:\Claude\portfolio_sitessets; у роликов с пиком выше -6 дБ - копия с пониженной громкостью, видео без перекодирования).
  js/gallery.js  - галерея дизайна (57 изображений, media/gallery; t_ - миниатюры). Генерируется: python tools/gen_archive_js.py
  Пересборка медиа архива: python tools/build_archive.py. Фильтры архива/галереи строятся из полей cat / c автоматически.
  Не включено: th_yasmina (клиентская обложка с человеком).

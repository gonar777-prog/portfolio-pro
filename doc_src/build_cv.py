"""GONAR — CV-portfolio for employers (no prices), in the site style.
Run:  python3 doc_src/build_cv.py        -> assets/docs/GONAR_Portfolio_{RU,EN}.pdf
Needs: pip install segno ; node with playwright (Chromium).  Texts are in T below."""
import os, html, subprocess, segno

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'assets', 'docs')
SITE = 'https://gonar777-prog.github.io/portfolio-pro/'
TG = 'https://t.me/aid99999'
FH = 'https://freelancehunt.com/freelancer/gonar.html'
MAIL = 'gonar777@gmail.com'
P = '../media/poster/'
e = html.escape


CV = os.path.join(HERE, 'cvimg')


def im(name, w=900, src='../media/poster/'):
    """jpg copy at width w (keeps the PDF light); returns a path relative to doc_src"""
    os.makedirs(CV, exist_ok=True)
    base = os.path.splitext(name)[0]
    out = os.path.join(CV, f'{base}_{w}.jpg')
    if not os.path.exists(out):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(HERE, src, name), '-vf', f'scale={w}:-2', '-q:v', '4', out], check=True)
    return f'cvimg/{base}_{w}.jpg'


def pic(n, w):
    return im(n[1:], w, '../media/img/') if n.startswith('@') else im(n, w)


def qr(url):
    q = segno.make(url, error='m')
    return q.svg_data_uri(dark='#14161b', light='#ffffff', border=2, scale=4)


# ---------------------------------------------------------------- texts
T = {
'ru': dict(
  lang='ru', doc='Портфолио · резюме 2026',
  role='Моушн-дизайнер · Видеомонтажёр · AI-видео',
  open='Ищу постоянную работу · полная занятость',
  lede='Монтаж, моушн-графика, 3D и AI-видео. Делаю ролики, которые понятны с первой секунды и которые хочется досмотреть.',
  reel='Шоурил и все работы', reel_s='Нажмите на кадр или сканируйте QR-код',
  facts=[('7+', 'лет в дизайне и видео'), ('4', 'компании в штате'), ('3', 'года в AI-видео'), ('5.0', 'рейтинг Freelancehunt')],
  c_tg='Telegram', c_mail='Email', c_site='Сайт', c_fh='Freelancehunt',
  p_h='Профиль', p_eb='01 · Обо мне',
  p_big='Один специалист на всю цепочку: от идеи и раскадровки до монтажа, моушна, звука и сдачи файлов.',
  p_txt='За 7+ лет я работал в четырёх компаниях. Три года — в AI-видео: замена лица (deepfake), липсинк и AI-озвучка. Остальное время — моушн-дизайн и монтаж для новостных и соцмедиа-каналов, рекламы, YouTube и интерьерных студий. Работаю по брендбукам и шаблонам, сдаю в срок, проекты и исходники держу в порядке.',
  dir_h='Направления', dirs=[('Новости и соцсети', 'u4.webp'), ('Реклама и промо', 'telefon.webp'), ('YouTube и обложки', '@th_missing39.webp'), ('Интерьеры и рилсы', 'remont1.webp'), ('3D и окружения', 'volcano.webp'), ('Анимация и AI', 'chaos.webp')],
  g_h='Дизайн и обложки', g_s='Превью для YouTube: крупная идея, читаемый текст, эмоция — чтобы хотелось нажать.',
  x_h='Опыт', x=[
    ('Моушн-дизайн и монтаж', '4+ года', ['Вертикальные новостные ролики по шаблонам каналов: титры, инфографика, озвучка, звук — быстрая сдача.', 'Рекламные креативы, кинетическая типографика и промо, моушн-брендинг и логотипы.', 'YouTube-каналы под ключ, обложки, анимационные истории, рилсы для интерьерных студий.']),
    ('AI-видео', '3 года', ['Замена лица (deepfake) и липсинк: подготовка исходников, генерация, доводка кадров.', 'AI-озвучка и синтез голоса, сведение с музыкой и эффектами.', 'Встраивание AI-кадров в монтаж так, чтобы результат выглядел цельно.'])],
  x_note='4 компании · полная занятость',
  l_h='Языки', langs=[('Русский', ''), ('Украинский', ''), ('Английский', 'разговорный, средний')],
  f_h='Формат', f_txt='Постоянная работа, полная занятость. Готов к тестовому заданию.',
  s_h='Навыки', s_eb='02 · Инструменты',
  s_groups=[('Основное', ['After Effects', 'Premiere Pro', 'Photoshop', 'Моушн-дизайн и типографика', 'Монтаж и цветокоррекция']),
            ('3D и AI', ['Blender', 'Stable Diffusion · ComfyUI', 'Deepfake · липсинк', 'ElevenLabs (голос)', 'Апскейл · Real-ESRGAN']),
            ('Плюс', ['Звуковой дизайн и сведение', 'Субтитры · Whisper', 'Remotion (моушн в коде)', 'FFmpeg', 'Обложки для YouTube'])],
  st_h='Сильные стороны', st=[('Ритм', 'Монтаж и анимация попадают в бит и в смысл фразы.'), ('Скорость', 'Новостной формат приучил сдавать быстро и без ошибок.'), ('Диапазон', 'Новости, реклама, 3D, анимация и AI — в одном человеке.'), ('Порядок', 'Брендбук, шаблоны, форматы и чистые проекты.')],
  w_h='Избранные работы', w_eb='03 · Работы', w_s='Нажмите на кадр, чтобы открыть видео на сайте.',
  role_l='Роль', task_l='Задача', sol_l='Решение',
  news_h='Новостные шортсы', news_s='Вертикальные ролики 9:16 для каналов UNN и TEZA: шаблон заголовка, инфографика, озвучка и звук, до 30 секунд.',
  r_h='Отзывы', r_eb='04 · Отзывы', r_s='Реальные отзывы заказчиков с Freelancehunt. Все оценки — 5.0.',
  end_h='Давайте работать вместе', end_s='Быстрее всего ответ в Telegram. Готов к собеседованию и тестовому заданию.',
  q_site='Сайт-портфолио', q_tg='Telegram',
  works=[
    ('sylar', 'Portfolio_Sylar_TG.webp', True, 'Портфолио Sylar TG', '9:16 · 0:20', 'Идея, моушн, 3D, титры, звук', 'Моушн-визитка, которую видно сразу: 20 секунд под трек.', '3D-космос, голограммные титры и переходы точно в бит музыки.'),
    ('intro', 'GONAR_intro.webp', False, 'Заставка GONAR', '16:9 · 0:20 · петля', 'Идея, 3D, моушн', 'Зацикленная заставка для сайта, в которой видно все работы.', 'Камера облетает плёнку с моими роликами; голограммный глитч и печать в стиле DOS.'),
    ('soobshenie', 'soobshenie.webp', False, 'Сообщение от меня', '16:9 · 2:39', 'Сюжет, анимация, озвучка, звук, монтаж', 'Удержать внимание почти три минуты простой плоской графикой.', 'Ритм по репликам, субтитры точно по звуку, напряжение держит звуковой дизайн.'),
    ('marshrut0', 'marshrut0.webp', False, 'Маршрут 0', '16:9 · 2:56', 'Анимация, типографика, звук, монтаж', 'Тихая тревожная история, читаемая с первого взгляда.', 'Сильные одно-кадровые сцены, читаемые титры, сдержанный звук.'),
    ('volcano', 'volcano.webp', False, 'Volcanic Valley', '16:9 · 0:30', '3D, свет, камера, рендер', 'Кинематографичное окружение без рендер-фермы.', 'Рельеф, лава, частицы и небо созданы процедурно в Blender.'),
    ('chaos', 'chaos.webp', False, 'Chaos Reality · 2.5D', '16:9 · 0:09', 'Арт-дирекшн, анимация, звук', 'Недорогой и мгновенно читаемый стиль для канала.', 'AI-персонажи разложены по слоям и анимированы в 2.5D, эффекты на битах.'),
    ('mebel', 'mebel.webp', True, 'Мебель и квартира', '9:16 · 0:52', 'Монтаж, композитинг, переходы', 'Показать дизайн-проект до реализации в формате для соцсетей.', 'Переходы взмахом руки превращают стройку в готовые комнаты.'),
    ('telefon', 'telefon.webp', False, 'Телефон · кинетическое промо', '1:1 · 0:09', 'Моушн-дизайн, типографика', 'Квадратный ролик, который останавливает ленту.', 'Один объект, несколько слов, ритм от склеек.')],
  reviews=[('Видеомонтаж анимации + логотип', 'Супер якісне виконання проекту, максимальна лояльність та професіоналізм зі сторони виконавця. Однозначно звернемось ще, неодноразово. Задоволені на 100%.'),
           ('Видеокреатив', 'Роботою задоволений на всі 1000%. Завжди був на зв’язку, відповідав практично миттєво. Була одна правка, і та несуттєва — виконав протягом години.'),
           ('Трекинг объекта в After Effects', 'Відмінний майстер, все зробив дуже швидко і якісно, можете на нього покластися при будь-яких завданнях.'),
           ('Ретушь и обработка изображений', 'Хоча моє ТЗ було сформовано не надто чітко, він швидко уточнив усю необхідну інформацію та якісно виконав завдання. 10/10.')],
),
'en': dict(
  lang='en', doc='Portfolio · CV 2026',
  role='Motion Designer · Video Editor · AI Video',
  open='Open to a full-time position',
  lede='Editing, motion graphics, 3D and AI video. I make videos that are clear from the first second and worth watching to the end.',
  reel='Showreel and all work', reel_s='Click the frame or scan the QR code',
  facts=[('7+', 'years in design and video'), ('4', 'companies, in-house'), ('3', 'years in AI video'), ('5.0', 'Freelancehunt rating')],
  c_tg='Telegram', c_mail='Email', c_site='Website', c_fh='Freelancehunt',
  p_h='Profile', p_eb='01 · About',
  p_big='One person for the whole chain: from idea and storyboard to edit, motion, sound and delivery.',
  p_txt='Over 7+ years I have worked at four companies. Three years were in AI video: face replacement (deepfake), lip-sync and AI voice-over. The rest was motion design and editing for news and social channels, advertising, YouTube and interior studios. I work to brand guides and templates, deliver on time and keep projects and source files tidy.',
  dir_h='Fields', dirs=[('News & social', 'u4.webp'), ('Ads & promos', 'telefon.webp'), ('YouTube & thumbnails', '@th_missing39.webp'), ('Interiors & Reels', 'remont1.webp'), ('3D environments', 'volcano.webp'), ('Animation & AI', 'chaos.webp')],
  g_h='Design & thumbnails', g_s='YouTube thumbnails: one big idea, readable text and emotion that makes people click.',
  x_h='Experience', x=[
    ('Motion design & editing', '4+ years', ['Vertical news videos on channel templates: titles, data graphics, voice-over and sound, fast turnaround.', 'Ad creatives, kinetic typography and promos, motion branding and logos.', 'Full YouTube channel production, thumbnails, animated stories, Reels for interior studios.']),
    ('AI video', '3 years', ['Face replacement (deepfake) and lip-sync: source prep, generation, shot clean-up.', 'AI voice-over and voice synthesis, mixed with music and effects.', 'Blending AI shots into the edit so the result feels seamless.'])],
  x_note='4 companies · full-time',
  l_h='Languages', langs=[('Russian', ''), ('Ukrainian', ''), ('English', 'conversational, intermediate')],
  f_h='Availability', f_txt='Full-time position. Happy to do a test task.',
  s_h='Skills', s_eb='02 · Tools',
  s_groups=[('Core', ['After Effects', 'Premiere Pro', 'Photoshop', 'Motion design & typography', 'Editing & colour']),
            ('3D & AI', ['Blender', 'Stable Diffusion · ComfyUI', 'Deepfake · lip-sync', 'ElevenLabs (voice)', 'Upscaling · Real-ESRGAN']),
            ('Plus', ['Sound design & mixing', 'Subtitles · Whisper', 'Remotion (motion in code)', 'FFmpeg', 'YouTube thumbnails'])],
  st_h='Strengths', st=[('Rhythm', 'Cuts and animation land on the beat and on the meaning.'), ('Speed', 'News work taught me to deliver fast and clean.'), ('Range', 'News, ads, 3D, animation and AI in one person.'), ('Order', 'Brand guides, templates, formats and clean projects.')],
  w_h='Selected work', w_eb='03 · Work', w_s='Click a frame to open the video on the website.',
  role_l='Role', task_l='Task', sol_l='Approach',
  news_h='News shorts', news_s='Vertical 9:16 edits for the UNN and TEZA channels: headline template, data call-outs, voice-over and sound, under 30 seconds.',
  r_h='Reviews', r_eb='04 · Reviews', r_s='Real client reviews from Freelancehunt. Every rating is 5.0.',
  end_h='Let’s work together', end_s='Telegram gets the fastest reply. Ready for an interview and a test task.',
  q_site='Portfolio website', q_tg='Telegram',
  works=[
    ('sylar', 'Portfolio_Sylar_TG.webp', True, 'Portfolio Sylar TG', '9:16 · 0:20', 'Idea, motion, 3D, titles, sound', 'A motion business card that grabs attention: 20 seconds to a track.', '3D space, hologram titles and transitions locked to the beat.'),
    ('intro', 'GONAR_intro.webp', False, 'GONAR intro', '16:9 · 0:20 · loop', 'Idea, 3D, motion', 'A looping website intro that shows all my work at once.', 'The camera orbits a film strip playing my videos; hologram glitch and DOS-style typing.'),
    ('soobshenie', 'soobshenie.webp', False, 'Message From Me', '16:9 · 2:39', 'Story, animation, voice, sound, edit', 'Hold attention for almost three minutes with flat illustration.', 'Paced line by line, subtitles timed to audio, sound carries the tension.'),
    ('marshrut0', 'marshrut0.webp', False, 'Route 0', '16:9 · 2:56', 'Animation, typography, sound, edit', 'A quiet, eerie story readable at a glance.', 'Strong single-image scenes, legible captions, restrained sound.'),
    ('volcano', 'volcano.webp', False, 'Volcanic Valley', '16:9 · 0:30', '3D, lighting, camera, render', 'A cinematic environment without a render farm.', 'Terrain, lava, particles and sky built procedurally in Blender.'),
    ('chaos', 'chaos.webp', False, 'Chaos Reality · 2.5D', '16:9 · 0:09', 'Art direction, animation, sound', 'A cheap, instantly readable look for a channel.', 'AI characters split into layers and animated in 2.5D, effects on the beats.'),
    ('mebel', 'mebel.webp', True, 'Furniture & Apartment', '9:16 · 0:52', 'Edit, compositing, transitions', 'Show a design project before it is built, made for social media.', 'Hand-swipe transitions turn the building site into finished rooms.'),
    ('telefon', 'telefon.webp', False, 'Phone · Kinetic Promo', '1:1 · 0:09', 'Motion design, typography', 'A square promo that stops the scroll.', 'One object, a few words, rhythm from the cuts.')],
  reviews=[('Animation edit + logo', 'Super high-quality work, maximum loyalty and professionalism. We will definitely come back, more than once. 100% satisfied.'),
           ('Video creative', '1000% happy. Always in touch and replied almost instantly. There was one minor revision, done within an hour.'),
           ('Object tracking in After Effects', 'An excellent pro: everything done fast and well. You can rely on him for any task.'),
           ('Image retouching', 'My brief wasn’t very clear, but he quickly clarified everything and delivered. A hard, very detailed job. 10/10.')],
),
}

THUMBS = ['th_missing39', 'thumb_alive', 'th_9effects', 'th_archaeology', 'th_firefly', 'th_skater']
NEWS = ['u4', 'u3', 'tz3', 'n1', 'u2', 'n12']

CSS = r"""
@import url(../fonts/fonts.css);
@font-face{font-family:Oswald;font-weight:500;src:url(../fonts/oswald-latin-500.woff2)}
@font-face{font-family:Oswald;font-weight:600;src:url(../fonts/oswald-latin-600.woff2)}
@font-face{font-family:Oswald;font-weight:700;src:url(../fonts/oswald-latin-700.woff2)}
@font-face{font-family:Oswald;font-weight:500;src:url(../fonts/oswald-cyr-500.woff2);unicode-range:U+0400-04FF}
@font-face{font-family:Oswald;font-weight:600;src:url(../fonts/oswald-cyr-600.woff2);unicode-range:U+0400-04FF}
@font-face{font-family:Oswald;font-weight:700;src:url(../fonts/oswald-cyr-700.woff2);unicode-range:U+0400-04FF}
@page{size:A4;margin:0}
:root{--ink:#14161b;--ink2:#1b1e25;--card:#20242c;--line:#2e333d;--paper:#e9ecef;--mut:#9aa3ad;--acc:#4fd1c5;--amb:#f2b544}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--ink)}
body{color:var(--paper);font:400 10pt/1.5 'Inter Tight',system-ui,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
a{color:inherit;text-decoration:none}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;padding:14mm 15mm 12mm;page-break-after:always;background:var(--ink);display:flex;flex-direction:column}
.page:last-child{page-break-after:auto}
.top{display:flex;justify-content:space-between;align-items:center;font:500 7.5pt/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);padding-bottom:5mm;border-bottom:1px solid var(--line);margin-bottom:9mm}
.top b{color:var(--paper);font:600 11pt/1 Oswald;letter-spacing:.06em;display:flex;align-items:center;gap:2.5mm}
.top img{width:7mm;height:7mm}
.eb{font:500 7.5pt/1 'IBM Plex Mono',monospace;letter-spacing:.18em;text-transform:uppercase;color:var(--amb);margin-bottom:3mm}
h1,h2,h3{font-family:Oswald;text-transform:uppercase;letter-spacing:.01em;line-height:1}
h2{font-weight:600;font-size:30pt;margin-bottom:6mm}
h3{font-weight:600;font-size:12pt;letter-spacing:.04em;margin-bottom:3mm}
.acc{color:var(--acc)}
.mut{color:var(--mut)}
.film{height:5mm;margin:6mm 0;background:repeating-linear-gradient(90deg,transparent 0 3mm,var(--line) 3mm 6mm);-webkit-mask:linear-gradient(#000 0 1mm,transparent 1mm 4mm,#000 4mm)}
.foot{margin-top:auto;padding-top:4mm;border-top:1px solid var(--line);display:flex;justify-content:space-between;font:500 7pt/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}
/* cover */
.cover .name{font:700 92pt/.86 Oswald;letter-spacing:-.005em;margin:2mm 0 4mm}
.cover .role{font:500 14pt/1.2 Oswald;text-transform:uppercase;letter-spacing:.05em;color:var(--acc)}
.cover .open{display:inline-flex;align-items:center;gap:2mm;margin:6mm 0 4mm;padding:2.2mm 3.5mm;border:1px solid var(--amb);color:var(--amb);font:500 8pt/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase}
.cover .open i{width:2mm;height:2mm;border-radius:50%;background:var(--amb)}
.cover .lede{font-size:11pt;max-width:150mm;color:#cfd5db}
.reel{display:grid;grid-template-columns:1fr 38mm;gap:5mm;margin-top:8mm;align-items:stretch}
.reel .shot{position:relative;display:block;aspect-ratio:16/9;border:1px solid var(--line);overflow:hidden}
.reel .shot img{width:100%;height:100%;object-fit:cover;display:block}
.play{position:absolute;left:50%;top:50%;width:16mm;height:16mm;margin:-8mm 0 0 -8mm;border-radius:50%;background:rgba(20,22,27,.55);border:1.5px solid var(--acc);display:grid;place-items:center}
.play:after{content:'';margin-left:1.2mm;border-left:5mm solid var(--acc);border-top:3mm solid transparent;border-bottom:3mm solid transparent}
.reel .tag{position:absolute;left:3mm;bottom:3mm;font:500 7pt/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase;background:var(--acc);color:var(--ink);padding:1.6mm 2.4mm}
.qr{display:flex;flex-direction:column;gap:2.5mm;justify-content:flex-end}
.qr img{width:38mm;height:38mm;display:block;border-radius:1.5mm}
.qr span{font:500 7pt/1.35 'IBM Plex Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--mut)}
.qr b{font:600 10pt/1.1 Oswald;letter-spacing:.04em;text-transform:uppercase;color:var(--paper)}
.facts{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-top:8mm}
.facts div{padding:4.5mm 3mm 4mm 0}
.facts div+div{padding-left:4mm;border-left:1px solid var(--line)}
.facts b{display:block;font:600 26pt/1 Oswald;color:var(--paper)}
.facts b em{font-style:normal;color:var(--amb);font-size:16pt;margin-left:.6mm}
.facts span{font-size:8pt;color:var(--mut)}
.contacts{display:grid;grid-template-columns:repeat(4,auto);gap:2mm 8mm;margin-top:7mm;justify-content:start}
.contacts div span{display:block;font:500 6.5pt/1 'IBM Plex Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--amb);margin-bottom:1.6mm}
.contacts a{font-size:9.5pt}
/* hero bg */
.hbg{position:absolute;left:0;right:0;top:0;height:150mm;background-size:cover;background-position:center 60%;opacity:.55}
.hbg:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,22,27,.55) 0%,rgba(20,22,27,.25) 35%,rgba(20,22,27,.85) 75%,var(--ink) 100%),linear-gradient(90deg,rgba(20,22,27,.9),rgba(20,22,27,0) 70%)}
.cover>*:not(.hbg){position:relative}
.cover .name{font-size:112pt}
.dirs{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm}
.dirs div{position:relative;aspect-ratio:4/5;overflow:hidden;border:1px solid var(--line)}
.dirs img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.9) brightness(.8)}
.dirs span{position:absolute;left:0;right:0;bottom:0;padding:6mm 2.5mm 2.5mm;background:linear-gradient(transparent,rgba(12,13,16,.95));font:600 8.5pt/1.1 Oswald;text-transform:uppercase;letter-spacing:.03em}
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.gal a{display:block;aspect-ratio:16/9;overflow:hidden;border:1px solid var(--line)}
.gal img{width:100%;height:100%;object-fit:cover;display:block}
/* profile */
.big{font:500 17pt/1.22 Oswald;text-transform:uppercase;letter-spacing:.01em;margin-bottom:5mm}
.big em{font-style:normal;color:var(--acc)}
.txt{color:#cfd5db;font-size:10pt;max-width:175mm}
.xp{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:3mm}
.xc{background:var(--ink2);border:1px solid var(--line);padding:5mm}
.xc .hd{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3mm}
.xc .hd h3{margin:0;color:var(--paper)}
.xc .hd span{font:500 8pt/1 'IBM Plex Mono',monospace;color:var(--amb);letter-spacing:.1em;text-transform:uppercase}
.xc li{list-style:none;position:relative;padding-left:4mm;font-size:9pt;color:#cfd5db;margin-bottom:1.8mm}
.xc li:before{content:'';position:absolute;left:0;top:2mm;width:2mm;height:1px;background:var(--acc)}
.row3{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:5mm}
.box{border-top:1px solid var(--line);padding-top:4mm}
.lang{display:flex;justify-content:space-between;font-size:10pt;padding:1.6mm 0;border-bottom:1px dashed var(--line)}
.lang span{color:var(--mut);font-size:8.5pt}
/* skills */
.sk{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.sk ul{list-style:none}
.sk li{padding:1.5mm 0;border-bottom:1px solid var(--line);font-size:10pt}
.sk h3{color:var(--acc);border-bottom:1.5px solid var(--acc);padding-bottom:2.5mm;margin-bottom:0}
.str{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:1mm}
.str div{background:var(--ink2);border:1px solid var(--line);padding:3.2mm 4mm}
.str b{display:block;font:600 12pt/1 Oswald;text-transform:uppercase;letter-spacing:.04em;color:var(--amb);margin-bottom:2mm}
.str span{font-size:9pt;color:#cfd5db}
/* works */
.wk{display:grid;grid-template-columns:1fr 1fr;gap:5mm 5mm}
.w{background:var(--ink2);border:1px solid var(--line);display:flex;flex-direction:column}
.w .im{position:relative;display:block;aspect-ratio:16/9;overflow:hidden;background:#000}
.w .im img{width:100%;height:100%;object-fit:cover;display:block}
.w .im.v img{object-fit:contain;background:#0b0c0f}
.w .im .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(8px) brightness(.45);transform:scale(1.15)}
.w .im .fg{position:relative}
.w .im .play{width:10mm;height:10mm;margin:-5mm 0 0 -5mm}
.w .im .play:after{border-left-width:3.4mm;border-top-width:2.1mm;border-bottom-width:2.1mm;margin-left:.9mm}
.w .bd{padding:3.5mm 4mm 4mm}
.w .t{display:flex;justify-content:space-between;align-items:baseline;gap:3mm;margin-bottom:2mm}
.w .t h3{margin:0;font-size:11.5pt}
.w .t span{font:500 6.8pt/1 'IBM Plex Mono',monospace;color:var(--mut);letter-spacing:.08em;white-space:nowrap}
.w p{font-size:8.2pt;color:#c4cbd2;line-height:1.42;margin-top:1mm}
.w p b{font:500 6.6pt/1 'IBM Plex Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--amb);margin-right:1.5mm}
.news{display:grid;grid-template-columns:1.25fr repeat(6,1fr);gap:3mm;margin-top:6mm;align-items:end}
.news .h h3{margin-bottom:2mm}
.news .h p{font-size:8.2pt;color:#c4cbd2}
.news a{display:block;aspect-ratio:9/16;overflow:hidden;border:1px solid var(--line)}
.news img{width:100%;height:100%;object-fit:cover;display:block}
/* reviews + end */
.rv{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.rv div{background:var(--ink2);border:1px solid var(--line);padding:5mm;position:relative}
.rv .st{color:var(--amb);letter-spacing:1mm;font-size:9pt}
.rv q{display:block;font-size:9.3pt;line-height:1.45;color:#dfe4e8;margin:2.5mm 0 3mm;quotes:'“' '”'}
.rv span{font:500 6.8pt/1 'IBM Plex Mono',monospace;color:var(--mut);letter-spacing:.12em;text-transform:uppercase}
.end{margin-top:9mm;padding:8mm;background:var(--ink2);border:1px solid var(--line);display:grid;grid-template-columns:1fr auto auto;gap:7mm;align-items:end}
.end h2{font-size:26pt;margin-bottom:3mm}
.end .tg{font:600 24pt/1 Oswald;color:var(--acc);display:block;margin:4mm 0 4mm}
.end ul{list-style:none;font-size:9pt}
.end li{padding:1.2mm 0;color:#cfd5db}
.end li span{display:inline-block;width:27mm;font:500 6.6pt/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--amb)}
.end .qr img{width:32mm;height:32mm}
"""


def page(cls, t, n, label, body):
    return f'''<section class="page {cls}">
<div class="top"><b><img src="../media/img/GONAR_mark.svg" alt="">GONAR</b><span>{e(label)} · {n}/6</span></div>
{body}
<div class="foot"><span>GONAR · {e(t['role'])}</span><span>gonar777-prog.github.io/portfolio-pro</span></div>
</section>'''


def work(t, w):
    wid, img, vert, title, fmt, role, task, sol = w
    href = SITE + (f'#/work/{wid}' if wid not in ('sylar', 'intro') else '')
    src = im(img, 640)
    pic = (f'<img class="bg" src="{im(img, 200)}" alt=""><img class="fg" src="{src}" alt="">' if vert else f'<img src="{src}" alt="">')
    return f'''<div class="w"><a class="im{' v' if vert else ''}" href="{href}">{pic}<i class="play"></i></a>
<div class="bd"><div class="t"><h3><a href="{href}">{e(title)} ↗</a></h3><span>{e(fmt)}</span></div>
<p><b>{e(t['role_l'])}</b>{e(role)}</p><p><b>{e(t['task_l'])}</b>{e(task)}</p><p><b>{e(t['sol_l'])}</b>{e(sol)}</p></div></div>'''


def build(L):
    t = T[L]
    facts = ''.join(f'<div><b>{n.replace("+", "<em>+</em>").replace("5.0", "5.0<em>★</em>")}</b><span>{e(s)}</span></div>' for n, s in t['facts'])
    cover = f'''<section class="page cover"><div class="hbg" style="background-image:url({im('volcano.webp', 1400)})"></div>
<div class="top"><b><img src="../media/img/GONAR_mark.svg" alt="">GONAR</b><span>{e(t['doc'])}</span></div>
<div class="eb">{e(t['doc'])}</div>
<h1 class="name">GONAR</h1>
<div class="role">{e(t['role'])}</div>
<div><span class="open"><i></i>{e(t['open'])}</span></div>
<p class="lede">{e(t['lede'])}</p>
<div class="reel"><a class="shot" href="{SITE}"><img src="{im('GONAR_intro.webp', 1200)}" alt=""><i class="play"></i><span class="tag">Showreel ▶</span></a>
<div class="qr"><img src="{qr(SITE)}" alt=""><b>{e(t['reel'])}</b><span>{e(t['reel_s'])}</span></div></div>
<div class="facts">{facts}</div>
<div class="contacts"><div><span>{t['c_tg']}</span><a href="{TG}">@aid99999</a></div><div><span>{t['c_mail']}</span><a href="mailto:{MAIL}">{MAIL}</a></div><div><span>{t['c_site']}</span><a href="{SITE}">gonar777-prog.github.io/portfolio-pro</a></div><div><span>{t['c_fh']}</span><a href="{FH}">freelancehunt.com/freelancer/gonar</a></div></div>
<div class="foot"><span>GONAR · 2026</span><span>1/6</span></div>
</section>'''
    xp = ''.join(f'<div class="xc"><div class="hd"><h3>{e(h)}</h3><span>{e(y)}</span></div><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>' for h, y, items in t['x'])
    langs = ''.join(f'<div class="lang">{e(a)}<span>{e(b)}</span></div>' for a, b in t['langs'])
    big = e(t['p_big'])
    dirs = ''.join(f'<div><img src="{pic(n, 400)}" alt=""><span>{e(l)}</span></div>' for l, n in t['dirs'])
    prof = page('', t, 2, t['p_h'], f'''<div class="eb">{e(t['p_eb'])}</div><h2>{e(t['p_h'])}</h2>
<p class="big">{big}</p><p class="txt">{e(t['p_txt'])}</p>
<div class="film"></div>
<div style="display:flex;justify-content:space-between;align-items:baseline"><h3>{e(t['x_h'])}</h3><span class="eb" style="margin:0">{e(t['x_note'])}</span></div>
<div class="xp">{xp}</div>
<div class="row3"><div class="box"><h3>{e(t['l_h'])}</h3>{langs}</div><div class="box"><h3>{e(t['f_h'])}</h3><p class="txt">{e(t['f_txt'])}</p></div></div>
<h3 style="margin-top:5mm">{e(t['dir_h'])}</h3><div class="dirs">{dirs}</div>''')
    sk = ''.join(f'<div><h3>{e(h)}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>' for h, items in t['s_groups'])
    st = ''.join(f'<div><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in t['st'])
    gal = ''.join(f'<a href="{SITE}#gallery"><img src="{im(n + ".webp", 600, "../media/img/")}" alt=""></a>' for n in THUMBS)
    skills = page('', t, 3, t['s_h'], f'''<div class="eb">{e(t['s_eb'])}</div><h2>{e(t['s_h'])}</h2>
<div class="sk">{sk}</div><div class="film"></div><h3>{e(t['st_h'])}</h3><div class="str">{st}</div>
<div class="film"></div><div style="display:flex;justify-content:space-between;align-items:baseline;gap:8mm"><h3>{e(t['g_h'])}</h3><p class="mut" style="font-size:8.5pt;text-align:right">{e(t['g_s'])}</p></div>
<div class="gal">{gal}</div>''')
    W = t['works']
    w1 = page('', t, 4, t['w_h'], f'''<div class="eb">{e(t['w_eb'])}</div><h2>{e(t['w_h'])}</h2><p class="mut" style="margin:-3mm 0 5mm;font-size:9pt">{e(t['w_s'])}</p>
<div class="wk">{''.join(work(t, w) for w in W[:4])}</div>''')
    news = ''.join(f'<a href="{SITE}#shorts"><img src="{im(n + '.webp', 260)}" alt=""></a>' for n in NEWS)
    w2 = page('', t, 5, t['w_h'], f'''<div class="wk">{''.join(work(t, w) for w in W[4:8])}</div>
<div class="news"><div class="h"><h3>{e(t['news_h'])}</h3><p>{e(t['news_s'])}</p></div>{news}</div>''')
    rv = ''.join(f'<div><span class="st">★★★★★</span><q>{e(q)}</q><span>{e(tag)}</span></div>' for tag, q in t['reviews'])
    end = page('', t, 6, t['r_h'], f'''<div class="eb">{e(t['r_eb'])}</div><h2>{e(t['r_h'])}</h2><p class="mut" style="margin:-3mm 0 5mm;font-size:9pt">{e(t['r_s'])} <a class="acc" href="{FH}">Freelancehunt →</a></p>
<div class="rv">{rv}</div>
<div class="end"><div><h2>{e(t['end_h'])}</h2><p class="mut" style="font-size:9pt">{e(t['end_s'])}</p><a class="tg" href="{TG}">@aid99999</a>
<ul><li><span>{t['c_mail']}</span><a href="mailto:{MAIL}">{MAIL}</a></li><li><span>{t['c_site']}</span><a href="{SITE}">gonar777-prog.github.io/portfolio-pro</a></li><li><span>{t['c_fh']}</span><a href="{FH}">freelancehunt.com/freelancer/gonar</a></li></ul></div>
<div class="qr"><img src="{qr(SITE)}" alt=""><span>{e(t['q_site'])}</span></div>
<div class="qr"><img src="{qr(TG)}" alt=""><span>{e(t['q_tg'])}</span></div></div>''')
    doc = f'''<!doctype html><html lang="{t['lang']}"><head><meta charset="utf-8"><title>GONAR — {e(t['doc'])}</title><style>{CSS}</style></head>
<body>{cover}{prof}{skills}{w1}{w2}{end}</body></html>'''
    path = os.path.join(HERE, f'cv_{L}.html')
    open(path, 'w', encoding='utf-8').write(doc)
    return path


if __name__ == '__main__':
    js = os.path.join(HERE, 'print_pdf.js')
    for L in ('ru', 'en'):
        src = build(L)
        out = os.path.join(OUT, f'GONAR_Portfolio_{L.upper()}.pdf')
        subprocess.run(['node', js, src, out], check=True)
        print('wrote', out)

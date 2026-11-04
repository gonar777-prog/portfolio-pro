"""Сборка PDF-портфолио: python build_pdf.py  -> ../assets/docs/GONAR_Portfolio_{EN,RU}.pdf
Только Edge/Chrome headless (профиль на D:). Тексты - в словаре T ниже."""
import subprocess, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'assets', 'docs')
os.makedirs(OUT, exist_ok=True)
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
SITE_URL = 'https://gonar777-prog.github.io/portfolio-pro/'

M = 'img/'
T = {
'en': dict(
 role='Video Editor · Motion Designer · Creative Producer', years='7+ years in design',
 cover_sub='Cinematic storytelling, motion graphics, news and social video, AI-assisted pipelines.',
 contact_lbl='Contact', portfolio='Portfolio', year='2026',
 p_h='Profile',
 p_big='I turn ideas into video that is clear on the first second and worth finishing.',
 p_txt=['Seven years in design have taken me through studios and teams working on very different subjects: news and social channels, advertising, YouTube, interiors, e-commerce and animation.',
        'I handle the whole chain: concept and storyboard, editing, motion graphics, sound, thumbnails and delivery. I use AI tools where they save time, and keep timing, taste and final sound in my own hands.',
        'For studios and brands that means one reliable person who understands formats, templates and brand rules, and delivers files as agreed.'],
 pv=[('Range','Comfortable in very different genres and visual languages.'),('Pipeline','From script to finished file, with AI-assisted tools where they help.'),('Reliability','Briefs, templates and formats are respected; deliveries are clean.')],
 s_h='Tools I work with',
 sk=[('Editing & motion',['After Effects','Premiere Pro','Remotion (motion in code)','Titles & subtitles','Colour correction']),
     ('3D',['Blender','Procedural environments','Lighting & render']),
     ('Image & design',['Photoshop','YouTube thumbnails','Retouch & compositing','E-commerce infographics']),
     ('AI & sound',['ComfyUI / Stable Diffusion','Whisper · Real-ESRGAN','ElevenLabs (voice, effects)','Sound design & mix','FFmpeg'])],
 e_h='Experience by field',
 ex=[('News & social channels','Vertical news shorts built to channel templates, with voice-over and sound, delivered fast.','u4.webp'),
     ('Advertising & creatives','Square and vertical ad creatives, kinetic typography and product promos.','telefon.webp'),
     ('YouTube channels & thumbnails','Whole-channel production plus high-contrast covers designed to be clicked.','th_missing39.webp'),
     ('Furniture & interiors','Reveal reels that turn a construction site into the finished design.','mebel.webp'),
     ('E-commerce infographics','Product cards and infographics for marketplaces.','bag1.webp'),
     ('3D & AI animation','Blender environments, 2.5D comic animation and AI-assisted pipelines.','chaos.webp'),
     ('Animated stories','Script, voice, animation and sound for long-form mystery stories.','soobshenie.webp')],
 w_h='Selected work',
 w_s='Eight of eleven projects on the portfolio site. Video, case notes and the latest work are online.',
 works=[('soobshenie','Message From Me','Animated story · 2:39'),('volcano','Volcanic Valley','3D environment · Blender'),('chaos','Chaos Reality','2.5D style test'),('marshrut0','Route 0','Animated story · 2:56'),
        ('mebel','Furniture & Apartment','Interior reveal · 9:16'),('remont1','Renovation Studio','Social reel · 9:16'),('u4','Energy attack report','News short · UNN'),('tz3','Drone attack report','News short · TEZA')],
 sv_h='Services', sv=['Editing, reels and dynamic videos','Motion graphics and titles','Subtitles and text animation','Colour correction and retouch','AI video and lip-sync','YouTube thumbnails and covers','Remastering and upscaling','News and social-media shorts','Whole-channel production'],
 pr_h='Process', pr=[('Brief','Goal, audience, format, deadline.'),('References & storyboard','A shared picture of the result.'),('Edit & motion','Cut, animation, sound, preview link.'),('Revisions','Clear, consolidated feedback.'),('Delivery','Final files in the formats you need.')],
 c_h='Let’s make something worth watching.', c_s='The fastest way to reach me is Telegram.',
 lbl=dict(tg='Telegram',em='Email',fl='Freelancehunt',yt='YouTube'), fl_t='Freelancehunt profile', web='Portfolio site', cv='View the portfolio site',
 footer='GONAR · Video Editor · Motion Designer'),
'ru': dict(
 role='Видеомонтажёр · Моушн-дизайнер · Креативный продюсер', years='7+ лет в дизайне',
 cover_sub='Кинематографичный монтаж, моушн-графика, новостное и соцмедиа-видео, AI-пайплайны.',
 contact_lbl='Контакты', portfolio='Портфолио', year='2026',
 p_h='Профиль',
 p_big='Превращаю идеи в видео, которое понятно с первой секунды и которое хочется досмотреть.',
 p_txt=['Семь лет в дизайне провели меня через студии и команды с очень разными тематиками: новостные и соцмедиа-каналы, реклама, YouTube, интерьеры, e-commerce и анимация.',
        'Беру всю цепочку: концепция и раскадровка, монтаж, моушн-графика, звук, превью и сдача. Нейросети использую там, где они экономят время, а ритм, вкус и финальный звук остаются за мной.',
        'Для студий и брендов это один надёжный специалист, который понимает форматы, шаблоны и правила бренда и сдаёт файлы как договорились.'],
 pv=[('Диапазон','Уверенно работаю в очень разных жанрах и визуальных языках.'),('Пайплайн','От сценария до готового файла, с AI-инструментами там, где они помогают.'),('Надёжность','Бриф, шаблоны и форматы соблюдаются; сдача чистая.')],
 s_h='С чем я работаю',
 sk=[('Монтаж и моушн',['After Effects','Premiere Pro','Remotion (моушн в коде)','Титры и субтитры','Цветокоррекция']),
     ('3D',['Blender','Процедурные окружения','Свет и рендер']),
     ('Изображение и дизайн',['Photoshop','Превью для YouTube','Ретушь и композитинг','Инфографика для e-commerce']),
     ('AI и звук',['ComfyUI / Stable Diffusion','Whisper · Real-ESRGAN','ElevenLabs (голос, эффекты)','Звуковой дизайн и сведение','FFmpeg'])],
 e_h='Опыт по направлениям',
 ex=[('Новостные и соцмедиа-каналы','Вертикальные новостные ролики по шаблонам каналов, с озвучкой и звуком, быстрая сдача.','u4.webp'),
     ('Реклама и креативы','Квадратные и вертикальные рекламные креативы, кинетическая типографика и промо.','telefon.webp'),
     ('YouTube-каналы и превью','Продакшн канала целиком и контрастные обложки, на которые хочется нажать.','th_missing39.webp'),
     ('Мебель и интерьер','Рилсы, в которых стройка превращается в готовый дизайн-проект.','mebel.webp'),
     ('Инфографика для e-commerce','Карточки товаров и инфографика для маркетплейсов.','bag1.webp'),
     ('3D и AI-анимация','Окружения в Blender, 2.5D-комикс-анимация и AI-пайплайны.','chaos.webp'),
     ('Анимационные истории','Сценарий, озвучка, анимация и звук для длинных мистических историй.','soobshenie.webp')],
 w_h='Избранные работы',
 w_s='Восемь из одиннадцати проектов сайта-портфолио. Видео, описания кейсов и свежие работы — на сайте.',
 works=[('soobshenie','Сообщение от меня','Анимационная история · 2:39'),('volcano','Volcanic Valley','3D-окружение · Blender'),('chaos','Chaos Reality','Тест стиля 2.5D'),('marshrut0','Маршрут 0','Анимационная история · 2:56'),
        ('mebel','Мебель и квартира','Рилс об интерьере · 9:16'),('remont1','Студия ремонта','Рилс для соцсетей · 9:16'),('u4','Атака на энергетику','Новостной ролик · UNN'),('tz3','Атака дронов','Новостной ролик · TEZA')],
 sv_h='Услуги', sv=['Монтаж, рилсы и динамичные ролики','Моушн-графика и титры','Субтитры и анимация текста','Цветокоррекция и ретушь','AI-видео и липсинк','Превью и обложки YouTube','Ремастеринг и апскейл','Новостные ролики для соцсетей','Продакшн целых каналов'],
 pr_h='Процесс', pr=[('Бриф','Цель, аудитория, формат, срок.'),('Референсы и раскадровка','Общее понимание результата.'),('Монтаж и моушн','Монтаж, анимация, звук, превью по ссылке.'),('Правки','Понятные раунды правок.'),('Сдача','Финальные файлы в нужных форматах.')],
 c_h='Давайте сделаем то, что хочется смотреть.', c_s='Быстрее всего ответ в Telegram.',
 lbl=dict(tg='Telegram',em='Email',fl='Freelancehunt',yt='YouTube'), fl_t='Профиль на Freelancehunt', web='Сайт-портфолио', cv='Сайт-портфолио',
 footer='GONAR · Видеомонтажёр · Моушн-дизайнер')}

CSS = """
@font-face{font-family:'Inter Tight';font-weight:300;src:url('../fonts/d96a3a63.ttf')}
@font-face{font-family:'Inter Tight';font-weight:400;src:url('../fonts/71d1c35d.ttf')}
@font-face{font-family:'Inter Tight';font-weight:500;src:url('../fonts/7f6eefa6.ttf')}
@font-face{font-family:'Inter Tight';font-weight:600;src:url('../fonts/ae138b5c.ttf')}
@font-face{font-family:'Instrument Serif';src:url('../fonts/90405699.ttf')}
@font-face{font-family:'IBM Plex Mono';src:url('../fonts/9d122504.ttf')}
@page{size:A4;margin:0}
:root{--ink:#151514;--ink2:#1d1d1b;--paper:#ece8df;--mute:#8f8c84;--acc:#8da2ff;--accd:#3446c9;--line:rgba(236,232,223,.18)}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font:400 9.6pt/1.5 'Inter Tight',sans-serif;background:var(--ink);color:var(--paper)}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;break-after:page;padding:17mm 16mm 16mm;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto;break-after:auto}
.light{background:var(--paper);color:var(--ink)}
.dark{background:var(--ink)}
.serif{font-family:'Instrument Serif','Times New Roman',serif;font-weight:400;letter-spacing:-.01em}
.ru .serif{font-family:'Inter Tight',sans-serif;font-weight:300;letter-spacing:-.035em}
.mono{font:400 7.5pt/1.4 'IBM Plex Mono',monospace;color:var(--mute)}
.light .mono{color:#6c6a63}
.head{display:flex;justify-content:space-between;align-items:baseline;border-bottom:.3mm solid var(--line);padding-bottom:3.5mm;margin-bottom:10mm}
.light .head{border-color:rgba(21,21,20,.2)}
.head b{font:600 10pt 'Inter Tight'}
h2{font-size:34pt;line-height:1;margin-bottom:8mm}
img{display:block;width:100%;height:100%;object-fit:cover}
/* cover */
.cover{padding:0;justify-content:space-between}
.cover__img{position:absolute;inset:0}
.cover__img img{opacity:.55;filter:saturate(.85)}
.cover__img::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,21,20,.55) 0%,rgba(21,21,20,.25) 35%,rgba(21,21,20,.92) 85%,var(--ink) 100%)}
.cover>*:not(.cover__img){position:relative;z-index:1}
.cover__top{padding:16mm 16mm 0;display:flex;justify-content:space-between}
.cover__mid{padding:0 16mm}
.cover__word{font:600 112pt/.8 'Inter Tight';letter-spacing:-.065em;margin-left:-3mm}
.cover__role{font-size:15pt;margin-top:10mm;max-width:130mm;line-height:1.25;font-weight:400}
.cover__sub{color:#c9c5bb;max-width:110mm;margin-top:5mm}
.cover__bot{padding:0 16mm 16mm;display:grid;grid-template-columns:auto 1fr;gap:10mm;align-items:end;border-top:.3mm solid var(--line);padding-top:7mm;margin:0 16mm 0;padding-inline:0}
.yrs{font:300 46pt/1 'Inter Tight';letter-spacing:-.05em;color:var(--acc)}
.cover__bot dl{display:grid;grid-template-columns:auto 1fr;gap:1.5mm 6mm;font-size:9.5pt}
.cover__bot dt{color:var(--mute)}
.cover{padding-bottom:16mm}
/* profile */
.big{font-size:27pt;line-height:1.08;max-width:160mm;margin-bottom:9mm}
.ru .big{font-size:23pt}
.cols{columns:2;column-gap:10mm;color:#3b3a36}
.cols p{margin-bottom:3.5mm;break-inside:avoid}
.pv{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:auto;border-top:.3mm solid rgba(21,21,20,.25);padding-top:6mm}
.pv h3{font:500 12pt 'Inter Tight';margin-bottom:1.5mm}
.pv p{color:#55534d;font-size:9pt}
.pimg{height:62mm;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:3mm;margin-bottom:9mm}
/* skills */
.sk{display:grid;grid-template-columns:1fr 1fr;gap:9mm 10mm}
.sk h3{font:500 13pt 'Inter Tight';padding-bottom:2.5mm;border-bottom:.3mm solid var(--acc);margin-bottom:3mm}
.sk li{list-style:none;padding:2.2mm 0;border-bottom:.2mm solid var(--line);font-size:10.5pt}
.tools{display:flex;flex-wrap:wrap;gap:2.5mm;margin-top:auto}
.tools span{border:.3mm solid rgba(236,232,223,.4);border-radius:10mm;padding:2.5mm 5mm;font-size:11pt}
/* experience */
.ex{display:grid;gap:0;border-top:.3mm solid rgba(21,21,20,.25)}
.ex__i{display:grid;grid-template-columns:30mm 1fr;gap:6mm;padding:3.6mm 0;border-bottom:.3mm solid rgba(21,21,20,.25);align-items:center}
.ex__i .im{height:19mm;overflow:hidden;border-radius:.6mm;background:#ddd}
.ex__i h3{font:500 12.5pt 'Inter Tight';margin-bottom:.8mm}
.ex__i p{color:#55534d;font-size:9.2pt}
/* works */
.wk{display:grid;grid-template-columns:1fr 1fr;gap:6mm 6mm}
.wk .im{aspect-ratio:16/9;overflow:hidden;border-radius:.6mm;background:var(--ink2)}
.wk h3{font:500 10.5pt 'Inter Tight';margin-top:2mm}
.wkv{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:7mm}
.wkv .im{aspect-ratio:9/16;overflow:hidden;border-radius:.6mm;background:var(--ink2)}
.wkv h3{font:500 9.5pt/1.25 'Inter Tight';margin-top:2mm}
.lede{color:#c9c5bb;max-width:140mm;margin:-3mm 0 7mm}
/* services */
.svc{display:grid;grid-template-columns:1fr 1fr;gap:0 10mm;margin-bottom:9mm}
.svc li{list-style:none;padding:2.6mm 0;border-bottom:.2mm solid rgba(21,21,20,.25);font-size:10.5pt;font-weight:500}
.pr{display:grid;grid-template-columns:repeat(5,1fr);gap:4mm;margin-bottom:auto}
.pr div{border-top:.5mm solid var(--ink);padding-top:3mm}
.pr h3{font:500 10pt/1.2 'Inter Tight';margin-bottom:1.2mm}
.pr p{font-size:8.2pt;color:#55534d}
.pr .n{font:400 7.5pt 'IBM Plex Mono';color:var(--accd);display:block;margin-bottom:3mm}
.contact{margin:0 -16mm -16mm;padding:11mm 16mm 14mm;background:var(--ink);color:var(--paper);margin-top:9mm}
.contact h2{font-size:30pt;margin-bottom:3mm;max-width:150mm}
.contact .s{color:#c9c5bb;margin-bottom:7mm}
.ct{display:grid;grid-template-columns:28mm 1fr;gap:2.4mm 4mm;font-size:10.5pt}
.ct dt{font:400 7.8pt/1.9 'IBM Plex Mono';color:var(--mute)}
.ct a{color:var(--paper);text-decoration:none;border-bottom:.2mm solid var(--acc)}
.big-tg{font:600 30pt/1 'Inter Tight';letter-spacing:-.05em;margin-bottom:6mm;color:var(--acc)}
.foot{display:flex;justify-content:space-between;margin-top:6mm;color:var(--mute);font-size:8pt;border-top:.3mm solid var(--line);padding-top:3mm}
"""

def page(n, total, cls, inner, title=''):
    return f'<section class="page {cls}">{inner}</section>'

def head(t, n, total, title):
    return f'<div class="head"><b>GONAR</b><span class="mono">{title} · {n}/{total}</span></div>'

def build(lang):
    t = T[lang]; N = 6
    hero = M + 'volcano.jpg'
    p1 = f'''<section class="page cover dark">
 <div class="cover__img"><img src="{hero}" alt=""></div>
 <div class="cover__top"><span class="mono" style="color:#c9c5bb">{t["portfolio"]} {t["year"]}</span><span class="mono" style="color:#c9c5bb">t.me/aid99999</span></div>
 <div class="cover__mid"><div class="cover__word">GONAR</div><p class="cover__role serif">{t["role"]}</p><p class="cover__sub">{t["cover_sub"]}</p></div>
 <div class="cover__bot"><div class="yrs">{t["years"].split(" ")[0]}</div>
  <dl><dt>{t["years"].split(" ",1)[1]}</dt><dd></dd><dt>Telegram</dt><dd>@aid99999</dd><dt>Email</dt><dd>gonar777@gmail.com</dd><dt>Freelancehunt</dt><dd>freelancehunt.com/freelancer/gonar.html</dd></dl></div>
</section>'''
    ptxt = ''.join(f'<p>{x}</p>' for x in t['p_txt'])
    pv = ''.join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a, b in t['pv'])
    p2 = f'''<section class="page light">{head("", 2, N, t["p_h"])}
 <h2 class="serif">{t["p_h"]}</h2><p class="big serif">{t["p_big"]}</p>
 <div class="pimg"><div style="overflow:hidden"><img src="{M}marshrut0.jpg" alt=""></div><div style="overflow:hidden"><img src="{M}chaos.jpg" alt=""></div><div style="overflow:hidden"><img src="{M}mebel.jpg" alt=""></div></div>
 <div class="cols">{ptxt}</div><div class="pv">{pv}</div></section>'''
    sk = ''.join(f'<div><h3>{g}</h3><ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul></div>' for g, items in t['sk'])
    tools = ''.join(f'<span>{x}</span>' for x in ['After Effects', 'Premiere Pro', 'Photoshop', 'Blender', 'Remotion', 'ComfyUI / Stable Diffusion', 'ElevenLabs'])
    p3 = f'''<section class="page dark">{head("", 3, N, t["s_h"])}<h2 class="serif">{t["s_h"]}</h2><div class="sk">{sk}</div><div class="tools">{tools}</div></section>'''
    ex = ''.join(f'<div class="ex__i"><div class="im"><img src="{M + f.replace(".webp",".jpg")}" alt=""></div><div><h3>{a}</h3><p>{b}</p></div></div>' for a, b, f in t['ex'])
    p4 = f'''<section class="page light">{head("", 4, N, t["e_h"])}<h2 class="serif">{t["e_h"]}</h2><div class="ex">{ex}</div></section>'''
    w = t['works']
    land = ''.join(f'<div><div class="im"><img src="{M}{i}.jpg" alt=""></div><h3>{a}</h3><span class="mono">{b}</span></div>' for i, a, b in w[:4])
    vert = ''.join(f'<div><div class="im"><img src="{M}{i}.jpg" alt=""></div><h3>{a}</h3><span class="mono">{b}</span></div>' for i, a, b in w[4:])
    url = f'<br><a href="{SITE_URL}" style="color:var(--acc)">{SITE_URL}</a>' if SITE_URL else ''
    p5 = f'''<section class="page dark">{head("", 5, N, t["w_h"])}<h2 class="serif">{t["w_h"]}</h2><p class="lede">{t["w_s"]} {url}</p><div class="wk">{land}</div><div class="wkv">{vert}</div></section>'''
    sv = ''.join(f'<li>{x}</li>' for x in t['sv'])
    pr = ''.join(f'<div><span class="n">0{i+1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(t['pr']))
    L = t['lbl']
    p6 = f'''<section class="page light">{head("", 6, N, t["sv_h"])}
 <h2 class="serif" style="font-size:28pt;margin-bottom:5mm">{t["sv_h"]}</h2><ul class="svc">{sv}</ul>
 <h2 class="serif" style="font-size:28pt;margin-bottom:5mm">{t["pr_h"]}</h2><div class="pr">{pr}</div>
 <div class="contact"><h2 class="serif">{t["c_h"]}</h2><p class="s">{t["c_s"]}</p>
  <div class="big-tg">@aid99999</div>
  <dl class="ct"><dt>{L["tg"]}</dt><dd><a href="https://t.me/aid99999">t.me/aid99999</a></dd><dt>{L["em"]}</dt><dd><a href="mailto:gonar777@gmail.com">gonar777@gmail.com</a></dd><dt>{L["fl"]}</dt><dd><a href="https://freelancehunt.com/freelancer/gonar.html">freelancehunt.com/freelancer/gonar.html</a></dd><dt>{t["web"]}</dt><dd><a href="{SITE_URL}">gonar777-prog.github.io/portfolio-pro</a></dd></dl>
  <div class="foot"><span>{t["footer"]}</span><span>{t["year"]}</span></div></div></section>'''
    doc = f'<!doctype html><html lang="{lang}" class="{lang}"><head><meta charset="utf-8"><title>GONAR Portfolio {lang.upper()}</title><style>{CSS}</style></head><body class="{lang}">{p1}{p2}{p3}{p4}{p5}{p6}</body></html>'
    f = os.path.join(HERE, f'portfolio_{lang}.html'); open(f, 'w', encoding='utf8').write(doc)
    pdf = os.path.abspath(os.path.join(OUT, f'GONAR_Portfolio_{lang.upper()}.pdf'))
    subprocess.run([EDGE, '--headless', '--disable-gpu', '--no-pdf-header-footer', '--user-data-dir=D:\\TEMP\\edge_pdf_profile',
                    f'--print-to-pdf={pdf}', '--allow-file-access-from-files', 'file:///' + f.replace('\\', '/')], check=False, timeout=180)
    print(lang, os.path.getsize(pdf) if os.path.exists(pdf) else 'FAILED')

if __name__ == '__main__':
    for l in ('en', 'ru'): build(l)

"""Архив: переиспользует готовые веб-версии первого сайта (хардлинки; при пике звука > -6 дБ делает копию с понижением громкости, видео не перекодируется)."""
import os, re, subprocess, json, sys
SRC = r'D:\Claude\portfolio_site\assets'
DST = r'D:\Claude\portfolio_pro\media'
for d in ('archive\\video', 'archive\\loop', 'archive\\poster', 'gallery'):
    os.makedirs(os.path.join(DST, d), exist_ok=True)

def link(a, b):
    if os.path.exists(b): return
    try: os.link(a, b)
    except OSError:
        import shutil; shutil.copy2(a, b)

def probe(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,width,height,duration', '-of', 'json', p], capture_output=True, text=True)
    j = json.loads(r.stdout); v = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    return int(v['width']), int(v['height']), float(v.get('duration') or 0), any(s['codec_type'] == 'audio' for s in j['streams'])

def maxvol(p):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', p, '-af', 'volumedetect', '-vn', '-f', 'null', '-'], capture_output=True, text=True)
    m = re.search(r'max_volume: (-?[\d.]+) dB', r.stderr); return float(m.group(1)) if m else None

IDS = ['etazh13', 'otrazhenie', 'kasseta', 'gost2054', 'racia2', 'polaroid', 'sylar', 'matrica', 'matrica_11', 'matrica_916', 'ready1', 'remont2', 'remont3', 'ts1',
       'medical_bottle', 'citata1', 'citata2', 'citata3', 'coins3d', 'lipsync1', 'lipsync2', 'ps_lifehack', 'paranorma_clip', 'paranorma_clip_916', 'alien', 'gf_intro', 'cat_car', 'comic_subs']
info = {}
for i in IDS:
    sv = os.path.join(SRC, 'video', i + '.mp4'); dv = os.path.join(DST, 'archive', 'video', i + '.mp4')
    w, h, d, a = probe(sv)
    if not os.path.exists(dv):
        mv = maxvol(sv) if a else None
        if mv is not None and mv > -6.0:
            g = -6.5 - mv
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', sv, '-c:v', 'copy', '-af', f'volume={g}dB', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', dv], check=True)
            print('gain', i, mv, g)
        else: link(sv, dv)
    link(os.path.join(SRC, 'poster', i + '.jpg'), os.path.join(DST, 'archive', 'poster', i + '.jpg'))
    if os.path.exists(os.path.join(SRC, 'loop', i + '.mp4')):
        link(os.path.join(SRC, 'loop', i + '.mp4'), os.path.join(DST, 'archive', 'loop', i + '.mp4'))
    info[i] = dict(ar=round(w / h, 4), dur=round(d))
# галерея
GAL = re.findall(r'\{id:"(\w+)"', open(r'D:\Claude\portfolio_site\data.js', encoding='utf8').read().split('window.GALLERY')[1].split('window.GCATS')[0])
n = 0
for g in GAL:
    if g == 'th_yasmina': continue
    for pre in ('', 't_'):
        s = os.path.join(SRC, 'img', pre + g + '.webp')
        if os.path.exists(s): link(s, os.path.join(DST, 'gallery', pre + g + '.webp'))
    n += 1
print('gallery', n)
open(r'D:\Claude\portfolio_pro\tools\archive_info.json', 'w').write(json.dumps(info))
print(json.dumps(info))

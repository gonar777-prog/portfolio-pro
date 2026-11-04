import subprocess, re, shutil, os, sys
R=r'D:\Claude\portfolio_pro\media'
S=r'D:\Claude\portfolio_site\assets\video'
N=r'D:\Claude\teza\render\final4'
def run(a):
    r=subprocess.run(a,capture_output=True,text=True)
    if r.returncode: print('ERR',' '.join(a)[:200],r.stderr[-400:])
    return r
def maxvol(p):
    r=run(['ffmpeg','-hide_banner','-i',p,'-af','volumedetect','-vn','-f','null','-'])
    m=re.search(r'max_volume: (-?[\d.]+) dB',r.stderr); return float(m.group(1)) if m else None
# id: (src, poster_t, loop_t)
CASES={'soobshenie':(S+r'\soobshenie.mp4',22.8,22.8),'ostrov':(S+r'\ostrov.mp4',22.8,22.8),'marshrut0':(S+r'\marshrut0.mp4',150.9,147.5),
'volcano':(S+r'\volcano.mp4',10,8),'intro':(S+r'\intro.mp4',12,10),'gonarforce_logo':(S+r'\gonarforce_logo.mp4',5,1.2),
'chaos':(S+r'\chaos.mp4',7,1),'remont1':(S+r'\remont1.mp4',19,10),'telefon':(S+r'\telefon.mp4',2.6,0),'foto_anim':(S+r'\foto_anim.mp4',2,0),
'mebel':(r'D:\Рабочий стол СКА\Новая папка (4)\проект мебель и квартира 14.10.24\готово прав.mp4',36,12)}
V=r'D:\Канал\Все с компа\видео'
NEWS={'tz3':(V+r'\03_kirovohrad.mp4',),'u1':(V+r'\U1_tramp_starshield_ae.mp4',),'u2':(V+r'\U2_chaes_g7.mp4',),'u3':(V+r'\U3_oon_zhertvy_ae.mp4',),'u3s':(V+r'\U3_sumy_trc.mp4',),'u4':(V+r'\U4_ataka_enerhetyka.mp4',),
'n1':(N+r'\N1_unn_kyiv_ataka.mp4',),'n12':(N+r'\N12_unn_niderlandy.mp4',)}
def poster(src,t,out,w):
    run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',src,'-frames:v','1','-vf',f'scale={w}:-2','-c:v','libwebp','-quality','80',out])
def loop(src,t,out,vf,d=4):
    run(['ffmpeg','-v','error','-y','-ss',str(t),'-t',str(d),'-i',src,'-an','-vf',vf,'-c:v','libx264','-crf','31','-preset','slow','-pix_fmt','yuv420p','-movflags','+faststart',out])
def full(src,out,vf=None):
    mv=maxvol(src); args=['ffmpeg','-v','error','-y','-i',src]
    if vf: args+=['-vf',vf]
    if mv is None:
        args+=['-an']
    elif mv>-6.5:
        g=-6.5-mv; print('gain',out,mv,g); args+=['-af',f'volume={g}dB']
    if vf or (mv is not None and mv>-6.5) or True:
        args+=['-c:v','libx264','-crf','27','-preset','slow','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart',out]
    run(args)
if __name__=='__main__':
    what=sys.argv[1:] or ['cases','news']
    if 'cases' in what:
        for k,(s,pt,lt) in CASES.items():
            o=R+rf'\video\{k}.mp4'
            if not os.path.exists(o):
                mv=maxvol(s)
                if k=='mebel': full(s,o,'scale=720:1280')
                elif mv is not None and mv>-6.0: full(s,o)
                else: shutil.copy(s,o)
            vert=k in ('remont1','mebel')
            poster(s,pt,R+rf'\poster\{k}.webp',720 if vert else 1280)
            loop(s,lt,R+rf'\loop\{k}.mp4','scale=270:-2,fps=24' if vert else 'scale=480:-2,fps=24')
            print(k,'ok')
    if 'news' in what:
        for k,(s,) in NEWS.items():
            full(s,R+rf'\video\{k}.mp4','scale=720:1280')
            poster(s,1.0,R+rf'\poster\{k}.webp',540)
            loop(s,1,R+rf'\loop\{k}.mp4','scale=270:-2,fps=24')
            print(k,os.path.getsize(R+rf'\video\{k}.mp4'))



import subprocess,re
S=r'D:\Claude\portfolio_pro\media\video'
P=r'D:\Claude\portfolio_site\assets'
cuts=[('volcano',6,3),('soobshenie',22,3),('chaos',5.5,2.6),('ostrov',22,3),('gonarforce_logo',2,3),('marshrut0',148,3),
('racia2',53,3,P+r'\video\racia2.mp4'),('foto_anim',1,2.6),('etazh13',58,3,P+r'\video\etazh13.mp4'),('intro',11,2.5),('soobshenie',45.6,3),('volcano',20,3),('ostrov',60,3),('chaos',1,2.2)]
inp=[];fv=[];fa=[];n=len(cuts);XF=0
for i,c in enumerate(cuts):
    name,ss,d=c[:3]; path=c[3] if len(c)>3 else S+rf'\{name}.mp4'
    inp+=['-ss',str(ss),'-t',str(d),'-i',path]
    fv.append(f'[{i}:v]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=30,setsar=1,fade=t=in:st=0:d=0.2,fade=t=out:st={d-0.2}:d=0.2[v{i}]')
    if name=='volcano': fa.append(f'anullsrc=r=48000:cl=stereo,atrim=0:{d},asetpts=N/SR/TB[a{i}]')
    else: fa.append(f'[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:st=0:d=0.3,afade=t=out:st={d-0.4}:d=0.4[a{i}]')
cat=''.join(f'[v{i}]' for i in range(n))+f'concat=n={n}:v=1:a=0[v];'+''.join(f'[a{i}]' for i in range(n))+f'concat=n={n}:v=0:a=1,loudnorm=I=-20:TP=-8:LRA=7[a]'
g=';'.join(fv+fa)+';'+cat
open(r'D:\TEMP\reelgraph.txt','w').write(g)
subprocess.run(['ffmpeg','-v','error','-y']+inp+['-/filter_complex',r'D:\TEMP\reelgraph.txt','-map','[v]','-map','[a]','-c:v','libx264','-crf','24','-preset','slow','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-movflags','+faststart',r'D:\Claude\portfolio_pro\media\video\reel_full.mp4'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',r'D:\Claude\portfolio_pro\media\video\reel_full.mp4','-an','-vf','scale=1280:720','-c:v','libx264','-crf','33','-maxrate','1100k','-bufsize','2200k','-preset','slow','-pix_fmt','yuv420p','-movflags','+faststart',r'D:\Claude\portfolio_pro\media\video\reel_bg.mp4'],check=True)
r=subprocess.run(['ffmpeg','-hide_banner','-i',r'D:\Claude\portfolio_pro\media\video\reel_full.mp4','-af','volumedetect','-vn','-f','null','-'],capture_output=True,text=True)
print(re.findall(r'(max_volume|mean_volume): (\S+)',r.stderr))

import re, json
s = open(r'D:\Claude\portfolio_site\data.js', encoding='utf8').read()
g = s.split('window.GALLERY')[1].split('window.GCATS')[0]
rows = re.findall(r'\{id:"(\w+)", ch:"(\w+)", type:"(\w+)", ar:([\d.]+), title:"(.*?)"(?:, en:"(.*?)")?\}', g)
EN = {
'shapka_kanala':'Channel banner · green tram','shapka_3d':'Banner · 3D lettering','shapka_tram':'Banner · ghost tram','shapka_heroine':'Banner · heroine and light',
'shapka_dark':'Banner · night city','shapka_intro1':'Banner · variant 1','shapka_lighthouse':'Banner · lighthouse',
'logo_round':'Logo · round','logo_tram':'Logo · green ghost tram','logo_pal':'Logo · compact','logo_neon_tram':'Logo · neon tram','logo_ghost_tram':'Logo · ghost tram',
'thumb_alive':'Thumbnail · “Is it alive?!”','thumb_kasseta':'Thumbnail · vertical cassette story','thumb_episodes':'Thumbnail · seven episodes',
'card_13etazh':'Character card · Floor 13','card_arseniy':'Character card · Arseniy','card_artem':'Character card · Artem','card_liza':'Character card · Liza','card_conductor':'Character card · ghost conductor',
'gf_logo':'GONAR FORCE · logo','gf_harley':'Thumbnail · character review','gf_darthmaul':'Thumbnail · coloured contact lenses','gf_lenses_mesh':'Thumbnail · white mesh lenses',
'gf_greenlantern':'Thumbnail · animated series review','art_vortex':'Photo art · cloud vortex and sun','gf_nos4a2':'Thumbnail · series review','art_vampire_portrait':'Photo art · vampire portrait',
'gf_vampire':'Thumbnail · red lenses','gf_witcher':'Thumbnail · series review','art_sith':'Photo art · hooded figure','gf_kontiki':'Thumbnail · film review',
'gf_scary_lenses':'Thumbnail · scary lenses','card_bag1':'Product card · transformer backpack','card_bag2':'Product card · spacious backpack','card_bag3':'Product card · 70 cm transformer',
'gf_darkmaterials':'Thumbnail · series review'}
RU = {'gf_harley':'Превью · обзор персонажа','gf_darthmaul':'Превью · цветные линзы','gf_lenses_mesh':'Превью · линзы «белая сетка»','gf_greenlantern':'Превью · обзор мультсериала','gf_nos4a2':'Превью · обзор сериала','gf_vampire':'Превью · красные линзы','gf_witcher':'Превью · обзор сериала','gf_kontiki':'Превью · обзор фильма','gf_scary_lenses':'Превью · страшные линзы','gf_darkmaterials':'Превью · обзор сериала'}
CAT = {'thumb':'thumb','banner':'brand','logo':'brand','art':'art','char':'char','card':'prod','promo':'prod'}
out = []
for id_, ch, typ, ar, ru, en in rows:
    if id_ == 'th_yasmina': continue
    out.append(dict(id=id_, c=CAT[typ], ar=float(ar), ru=RU.get(id_, ru), en=en or EN.get(id_, ru)))
missing = [o['id'] for o in out if o['en'] == o['ru']]
print(len(out), 'no-en:', missing)
open(r'D:\Claude\portfolio_pro\js\gallery.js', 'w', encoding='utf8').write('window.GALLERY=' + json.dumps(out, ensure_ascii=False, indent=0) + ';\n')

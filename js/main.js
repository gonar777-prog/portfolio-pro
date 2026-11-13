(() => {
'use strict';
const S = window.SITE, $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const finePtr = matchMedia('(hover:hover) and (pointer:fine)').matches;
const store = { get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } }, set(k,v){ try { localStorage.setItem(k,v); } catch(e){} },
                sget(k){ try { return sessionStorage.getItem(k); } catch(e){ return null; } }, sset(k,v){ try { sessionStorage.setItem(k,v); } catch(e){} } };
let lang = store.get('lang') || ((navigator.language || 'en').toLowerCase().startsWith('ru') ? 'ru' : 'en');
const L = o => (o && (o[lang] || o.en)) || '';
const T = k => S.I18N[lang][k] || S.I18N.en[k] || '';
const ITEMS = [
  ...S.CASES.map(c => ({ ...c, kind: 'case' })),
  ...S.NEWS.map(n => ({ ...n, kind: 'news', ar: 0.5625, year: 2026, fmt: '9:16 · ' + n.dur,
    type: { en: 'News short · ' + n.ch, ru: 'Новостной ролик · ' + n.ch },
    role: { en: 'Edit, motion template, voice-over, sound', ru: 'Монтаж, моушн по шаблону, озвучка, звук' },
    tools: ['After Effects', 'AI voice-over'],
    line: { en: 'Vertical news edit for ' + n.ch + ', built to the channel template.', ru: 'Вертикальный новостной монтаж для ' + n.ch + ' по шаблону канала.' },
    brief: { en: 'Turn a breaking story into a clear vertical video, fast, without breaking the channel style.', ru: 'Быстро превратить свежую новость в понятный вертикальный ролик, не нарушая стиль канала.' },
    solution: { en: 'Template headline, data call-outs, voice-over and a mixed soundtrack, assembled in After Effects.', ru: 'Заголовок по шаблону, цифры-акценты, озвучка и сведённый звук, сборка в After Effects.' } }))
];
const byId = id => ITEMS.find(i => i.id === id);

/* ---------- text split ---------- */
function split(el, text) {
  el.textContent = '';
  text.split(' ').forEach((w, i) => {
    const o = document.createElement('span'); o.className = 'w';
    const s = document.createElement('span'); s.textContent = w; s.style.setProperty('--i', i); o.appendChild(s);
    el.appendChild(o); el.appendChild(document.createTextNode(' '));
  });
}
function setText(el, text) {
  if (el.hasAttribute('data-split')) { const was = el.classList.contains('in'); split(el, text); if (was) el.classList.add('in'); }
  else el.textContent = text;
}

/* ---------- render lists ---------- */
function renderLists() {
  $('#workTrack').innerHTML = S.CASES.map(c => `
    <li class="card" style="--ar:${c.ar}" data-id="${c.id}">
      <a class="card__a" href="#/work/${c.id}" data-cursor="View" data-open="${c.id}">
        <div class="card__m"><img src="media/poster/${c.id}.webp" alt="${L(c.title)}" width="1280" height="${Math.round(1280 / c.ar)}" loading="${S.CASES.indexOf(c) < 3 ? 'eager' : 'lazy'}" decoding="async"></div>
        <div class="card__t"><h3>${L(c.title)}</h3><span>${c.year}</span></div>
        <p class="card__r">${L(c.type)}. ${L(c.role)}</p>
      </a></li>`).join('');
  $('#shortsGrid').innerHTML = S.NEWS.map(n => `
    <li class="short" data-id="${n.id}"><a href="#/work/${n.id}" data-cursor="Play" data-open="${n.id}">
      <div class="short__m"><img src="media/poster/${n.id}.webp" alt="${L(n.title)}" width="540" height="960" loading="lazy" decoding="async"></div>
      <div class="short__t"><h3>${L(n.title)}</h3><span>${n.ch} · ${n.dur}</span></div></a></li>`).join('');
  $('#servList').innerHTML = S.SERVICES.map(s => `<li class="serv"><h3>${L(s.t)}</h3><p>${L(s.d)}</p></li>`).join('');
  $('#procList').innerHTML = S.PROCESS.map(s => `<li class="step"><h3>${L(s.t)}</h3><p>${L(s.d)}</p></li>`).join('');
  $('#expList').innerHTML = S.EXP.map(s => `<li class="exp__i"><h4>${L(s.t)}</h4><p>${L(s.d)}</p></li>`).join('');
  $('#apprList').innerHTML = S.APPR.map(s => `<li class="step"><h3>${L(s.t)}</h3><p>${L(s.d)}</p></li>`).join('');
  $$('[data-pdf]').forEach(a => { a.href = `assets/docs/GONAR_Portfolio_${lang.toUpperCase()}.pdf`; a.setAttribute('download', `GONAR_Portfolio_${lang.toUpperCase()}.pdf`); });
  $('#toolGroups').innerHTML = S.TOOLGROUPS.map(g => `<div class="tg"><h3>${L(g.g)}</h3><ul>${g.i.map(x => `<li>${typeof x === 'string' ? x : L(x)}</li>`).join('')}</ul></div>`).join('');
  $('#priceGrid').innerHTML = S.PRICING.map(p => `
    <li class="price${p.hot ? ' is-hot' : ''}"><span class="price__ghost" aria-hidden="true">${p.ghost}</span>
      <div class="price__top"><span class="badge">${L(p.time)}</span>${p.hot ? `<span class="badge badge--hot">${T('hot')}</span>` : ''}</div>
      <h3>${L(p.t)}</h3><p class="price__d">${L(p.d)}</p>
      <p class="price__p">${L(p.price)}</p>${L(p.alt) ? `<p class="price__alt">${L(p.alt)}</p>` : ''}
      <ul>${L(p.i).map(x => `<li>${x}</li>`).join('')}</ul>
      <a class="btn ${p.hot ? 'btn--solid' : ''}" href="${S.links.tg}" target="_blank" rel="noopener">${T('order')}</a></li>`).join('');
  $('#termsList').innerHTML = S.TERMS.map(x => `<li><b>${L(x.n)}</b><span>${L(x.t)}</span></li>`).join('');
  $('#revGrid').innerHTML = S.REVIEWS.map((r, n) => `<li class="rev${n > 5 ? ' rev--more' : ''}"><span class="stars" aria-label="5 of 5">★★★★★</span><blockquote>«${L(r.q)}»</blockquote><p class="rev__tag">${L(r.tag)} · Freelancehunt</p></li>`).join('');
  { const g = $('#revGrid'), b = $('#revMore') || Object.assign(document.createElement('button'), { id: 'revMore', type: 'button', className: 'btn mag rev__more' });
    if (!b.parentNode) g.after(b); const open = g.classList.contains('is-open');
    b.textContent = open ? (lang === 'ru' ? 'Свернуть' : 'Show less') : (lang === 'ru' ? `Показать все отзывы (${S.REVIEWS.length})` : `Show all reviews (${S.REVIEWS.length})`);
    b.onclick = () => { g.classList.toggle('is-open'); b.textContent = g.classList.contains('is-open') ? (lang === 'ru' ? 'Свернуть' : 'Show less') : (lang === 'ru' ? `Показать все отзывы (${S.REVIEWS.length})` : `Show all reviews (${S.REVIEWS.length})`); if (window.ScrollTrigger) ScrollTrigger.refresh(); }; }
  $('#faqList').innerHTML = S.FAQ.map((f, i) => `<details class="qa"${i === 0 ? ' open' : ''}><summary>${L(f.q)}</summary><p>${L(f.a)}</p></details>`).join('');
  renderArchive(); renderGallery();
  const m = S.MARQUEE[lang].map(x => `<span>${x}</span>`).join('');
  $('#marquee').innerHTML = m + m + m + m;
  bindHover();
}

function applyLang() {
  document.documentElement.lang = lang;
  $$('[data-i18n]').forEach(el => { const t = T(el.dataset.i18n); if (t) setText(el, t); });
  document.title = T('meta_title');
  const md = $('meta[name=description]'); if (md) md.content = T('meta_desc');
  $$('.lang button').forEach(b => b.setAttribute('aria-pressed', b.dataset.lang === lang));
  renderLists();
  if (current) fillCase(byId(current), false);
  if (window.ScrollTrigger) ScrollTrigger.refresh();
}

/* ---------- smooth scroll ---------- */
let lenis = null;
if (!reduced && window.Lenis) {
  lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 0.95, smoothWheel: true });
  gsap.ticker.add(t => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);
  lenis.on('scroll', ScrollTrigger.update);
}
gsap.registerPlugin(ScrollTrigger);
$$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
  const h = a.getAttribute('href'); if (h.startsWith('#/') || h === '#') return;
  const t = $(h); if (!t) return; e.preventDefault();
  if (lenis) lenis.scrollTo(t, { offset: 0, duration: 1.4 }); else t.scrollIntoView();
}));

/* ---------- hover previews ---------- */
function bindHover() {
  const make = (host, id, box, base = 'media/loop/') => {
    if (host._hb) return; host._hb = 1;
    let v = null;
    const on = () => {
      if (!v) { v = document.createElement('video'); v.muted = true; v.loop = true; v.playsInline = true; v.preload = 'auto'; v.setAttribute('aria-hidden', 'true'); v.src = `${base}${id}.mp4`; box.appendChild(v); }
      host.classList.add('is-hot'); v.play().catch(() => {});
    };
    const off = () => { host.classList.remove('is-hot'); if (v) v.pause(); };
    if (finePtr) { host.addEventListener('pointerenter', on); host.addEventListener('pointerleave', off); host.addEventListener('focusin', on); host.addEventListener('focusout', off); }
    else if ('IntersectionObserver' in window && !reduced) {
      new IntersectionObserver(es => es.forEach(e => e.isIntersecting && e.intersectionRatio > .6 ? on() : off()), { threshold: [0, .6] }).observe(host);
    }
  };
  $$('.card').forEach(c => make(c, c.dataset.id, $('.card__m', c)));
  $$('.short').forEach(c => make(c, c.dataset.id, $('.short__m', c)));
  $$('.acard').forEach(c => make(c, c.dataset.id, $('.acard__m', c), c.dataset.news ? 'media/loop/' : 'media/archive/loop/'));
  $$('[data-open]').forEach(a => { if (a._cb) return; a._cb = 1; a.addEventListener('click', e => { e.preventDefault(); openCase(a.dataset.open, a); }); });
}

/* ---------- case overlay ---------- */
const caseEl = $('#case'), cv = $('#caseVideo'); let current = null, originEl = null;
function fillCase(it, load) {
  caseEl.classList.toggle('is-v', it.ar < 1);
  $('#caseTitle').textContent = L(it.title);
  $('#caseType').textContent = L(it.type) + ' · ' + it.year;
  $('#caseLine').textContent = L(it.line);
  $('#caseCh').textContent = it.kind === 'news' ? it.ch : '';
  $('#caseMeta').innerHTML = [[T('role'), L(it.role)], [T('tools'), it.tools.join(', ')], [T('format'), it.fmt], [T('year'), it.year]].map(([k, v]) => `<div><dt>${k}</dt><dd>${v}</dd></div>`).join('');
  const ytU = it.yt ? S.links[it.yt] : '';
  $('#caseTxt').innerHTML = `<div><h3>${T('brief')}</h3><p>${L(it.brief)}</p></div><div><h3>${T('solution')}</h3><p>${L(it.solution)}</p></div>` + (ytU ? `<p class="case__yt"><a href="${ytU}" target="_blank" rel="noopener">${T('watch_yt')} ↗</a></p>` : '');
  const i = ITEMS.indexOf(it), nxt = ITEMS[(i + 1) % ITEMS.length];
  $('#caseNextT').textContent = L(nxt.title); $('#caseNext').dataset.id = nxt.id;
  if (load) { cv.style.setProperty('--ar', it.ar); cv.poster = `media/poster/${it.id}.webp`; cv.src = `media/video/${it.id}.mp4`; }
}
function openCase(id, from, silent) {
  const it = byId(id); if (!it) return;
  const first = !current; current = id; originEl = from || null;
  fillCase(it, true); $('#caseScroll').scrollTop = 0;
  if (!silent) history.pushState({ id }, '', '#/work/' + id);
  if (first) { caseEl.hidden = false; if (lenis) lenis.stop(); document.body.style.overflow = 'hidden'; }
  const kids = [$('.case__bar'), $('.case__stage'), $('.case__info'), $('.case__next')];
  if (reduced) { gsap.set(caseEl, { clipPath: 'none' }); cv.play().catch(() => {}); $('#caseBack').focus(); return; }
  const r = from ? from.querySelector('.card__m,.short__m,.acard__m').getBoundingClientRect() : null;
  const W = innerWidth, H = innerHeight;
  const start = r && first ? `inset(${r.top}px ${W - r.right}px ${H - r.bottom}px ${r.left}px)` : 'inset(50% 50% 50% 50%)';
  gsap.killTweensOf([caseEl, ...kids]);
  gsap.fromTo(caseEl, { clipPath: first ? start : 'inset(0px)' , opacity: 1 }, { clipPath: 'inset(0px 0px 0px 0px)', duration: first ? 1 : .01, ease: 'power4.inOut',
    onComplete: () => { caseEl.style.clipPath = 'none'; } });
  gsap.fromTo(kids, { y: 40, opacity: 0 }, { y: 0, opacity: 1, duration: .9, ease: 'power3.out', stagger: .08, delay: first ? .55 : .1 });
  setTimeout(() => { cv.play().catch(() => {}); $('#caseBack').focus({ preventScroll: true }); }, first ? 900 : 300);
}
function closeCase(silent) {
  if (!current) return; const id = current; current = null; cv.pause();
  if (!silent && history.state && history.state.id) history.back();
  const done = () => { caseEl.hidden = true; cv.removeAttribute('src'); cv.load(); document.body.style.overflow = ''; if (lenis) lenis.start(); const f = $(`[data-open="${id}"]`); if (f) f.focus({ preventScroll: true }); };
  const card = $(`[data-open="${id}"]`);
  const m = card && card.querySelector('.card__m,.short__m'); const r = m && m.getBoundingClientRect();
  const vis = r && r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
  if (reduced) return done();
  gsap.to(caseEl, { clipPath: vis ? `inset(${r.top}px ${innerWidth - r.right}px ${innerHeight - r.bottom}px ${r.left}px)` : 'inset(50% 50% 50% 50%)', duration: .8, ease: 'power4.inOut', onComplete: done });
}
$('#caseBack').addEventListener('click', () => closeCase());
$('#caseNext').addEventListener('click', e => openCase(e.currentTarget.dataset.id, null));
addEventListener('keydown', e => { if (e.key === 'Escape') { if (!$('#lb').hidden) return; if (!$('#reel').hidden) closeReel(); else if (current) closeCase(); } });
addEventListener('popstate', () => { const m = location.hash.match(/^#\/work\/(.+)$/); if (m) { if (byId(m[1]) && m[1] !== current) openCase(m[1], null, true); } else if (current) closeCase(true); });
$('#caseScroll').setAttribute('data-lenis-prevent', '');


/* ---------- archive + gallery ---------- */
let archCat = 'all', galCat = 'all';
const newsAsArch = () => S.NEWS.map(n => ({ id: n.id, cat: 'news', ar: 0.5625, dur: n.dur, t: n.title, d: { en: n.ch + ' · vertical news short', ru: n.ch + ' · вертикальный новостной ролик' }, news: true }));
const archItems = () => [...window.ARCH, ...newsAsArch()];
function filtersHtml(cats, cur, items, key) {
  return Object.keys(cats).filter(k => k === 'all' || items.some(i => (i[key]) === k)).map(k => `<button type="button" data-f="${k}" aria-pressed="${k === cur}">${cats[k][lang] || cats[k].en}</button>`).join('');
}
function renderArchive() {
  const items = archItems();
  $('#archFilters').innerHTML = filtersHtml(window.ACATS, archCat, items, 'cat');
  $('#archGrid').innerHTML = items.filter(i => archCat === 'all' || i.cat === archCat).map(i => {
    const poster = i.news ? `media/poster/${i.id}.webp` : `media/archive/poster/${i.id}.jpg`;
    return `<li class="acard" data-id="${i.id}" ${i.news ? 'data-news="1"' : ''}><a href="#" class="acard__a" data-cursor="${i.ar < 1 ? 'Play' : 'Play'}" data-arch="${i.id}">
      <div class="acard__m" style="aspect-ratio:${i.ar}"><img src="${poster}" alt="${L(i.t)}" loading="lazy" decoding="async"></div>
      <div class="acard__t"><h3>${L(i.t)}</h3><span>${i.dur}</span></div></a></li>`;
  }).join('');
  $$('#archFilters button').forEach(b => b.onclick = () => { archCat = b.dataset.f; renderArchive(); bindHover(); });
  $$('[data-arch]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); const it = items.find(x => x.id === a.dataset.arch); if (it.news) openCase(it.id, a); else openLb('v', it); }));
}
function renderGallery() {
  const items = window.GALLERY;
  $('#galFilters').innerHTML = filtersHtml(window.GCATS, galCat, items, 'c');
  $('#galGrid').innerHTML = items.filter(i => galCat === 'all' || i.c === galCat).map(i =>
    `<li class="gitem"><a href="#" data-gal="${i.id}" data-cursor="View"><img src="media/gallery/t_${i.id}.webp" alt="${i[lang] || i.en}" width="600" height="${Math.round(600 / i.ar)}" loading="lazy" decoding="async" style="aspect-ratio:${i.ar}"></a></li>`).join('');
  $$('#galFilters button').forEach(b => b.onclick = () => { galCat = b.dataset.f; renderGallery(); });
  const vis = items.filter(i => galCat === 'all' || i.c === galCat);
  $$('[data-gal]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); openLb('i', vis.find(x => x.id === a.dataset.gal), vis); }));
  if (window.ScrollTrigger) ScrollTrigger.refresh();
}
/* viewer: video (v) or image (i) */
const lb = $('#lb'); let lbList = null, lbIdx = 0, lbKind = 'v';
function lbFill(kind, it) {
  const M = $('#lbM'); M.innerHTML = ''; $('#lbV').innerHTML = '';
  if (kind === 'v') {
    const vid = document.createElement('video'); vid.controls = true; vid.playsInline = true; vid.preload = 'metadata';
    const set = (id, ar) => { vid.src = `media/archive/video/${id}.mp4`; vid.poster = `media/archive/poster/${id}.jpg`; vid.style.aspectRatio = ar; vid.style.setProperty('--ar', ar); lb.classList.toggle('is-v', ar < 1); lb.classList.toggle('is-sq', ar === 1); };
    set(it.id, it.ar); M.appendChild(vid);
    $('#lbT').textContent = L(it.t); $('#lbD').textContent = L(it.d);
    if (it.variants) { const all = [{ id: it.id, label: it.ar === 1 ? '1:1' : '16:9', ar: it.ar }, ...it.variants];
      $('#lbV').innerHTML = all.map((v, i) => `<button type="button" data-v="${i}" aria-pressed="${i === 0}">${v.label}</button>`).join('');
      $$('#lbV button').forEach(b => b.onclick = () => { const v = all[+b.dataset.v]; set(v.id, v.ar); vid.play().catch(() => {}); $$('#lbV button').forEach(x => x.setAttribute('aria-pressed', x === b)); }); }
    vid.play().catch(() => {});
  } else {
    lb.classList.remove('is-v', 'is-sq');
    const img = document.createElement('img'); img.src = `media/gallery/${it.id}.webp`; img.alt = it[lang] || it.en; M.appendChild(img);
    $('#lbT').textContent = it[lang] || it.en; $('#lbD').textContent = '';
  }
}
function openLb(kind, it, list) {
  lbKind = kind; lbList = list || null; lbIdx = list ? list.indexOf(it) : 0;
  lb.hidden = false; document.body.style.overflow = 'hidden'; if (lenis) lenis.stop();
  $('#lbP').hidden = $('#lbN').hidden = !list;
  lbFill(kind, it); $('#lbX').focus();
  if (!reduced) gsap.fromTo(lb, { opacity: 0 }, { opacity: 1, duration: .35 });
}
function closeLb() { const v = $('video', lb); if (v) { v.pause(); v.removeAttribute('src'); v.load(); } $('#lbM').innerHTML = ''; lb.hidden = true; document.body.style.overflow = current ? 'hidden' : ''; if (!current && lenis) lenis.start(); }
function lbStep(d) { if (!lbList) return; lbIdx = (lbIdx + d + lbList.length) % lbList.length; lbFill('i', lbList[lbIdx]); }
$('#lbX').addEventListener('click', closeLb); $('#lbP').addEventListener('click', () => lbStep(-1)); $('#lbN').addEventListener('click', () => lbStep(1));
lb.addEventListener('click', e => { if (e.target === lb || e.target.id === 'lbF') closeLb(); });
addEventListener('keydown', e => { if (lb.hidden) return; if (e.key === 'Escape') closeLb(); else if (e.key === 'ArrowLeft') lbStep(-1); else if (e.key === 'ArrowRight') lbStep(1); });

/* ---------- reel lightbox ---------- */
const reelEl = $('#reel'), rv = $('#reelVideo'), hv = $('#heroVideo');
$('#reelBtn').addEventListener('click', () => {
  reelEl.hidden = false; hv.pause(); if (lenis) lenis.stop(); document.body.style.overflow = 'hidden';
  rv.preload = 'auto'; rv.currentTime = 0; rv.muted = false; rv.play().catch(() => {}); $('#reelX').focus();
  if (!reduced) gsap.fromTo(reelEl, { opacity: 0 }, { opacity: 1, duration: .5 });
});
function closeReel() { rv.pause(); reelEl.hidden = true; const v2 = $('#vkVideo'); if (v2) v2.play().catch(() => {}); document.body.style.overflow = current ? 'hidden' : ''; if (!current && lenis) lenis.start(); hv.play().catch(() => {}); }
$('#reelX').addEventListener('click', closeReel);

/* ---------- hero business card (Portfolio Sylar TG) ---------- */
const vk = $('#vkVideo'), vkB = $('#vkSnd'), vkT = $('#vkSndT');
if (vk) {
  const setVk = () => { const on = !vk.muted; vkB.classList.toggle('is-on', on); vkB.setAttribute('aria-pressed', on); vkT.dataset.i18n = on ? 'vk_off' : 'vk_on'; vkT.textContent = T(vkT.dataset.i18n); };
  const mute = () => { vk.muted = true; vk.loop = true; setVk(); };
  vkB.addEventListener('click', () => {
    if (vk.muted) { vk.currentTime = 0; vk.muted = false; vk.loop = false; vk.play().catch(() => mute()); } else { mute(); vk.play().catch(() => {}); }
    setVk();
  });
  vk.addEventListener('ended', () => { mute(); vk.currentTime = 0; vk.play().catch(() => {}); });
  $('#reelBtn').addEventListener('click', () => { if (!vk.muted) mute(); vk.pause(); });
  new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { if (reelEl.hidden) vk.play().catch(() => {}); } else { if (!vk.muted) mute(); vk.pause(); } }), { threshold: .15 }).observe(vk);
}

/* ---------- hero timecode ---------- */
const tc = $('#tc'), pad = n => String(n).padStart(2, '0');
const fmtTc = t => `00:${pad(Math.floor(t / 60) % 60)}:${pad(Math.floor(t) % 60)}:${pad(Math.floor((t % 1) * 30))}`;
let tcOn = true; new IntersectionObserver(es => { tcOn = es[0].isIntersecting; }).observe($('#hero'));
(function loop() { if (tcOn && !hv.paused) tc.textContent = fmtTc(hv.currentTime); requestAnimationFrame(loop); })();

/* ---------- cursor + magnetic ---------- */
if (finePtr) {
  document.body.classList.add('cur-on');
  const cur = $('#cursor'), lab = $('#cursorLabel');
  const qx = gsap.quickTo(cur, 'x', { duration: .35, ease: 'power3' }), qy = gsap.quickTo(cur, 'y', { duration: .35, ease: 'power3' });
  addEventListener('pointermove', e => { qx(e.clientX); qy(e.clientY); });
  document.addEventListener('pointerover', e => { const t = e.target.closest('[data-cursor]'); if (t) { lab.textContent = t.dataset.cursor; cur.classList.add('has-label'); } else cur.classList.remove('has-label'); });
  $$('.mag').forEach(el => {
    const mx = gsap.quickTo(el, 'x', { duration: .5, ease: 'power3' }), my = gsap.quickTo(el, 'y', { duration: .5, ease: 'power3' });
    el.addEventListener('pointermove', e => { const r = el.getBoundingClientRect(); mx((e.clientX - r.left - r.width / 2) * .25); my((e.clientY - r.top - r.height / 2) * .35); });
    el.addEventListener('pointerleave', () => { mx(0); my(0); });
  });
}

/* ---------- scroll animations ---------- */
function setupScroll() {
  $$('[data-split]').forEach(el => { if (el.closest('.hero')) return; ScrollTrigger.create({ trigger: el, start: 'top 88%', once: true, onEnter: () => el.classList.add('in') }); });
  if (reduced) { $$('[data-split]').forEach(e => e.classList.add('in')); $$('[data-count]').forEach(e => e.textContent = e.dataset.count); return; }
  gsap.to('.hero__media', { yPercent: 10, ease: 'none', scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true } });
  gsap.to('.hero__main,.hero__top', { opacity: 0, y: -40, ease: 'none', scrollTrigger: { trigger: '#hero', start: '35% top', end: 'bottom 20%', scrub: true } });
    $$('.thumb img').forEach((img, i) => gsap.fromTo(img, { yPercent: -5 }, { yPercent: 5, ease: 'none', scrollTrigger: { trigger: img.parentElement, scrub: true } }));
  $$('.thumb').forEach(t => { t.style.overflow = 'hidden'; const im = $('img', t); im.style.scale = 1.12; });
  $$('.step,.serv,.chan,.short,.thumb,.price,.rev,.qa,.fact').forEach(el => gsap.from(el, { opacity: 0, y: 36, duration: .9, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 92%', once: true } }));
  $$('[data-count]').forEach(el => { const n = +el.dataset.count, o = { v: 0 };
    ScrollTrigger.create({ trigger: el, start: 'top 92%', once: true, onEnter: () => gsap.to(o, { v: n, duration: 1.6, ease: 'power2.out', onUpdate: () => el.textContent = Math.round(o.v) + (el.dataset.suf || '') }) }); });
  gsap.matchMedia().add('(min-width: 900px)', () => {
    const track = $('#workTrack'), vp = $('.work__viewport');
    const dist = () => Math.max(0, track.scrollWidth + parseFloat(getComputedStyle(vp).paddingLeft) * 2 - vp.clientWidth);
    gsap.to(track, { x: () => -dist(), ease: 'none', scrollTrigger: { trigger: '#workPin', start: 'top top', end: () => '+=' + dist(), pin: true, scrub: .6, invalidateOnRefresh: true, anticipatePin: 1 } });
  });
}

/* ---------- intro ---------- */
function intro() {
  const el = $('#intro'), b = $('#introBar'), t = $('#introTc'); let done = false;
  const reveal = () => { document.body.classList.remove('is-loading'); $$('.hero [data-split]').forEach(h => h.classList.add('in')); if (lenis) lenis.start(); ScrollTrigger.refresh(); };
  const finish = () => { if (done) return; done = true; store.sset('seen', '1');
    if (reduced) { el.remove(); reveal(); return; }
    gsap.to(el, { yPercent: -100, duration: .9, ease: 'power4.inOut', onStart: () => setTimeout(reveal, 250), onComplete: () => el.remove() }); };
  if (store.sget('seen') || reduced) { el.remove(); reveal(); return; }
  const o = { v: 0 };
  if (lenis) lenis.stop();
  gsap.to(o, { v: 1, duration: 1.0, ease: 'power2.inOut', onUpdate: () => { b.style.transform = `scaleX(${o.v})`; t.textContent = fmtTc(o.v * 4.2); }, onComplete: finish });
  gsap.from('.intro__name', { yPercent: 100, duration: 1, ease: 'power4.out', delay: .1 });
  $('#introSkip').addEventListener('click', finish);
  addEventListener('keydown', e => { if (!done && (e.key === 'Escape' || e.key === 'Enter' || e.key === ' ')) finish(); });
  el.addEventListener('click', finish);
}

/* ---------- misc ---------- */
$$('.lang button').forEach(b => b.addEventListener('click', () => { lang = b.dataset.lang; store.set('lang', lang); applyLang(); }));
$('#copyMail').addEventListener('click', async e => {
  const btn = e.currentTarget, mail = S.links.email;
  try { await navigator.clipboard.writeText(mail); } catch (er) { const ta = document.createElement('textarea'); ta.value = mail; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); } catch (x) {} ta.remove(); }
  btn.textContent = T('email_done'); setTimeout(() => btn.textContent = T('email_copy'), 1800);
});
document.addEventListener('visibilitychange', () => { if (document.hidden) { hv.pause(); } else if (reelEl.hidden) hv.play().catch(() => {}); });

/* boot */
$('#stVideo').dataset.count = $('#stVideo2').dataset.count = S.CASES.length + S.NEWS.length + window.ARCH.length; $('#stDesign').dataset.count = window.GALLERY.length;
applyLang(); setupScroll(); intro();
const m = location.hash.match(/^#\/work\/(.+)$/); if (m && byId(m[1])) setTimeout(() => openCase(m[1], null, true), 300);
const mv = location.hash.match(/^#\/video\/(.+)$/); if (mv) { const it = window.ARCH.find(x => x.id === mv[1]); if (it) setTimeout(() => { $('#archive').scrollIntoView(); openLb('v', it); }, 500); }
if (reduced) hv.removeAttribute('autoplay');
})();

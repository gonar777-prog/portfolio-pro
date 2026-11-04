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
  $('#thumbsGrid').innerHTML = S.THUMBS.map(t => `<li class="thumb"><img src="media/img/${t.f}.webp" alt="${L(t.alt)}" width="1280" height="${Math.round(1280 / t.ar)}" loading="lazy" decoding="async"></li>`).join('');
  $('#servList').innerHTML = S.SERVICES.map(s => `<li class="serv"><h3>${L(s.t)}</h3><p>${L(s.d)}</p></li>`).join('');
  $('#procList').innerHTML = S.PROCESS.map(s => `<li class="step"><h3>${L(s.t)}</h3><p>${L(s.d)}</p></li>`).join('');
  $('#expList').innerHTML = S.EXP.map(s => `<li class="exp__i"><h4>${L(s.t)}</h4><p>${L(s.d)}</p></li>`).join('');
  $('#apprList').innerHTML = S.APPR.map(s => `<li class="step"><h3>${L(s.t)}</h3><p>${L(s.d)}</p></li>`).join('');
  $$('[data-pdf]').forEach(a => { a.href = `assets/docs/GONAR_Portfolio_${lang.toUpperCase()}.pdf`; a.setAttribute('download', `GONAR_Portfolio_${lang.toUpperCase()}.pdf`); });
  $('#toolsList').innerHTML = S.TOOLS.map(t => `<li>${t}</li>`).join('');
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
  const make = (host, id, box) => {
    let v = null;
    const on = () => {
      if (!v) { v = document.createElement('video'); v.muted = true; v.loop = true; v.playsInline = true; v.preload = 'auto'; v.setAttribute('aria-hidden', 'true'); v.src = `media/loop/${id}.mp4`; box.appendChild(v); }
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
  $$('[data-open]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); openCase(a.dataset.open, a); }));
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
  $('#caseTxt').innerHTML = `<div><h3>${T('brief')}</h3><p>${L(it.brief)}</p></div><div><h3>${T('solution')}</h3><p>${L(it.solution)}</p></div>`;
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
  const r = from ? from.querySelector('.card__m,.short__m').getBoundingClientRect() : null;
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
addEventListener('keydown', e => { if (e.key === 'Escape') { if (!$('#reel').hidden) closeReel(); else if (current) closeCase(); } });
addEventListener('popstate', () => { const m = location.hash.match(/^#\/work\/(.+)$/); if (m) { if (byId(m[1]) && m[1] !== current) openCase(m[1], null, true); } else if (current) closeCase(true); });
$('#caseScroll').setAttribute('data-lenis-prevent', '');

/* ---------- reel lightbox ---------- */
const reelEl = $('#reel'), rv = $('#reelVideo'), hv = $('#heroVideo');
$('#reelBtn').addEventListener('click', () => {
  reelEl.hidden = false; hv.pause(); if (lenis) lenis.stop(); document.body.style.overflow = 'hidden';
  rv.preload = 'auto'; rv.currentTime = 0; rv.muted = false; rv.play().catch(() => {}); $('#reelX').focus();
  if (!reduced) gsap.fromTo(reelEl, { opacity: 0 }, { opacity: 1, duration: .5 });
});
function closeReel() { rv.pause(); reelEl.hidden = true; document.body.style.overflow = current ? 'hidden' : ''; if (!current && lenis) lenis.start(); hv.play().catch(() => {}); }
$('#reelX').addEventListener('click', closeReel);

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
  gsap.to('.hero__word', { yPercent: 18, ease: 'none', scrollTrigger: { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true } });
  $$('.thumb img').forEach((img, i) => gsap.fromTo(img, { yPercent: -5 }, { yPercent: 5, ease: 'none', scrollTrigger: { trigger: img.parentElement, scrub: true } }));
  $$('.thumb').forEach(t => { t.style.overflow = 'hidden'; const im = $('img', t); im.style.scale = 1.12; });
  $$('.step,.serv,.chan,.short,.thumb').forEach(el => gsap.from(el, { opacity: 0, y: 36, duration: .9, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 92%', once: true } }));
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
  gsap.to(o, { v: 1, duration: 1.7, ease: 'power2.inOut', onUpdate: () => { b.style.transform = `scaleX(${o.v})`; t.textContent = fmtTc(o.v * 4.2); }, onComplete: finish });
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
applyLang(); setupScroll(); intro();
const m = location.hash.match(/^#\/work\/(.+)$/); if (m && byId(m[1])) setTimeout(() => openCase(m[1], null, true), 300);
if (reduced) hv.removeAttribute('autoplay');
})();

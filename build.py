#!/usr/bin/env python3
"""Ave Mujica を観る日（10/23金）の3コース提案ページ。 python3 build.py -> index.html
デザインは https://yukitchy.github.io/sakatsu/ と同じ骨格（manga-week系）。"""
import json, html

PH = json.load(open('photos.json'))
def img(k): return PH[k]['thumb']
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + urlq(q)
def urlq(s):
    import urllib.parse; return urllib.parse.quote(s)
def emb(q): return 'https://maps.google.com/maps?q=' + urlq(q) + '&output=embed&z=16'
def route_link(stops):
    import urllib.parse
    s = [urllib.parse.quote(x) for x in stops]
    return ('https://www.google.com/maps/dir/?api=1&origin=' + s[0] + '&destination=' + s[-1]
            + ('&waypoints=' + '%7C'.join(s[1:-1]) if len(s) > 2 else '') + '&travelmode=transit')

COURSES = [
 dict(id='A', area='品川', kicker='COURSE A', name='品川', place='T・ジョイPRINCE品川',
  tag='駅から3分。劇場も店もホテルの敷地で完結', card=img('cinema_shinagawa'),
  chips=['品川駅から徒歩3分', '雨に濡れない', 'IMAXあり'],
  why='品川プリンスホテルの中にある劇場です。品川駅の高輪口を出て坂を上がればすぐで、観たあとの店も同じ敷地にあります。移動が一番少ないのがこのコース。',
  photos=[img('cinema_shinagawa2'), img('hotel_night')],
  steps=[('10:00', 'T・ジョイPRINCE品川に集合', '品川駅の高輪口から歩いて3分。品川プリンスホテル アネックスタワーの中です。'),
         ('10:20', '上映開始', '回の時刻が出たら確定します。チケットはユウキが取ります。'),
         ('12:40', '終映、そのまま歩く', 'ホテルの敷地内なので、外に出ずに店まで行けます。'),
         ('13:00', 'ランチ', '下の2軒から選びます。')],
  moves='品川駅 高輪口 → 劇場 徒歩3分。劇場 → 店 徒歩3分。',
  stops=['品川駅', 'T・ジョイPRINCE品川', '品川プリンスホテル'],
  eats=[('LUXE DINING HAPUNA', '品川プリンスホテル · ビュッフェ', '同じホテルのメインタワーにあるビュッフェ。劇場から屋根の下を歩いて行けるので、終映から座るまでが一番速い。', '品川プリンスホテル LUXE DINING HAPUNA', img('hotel_entrance')),
        ('とんかつ かつ仙', '高輪 · とんかつ', '品川では数少ないとんかつの専門店。群馬の赤城山麓の銘柄豚を使っていて、昼も混みます。', 'とんかつ かつ仙 品川', img('tonkatsu'))],
  good='移動を最小にしたい日。雨予報の日。IMAXで観たい場合もここ。',
  mind='ホテルの敷地は広いので、集合は劇場の入口前にします。ビュッフェは混む時間帯があります。',
  links=[('T・ジョイPRINCE品川', 'https://tjoy.jp/t-joy_prince_shinagawa')]),

 dict(id='B', area='川崎', kicker='COURSE B', name='川崎', place='チネチッタ',
  tag='映画館も店も、ひとつの広場の中にある', card=img('citta_plaza'),
  chips=['川崎駅から徒歩5分', '音がいい劇場', '広場で選べる'],
  why='イタリアの街並みを模したラ チッタデッラという広場の中にある映画館です。音の設備に力を入れている劇場なので、ライブの場面がある作品と相性がいい。店も同じ広場の中から選べます。',
  photos=[img('citta_arcade'), img('citta_fountain')],
  steps=[('10:00', 'チネチッタに集合', '川崎駅の東口から歩いて5分。ラ チッタデッラの広場を入ってすぐです。'),
         ('10:20', '上映開始', '回の時刻が出たら確定します。'),
         ('12:40', '終映、広場に出る', '店は広場を出ずに歩いて1分です。'),
         ('13:00', 'ランチ', '下の2軒から選びます。')],
  moves='川崎駅 東口 → チネチッタ 徒歩5分。劇場 → 店 徒歩1分。',
  stops=['川崎駅', 'チネチッタ', 'ラ チッタデッラ'],
  eats=[('酉十郎 川崎店', 'ラ チッタデッラ · 定食', 'クラブチッタの入口の正面。定食や御膳がしっかり出てくるので、腹を決めて食べたい時はここ。', '酉十郎 川崎店', img('teishoku')),
        ('イル・パチョッコーネ・ディ・キャンティ', 'ラ チッタデッラ · イタリアン', '広場の中のイタリアン。トスカーナのキャンティ地方の郷土料理が中心で、広場を眺めながら座れます。', 'IL PACIOCCONE DI CHIANTI 川崎', img('pasta'))],
  good='映画のあとに歩き回りたくない日。広場そのものが気持ちいいので、昼まで居られる。',
  mind='土日の広場はイベントで混みます。10/23は金曜なので比較的静かなはずです。',
  links=[('チネチッタ', 'https://cinecitta.co.jp/'), ('ラ チッタデッラ', 'https://lacittadella.co.jp/')]),

 dict(id='C', area='横浜', kicker='COURSE C', name='横浜', place='横浜ブルク13',
  tag='駅前のビルの11階。店は向かいの崎陽軒本店', card=img('skybldg'),
  chips=['横浜駅から徒歩3分', '地下街で直結', '崎陽軒の本店'],
  why='横浜駅の東口、横浜スカイビルの中にある劇場です。観たあとは向かいの崎陽軒本店へ。地下街のポルタで繋がっているので、外を歩かずに行けます。',
  photos=[img('kiyoken'), img('seabass')],
  steps=[('10:00', '横浜ブルク13に集合', '横浜駅の東口から歩いて3分。横浜スカイビルの11階です。'),
         ('10:20', '上映開始', '回の時刻が出たら確定します。'),
         ('12:40', '終映、地下へ降りる', 'ポルタの地下街を通って崎陽軒本店へ。'),
         ('13:00', 'ランチ', '下の2軒から選びます。')],
  moves='横浜駅 東口 → 劇場 徒歩3分。劇場 → 崎陽軒本店 徒歩3分（地下街で繋がっています）。',
  stops=['横浜駅', '横浜ブルク13', '崎陽軒本店'],
  eats=[('崎陽軒本店 嘉宮', '横浜駅東口 · 中国料理', '崎陽軒の本店の中の中国料理。壺で出てくる料理とランチのコースがあります。', '崎陽軒本店 嘉宮', img('shumai')),
        ('崎陽軒本店 イル・サッジオ', '横浜駅東口 · イタリアン', '同じ本店の中のイタリアン。ナポリの郷土料理をやっている店なので、中華の気分じゃない日はこちら。', '崎陽軒本店 イルサッジオ', img('pizza'))],
  good='そのあと横浜で遊びたい日。みなとみらいも中華街も電車ですぐです。',
  mind='スカイビルは入口が分かりにくいので、集合はビルの1階のエレベーター前にします。',
  links=[('横浜ブルク13', 'https://www.kinezo.jp/burg13/'), ('崎陽軒本店', 'https://kiyoken.com/'),]),
]

def card(c):
    ch = ''.join('<li>' + html.escape(t) + '</li>' for t in c['chips'])
    return f'''<button class="mcard" type="button" data-course="{c['id']}" aria-expanded="false" aria-controls="detail-{c['id']}">
<img src="{c['card']}" alt="{html.escape(c['place'])}" loading="lazy">
<span class="mb"><span class="mk">{c['kicker']}</span><span class="mt">{html.escape(c['name'])}<small class="mpl"> {html.escape(c['place'])}</small></span>
<span class="mtag">{html.escape(c['tag'])}</span><ul class="mch">{ch}</ul><span class="mopen">コースを見る</span></span></button>'''

def detail(c):
    ph = ''.join(f'<img src="{u}" alt="{html.escape(c["name"])}コースの写真" loading="lazy">' for u in c['photos'])
    st = ''.join(f'<li><b>{t}</b><div><strong>{html.escape(h)}</strong><span>{html.escape(d)}</span></div></li>' for t, h, d in c['steps'])
    fd = ''.join(f'<a class="eat" href="{gm(q)}" target="_blank" rel="noopener">'
                 f'<img src="{im}" alt="{html.escape(n)}" loading="lazy">'
                 f'<span class="eb"><strong>{html.escape(n)}</strong><em>{html.escape(a)}</em><span>{html.escape(d)}</span>'
                 f'<i>Googleマップで開く ↗</i></span></a>'
                 for n, a, d, q, im in c['eats'])
    ln = ' '.join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(t)} ↗</a>' for t, u in c['links'])
    return f'''<section class="detail" id="detail-{c['id']}" hidden><div class="dwrap"><div class="dtop"></div>
<div class="dhead"><div><p class="kicker">{c['kicker']} · {html.escape(c['area'])}</p><h2><span class="nb">{html.escape(c['place'])}</span></h2></div>
<button class="dclose" type="button" aria-label="閉じる">CLOSE ✕</button></div>
<p class="why">{html.escape(c['why'])}</p>
<div class="photos">{ph}</div>
<div class="dgrid">
<div><h3>TIMELINE</h3><ol class="steps">{st}</ol></div>
<div><h3>MAP</h3><div class="mapbox"><iframe src="{emb(c['place'])}" loading="lazy" title="{html.escape(c['place'])}" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<p class="moves">{html.escape(c['moves'])} <a href="{route_link(c['stops'])}" target="_blank" rel="noopener">経路をGoogleマップで開く ↗</a></p></div>
</div>
<h3>ランチはこの2軒から</h3><div class="eats">{fd}</div>
<div class="notes"><p><b>GOOD</b> {html.escape(c['good'])}</p><p><b>NOTE</b> {html.escape(c['mind'])}</p></div>
<p class="links">{ln}</p>
<a class="choose" href="{gm(c['place'])}" target="_blank" rel="noopener">Googleマップで{html.escape(c['place'])}を開く</a>
</div></section>'''

KV = [('img/img_kv_02.webp', '劇場版 Ave Mujica prima aurora キービジュアル', 'center 35%'),
      ('img/img_kv_01.webp', '劇場版 Ave Mujica ティザービジュアル', 'center 63%'),
      ('img/movieintro.webp', '劇場版 Ave Mujica の場面写真', 'center center')]
slides = ''.join(f'<img src="{u}" alt="{html.escape(a)}" style="object-position:{pos}">' for u, a, pos in KV)
dots = ''.join('<button type="button" aria-label="ビジュアル' + str(i + 1) + '"></button>' for i in range(len(KV)))
credits = ' / '.join(sorted(set(html.escape(v['title'].rsplit('.', 1)[0]) for v in PH.values())))

page = f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>10/23 Ave Mujica｜品川・川崎・横浜の3コース</title><meta name="robots" content="noindex">
<meta property="og:title" content="10/23（金）Ave Mujica を観て、そのままランチ。">
<meta property="og:description" content="品川・川崎・横浜の3コース。劇場と観たあとの店をセットにしてあります。行きたいエリアを1つ選んでください。">
<meta property="og:image" content="https://yukitchy.github.io/ave-mujica-day/ogp.png?v=2">
<meta property="og:url" content="https://yukitchy.github.io/ave-mujica-day/">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22><rect width=%2232%22 height=%2232%22 fill=%22%23111%22/><rect x=%2214%22 y=%225%22 width=%224%22 height=%2222%22 rx=%222%22 fill=%22%231a5c3a%22/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=Inter:wght@500;600;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#fffdf6;--card:#fff;--ink:#111;--mute:#767065;--line:#eae4d6;--acc:#1a5c3a;--r:10px}}
*{{box-sizing:border-box;min-width:0}} html,body{{overflow-x:hidden;max-width:100%}} img{{max-width:100%}}
body{{margin:0;font-family:Inter,"Zen Kaku Gothic New",-apple-system,"Hiragino Sans",sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
.kicker{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin:0 0 10px}}
h1,h2,.mt{{text-wrap:balance}} .nb{{white-space:nowrap;display:inline-block}}
h1{{font-weight:800;font-size:clamp(30px,5.4vw,54px);line-height:1.14;letter-spacing:-.025em;margin:0 0 16px}}
h2{{font-weight:800;font-size:clamp(26px,4.2vw,42px);line-height:1.14;letter-spacing:-.025em;margin:0}}
h3{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin:0 0 12px}}
.hpic{{position:relative;background:#111;color:#fff}}
.slides{{position:absolute;inset:0;overflow:hidden}}
.slides img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity 1.1s ease,transform 5s linear}}
.slides img.on{{opacity:1;transform:scale(1)}}
.slides:after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.08) 30%,rgba(0,0,0,.74))}}
.hcap{{position:relative;z-index:1;min-height:62vh;max-height:600px;display:flex;flex-direction:column;justify-content:flex-end;padding-top:48px;padding-bottom:22px}}
.hcap .kicker{{color:#9ee3b8}}
.hcap h1{{color:#fff;margin:0 0 14px;text-shadow:0 2px 14px rgba(0,0,0,.3)}}
.esub{{margin:0 0 16px;font-size:14px;font-weight:600;letter-spacing:.12em;color:#e6e0d4}}
.snav{{display:flex;align-items:center;gap:10px}}
.slabel{{font:inherit;font-size:12.5px;font-weight:600;color:#fff;background:rgba(0,0,0,.38);border:1px solid rgba(255,255,255,.4);border-radius:999px;padding:7px 13px;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.dots{{display:flex;gap:7px;margin-left:auto;flex:none}}
.dots button{{width:9px;height:9px;padding:0;border:none;border-radius:50%;background:rgba(255,255,255,.45);cursor:pointer}}
.dots button.on{{background:#fff}}
.hbody{{padding-top:22px;padding-bottom:26px}}
@media(prefers-reduced-motion:reduce){{.slides img{{transition:none;transform:none}}}}
header p{{font-size:18px;color:var(--mute);margin:0;max-width:620px}}
.facts{{display:flex;flex-wrap:wrap;gap:6px 20px;margin:20px 0 0;padding:0;list-style:none;font-size:14px;color:var(--mute)}} .facts b{{color:var(--ink);font-weight:600}}
.sechead{{display:flex;align-items:baseline;gap:14px;padding:26px 0 16px;border-top:1px solid var(--line)}}
.sechead .n{{font-weight:800;font-size:26px;line-height:1;letter-spacing:-.02em;color:var(--acc)}}
.sechead b{{font-size:19px;font-weight:600}} .sechead span{{font-size:14px;color:var(--mute)}}
.menu{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.mcard{{display:flex;flex-direction:column;text-align:left;font:inherit;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;padding:0;cursor:pointer;transition:transform .18s,box-shadow .18s,border-color .18s}}
.mcard:hover{{transform:translateY(-3px);box-shadow:0 10px 24px rgba(34,31,27,.10)}}
.menu.picked .mcard:not([aria-expanded=true]){{opacity:.42;filter:saturate(.45)}}
.menu.picked .mcard:not([aria-expanded=true]):hover{{opacity:.75;filter:none}}
.mcard[aria-expanded=true]{{border:2px solid var(--ink);box-shadow:0 12px 28px rgba(17,17,17,.16);transform:translateY(-3px)}}
.mcard[aria-expanded=true] .mopen{{color:var(--acc);border-bottom-color:var(--acc)}}
.mcard>img{{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:#f0ebe0}}
.mb{{display:flex;flex-direction:column;flex:1;padding:18px 20px 20px}}
.mk{{display:block;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin-bottom:6px}}
.mt{{display:block;font-weight:800;font-size:26px;line-height:1.16;letter-spacing:-.025em;margin-bottom:6px}}
.mpl{{display:block;font-size:15px;font-weight:600;letter-spacing:0;color:var(--mute);margin-top:2px}}
.mtag{{display:block;font-size:15px;color:var(--mute);margin-bottom:12px}}
.mch{{list-style:none;margin:auto 0 14px;padding:0;display:flex;flex-wrap:wrap;gap:6px}}
.mch li{{font-size:11px;font-weight:600;letter-spacing:.04em;border:1px solid var(--line);border-radius:4px;padding:3px 8px;color:var(--mute)}}
.mopen{{align-self:flex-start;display:inline-block;font-size:14px;font-weight:600;border-bottom:2px solid var(--acc);padding-bottom:1px}}
.mcard[aria-expanded=true] .mopen::after{{content:" ▲"}} .mcard[aria-expanded=false] .mopen::after{{content:" ▾"}}
.detail{{scroll-margin-top:12px;display:grid;grid-template-rows:0fr;transition:grid-template-rows .32s ease;margin-top:14px;position:relative}}
.detail[hidden]{{display:none}} .detail.open{{grid-template-rows:1fr}}
.dwrap{{overflow:hidden;min-height:0;background:var(--card);border:2px solid var(--ink);border-radius:var(--r);position:relative}}
.detail::before{{content:'';position:absolute;top:-11px;left:var(--arrow,50%);width:20px;height:20px;margin-left:-10px;background:var(--acc);border-left:2px solid var(--acc);border-top:2px solid var(--acc);transform:rotate(45deg);z-index:2;opacity:0;transition:opacity .2s .12s}}
.detail.open::before{{opacity:1}}
.dtop{{height:5px;background:var(--acc)}}
.detail.open .dwrap{{overflow:visible}}
.dwrap>*{{margin-left:26px;margin-right:26px}} .dwrap>.dtop{{margin:0}}
.dhead{{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;padding-top:26px}}
.dclose{{flex:none;font:inherit;font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--mute);background:none;border:1px solid var(--line);border-radius:6px;padding:8px 14px;cursor:pointer}}
.dclose:hover{{color:var(--ink);border-color:var(--ink)}}
.why{{font-size:17px;color:var(--mute);margin:10px 0 20px;max-width:640px}}
.photos{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-bottom:26px}}
.photos img{{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:8px;background:#f0ebe0}}
.dgrid{{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:28px}}
.steps{{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}}
.steps li{{display:grid;grid-template-columns:64px minmax(0,1fr);gap:12px;padding:11px 0;border-bottom:1px solid var(--line)}}
.steps b{{font-variant-numeric:tabular-nums;color:var(--acc);font-weight:600;font-size:14px}} .steps strong{{display:block;font-weight:600;font-size:16px}} .steps span{{color:var(--mute);font-size:14px}}
.mapbox{{border-radius:8px;overflow:hidden;background:#f0ebe0}} .mapbox iframe{{display:block;width:100%;height:300px;border:0}}
.moves{{font-size:14px;color:var(--mute);margin:12px 0 0}} .moves a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px;white-space:nowrap}}
.eats{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-bottom:26px}}
.eat{{display:flex;flex-direction:column;text-decoration:none;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;overflow:hidden}}
.eat>img{{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;background:#f0ebe0}}
.eb{{display:flex;flex-direction:column;flex:1;padding:14px 16px 16px}}
.eat:hover{{border-color:var(--ink)}}
.eat strong{{display:block;font-weight:700;font-size:18px;line-height:1.25;letter-spacing:-.015em}}
.eat em{{display:block;font-style:normal;font-size:11px;color:var(--acc);font-weight:600;letter-spacing:.08em;margin:5px 0 9px}}
.eb>span{{display:block;font-size:14px;color:var(--mute)}} .eat i{{display:block;font-style:normal;font-size:12px;margin-top:auto;padding-top:10px;text-decoration:underline;text-underline-offset:3px}}
.notes{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;font-size:14px}} .notes p{{margin:0;padding:16px 18px;background:var(--bg);border:1px solid var(--line);border-radius:8px}} .notes b{{display:block;font-weight:600;margin-bottom:3px}}
.links{{margin:0 0 22px;font-size:14px;display:flex;flex-wrap:wrap;gap:6px 18px}} .links a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px}}
.choose{{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;font-weight:700;padding:16px 32px;border-radius:8px;font-size:16px;letter-spacing:-.01em;margin-bottom:28px}} .choose:hover{{background:#333}}
.pre{{display:grid;grid-template-columns:300px minmax(0,1fr);gap:30px;align-items:start;padding-bottom:8px}}
.pre>img{{width:100%;border-radius:10px;display:block;background:#f0ebe0}}
.pre p{{font-size:17px;color:var(--mute);margin:0 0 16px;max-width:620px}}
.pre p b{{color:var(--ink);font-weight:600}}
.vid{{position:relative;padding-top:56.25%;border-radius:10px;overflow:hidden;background:#000;margin:0 0 22px}}
.vid iframe{{position:absolute;inset:0;width:100%;height:100%;border:0}}
.pre h3{{margin-top:22px}}
.syn{{margin:0 0 18px;padding:16px 20px;background:var(--bg);border-left:3px solid var(--acc);border-radius:0 8px 8px 0;font-size:16px;color:var(--ink);line-height:1.75}}
.syn cite{{display:block;font-style:normal;font-size:12px;color:var(--mute);margin-top:8px;letter-spacing:.04em}}
.pre p b{{color:var(--ink);font-weight:600}}
.cast{{width:100%;border-collapse:collapse;font-size:14px;margin:0 0 20px}}
.cast td{{padding:9px 0;border-bottom:1px solid var(--line)}}
.cast tr:last-child td{{border-bottom:none}}
.cast td:first-child{{font-weight:600;white-space:nowrap;padding-right:14px}}
.cast td:nth-child(2){{color:var(--acc);font-size:12px;font-weight:600;letter-spacing:.06em;white-space:nowrap;padding-right:14px}}
.cast td:last-child{{color:var(--mute);text-align:right}}
.tail{{padding:30px 0 60px;border-top:1px solid var(--line);margin-top:36px}}
.tail p{{font-size:15px;color:var(--mute);max-width:640px;margin:0 0 10px}}
.tail b{{color:var(--ink)}}
.cred{{font-size:11px;color:#a49d90;margin-top:20px;line-height:1.6}}
@media(max-width:860px){{ .pre{{grid-template-columns:1fr;gap:20px}} .pre>img{{max-width:280px;margin:0 auto}} .menu{{grid-template-columns:1fr}} .dgrid{{grid-template-columns:1fr;gap:22px}} .notes{{grid-template-columns:1fr}} .eats{{grid-template-columns:1fr}} .dwrap>*{{margin-left:18px;margin-right:18px}} }}
</style></head><body>
<header class="hero"><div class="hpic"><div class="slides">{slides}</div>
<div class="wrap hcap"><p class="kicker">FRI, OCT 23 · 10:00</p>
<h1><span class="nb">Ave Mujica を観て、</span><span class="nb">そのままランチ。</span></h1>
<p class="esub">SHINAGAWA · KAWASAKI · YOKOHAMA</p>
<div class="snav"><span class="slabel">劇場版 BanG Dream! Ave Mujica prima aurora</span><div class="dots">{dots}</div></div></div></div>
<div class="wrap hbody"><p>10/23（金）の午前の回で観ます。劇場と、観たあとに歩いて行ける店をセットにして3案作りました。行きたいエリアを1つ選んでください。</p>
<ul class="facts"><li><b>日にち</b> 10/23（金）</li><li><b>集合</b> 10時台（回が出たら確定）</li><li><b>人数</b> 2人</li><li><b>作品</b> 劇場版 Ave Mujica prima aurora</li></ul></div></header>

<div class="wrap">
<div class="sechead"><span class="n">1</span><div><b>どんな映画か</b> <span>観る前に、これだけ。</span></div></div>
<div class="pre">
<img src="img/img_kv_01.webp" alt="劇場版 Ave Mujica のティザービジュアル" loading="lazy">
<div>
<p><b>劇場版「BanG Dream! Ave Mujica prima aurora」</b>。バンドリの世界のガールズバンド Ave Mujica の物語で、全編が新しく作られた新作です。10月16日（金）公開で、観るのはその翌週の金曜。</p>
<blockquote class="syn">Ave Mujicaの再デビューから半年以上が過ぎ、季節は春。バンドはさらに人気を博し、メンバーそれぞれの活動も軌道に乗っていた。次なる舞台として祥子が打ち出したのは、会員制のマスカレード。神になると誓った彼女の思惑とは……<cite>公式サイトのイントロダクション</cite></blockquote>
<h3>予告（公式・バンドリちゃんねる☆）</h3>
<div class="vid"><iframe src="https://www.youtube-nocookie.com/embed/Uqt2rXUA-r8" title="映画「BanG Dream! Ave Mujica prima aurora」2026年10月16日 公開" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy"></iframe></div>
<h3>軽くおさらい</h3>
<p style="font-size:15px">TVシリーズは、一度バラバラになった Ave Mujica が最後に5人で戻ってくるところで終わりました。劇場版はその<b>続き</b>で、時間は半年ぶん飛びます。TVシリーズを観ていれば、そのまま入って大丈夫です。</p>
<h3>バンドの5人</h3>
<table class="cast">
<tr><td>豊川 祥子</td><td>オブリビオニス</td><td>高尾 奏音</td></tr>
<tr><td>三角 初華</td><td>ドロリス</td><td>佐々木 李子</td></tr>
<tr><td>若葉 睦</td><td>モーティス</td><td>渡瀬 結月</td></tr>
<tr><td>八幡 海鈴</td><td>ティモリス</td><td>岡田 夢以</td></tr>
<tr><td>祐天寺 にゃむ</td><td>アモーリス</td><td>米澤 茜</td></tr>
</table>
<p style="font-size:14px">監督は柿本広大、音楽は藤田淳平（Elements Garden）、アニメーション制作はニチカライン。<a href="https://avemujica-movie.bang-dream.com/" target="_blank" rel="noopener" style="color:var(--ink);text-decoration:underline;text-underline-offset:3px">公式サイト ↗</a></p>
</div></div>

<div class="sechead" style="margin-top:36px"><span class="n">2</span><div><b>コースは3択</b> <span>カードを押すと、当日の流れ・地図・店が出ます。</span></div></div>
<div class="menu">{''.join(card(c) for c in COURSES)}</div>
{''.join(detail(c) for c in COURSES)}

<div class="sechead" style="margin-top:36px"><span class="n">3</span><div><b>決め方</b> <span>返事はエリア名だけで大丈夫です。</span></div></div>
<div class="tail" style="border:none;padding-top:0">
<p><b>品川・川崎・横浜のどれか</b>を返してください。店は当日その場で決めても大丈夫です。</p>
<p>10/23の上映時刻は、どの劇場もまだ出していません。だいたい1週間前、<b>10月17日ごろ</b>に出るので、出たらユウキが10時台の回を押さえて、時刻と座席をあらためて連絡します。</p>
<p>営業時間と定休日は変わることがあるので、当日の朝にリンクから確認します。</p>
<p class="cred">10/23（金）10:00〜13:00は「いつなら？」で確定した枠です。店の写真は料理のイメージです。<br>作品のビジュアルとあらすじは劇場版 Ave Mujica 公式サイトより。<br>エリアと料理の写真は Wikimedia Commons（CC BY / CC BY-SA / CC0）: {credits}</p>
</div>
</div>

<script>
(function(){{
 var sl=[].slice.call(document.querySelectorAll('.slides img')),dots=[].slice.call(document.querySelectorAll('.dots button')),i=0,t;
 function show(n){{i=n;sl.forEach(function(x,k){{x.classList.toggle('on',k===n)}});dots.forEach(function(x,k){{x.classList.toggle('on',k===n)}})}}
 function go(){{clearInterval(t);if(!matchMedia('(prefers-reduced-motion: reduce)').matches)t=setInterval(function(){{show((i+1)%sl.length)}},4600)}}
 dots.forEach(function(d,k){{d.addEventListener('click',function(){{show(k);go()}})}});
 show(0);go();
}})();
(function(){{
 var menu=document.querySelector('.menu');
 function close(b){{var d=document.getElementById(b.getAttribute('aria-controls'));b.setAttribute('aria-expanded','false');d.classList.remove('open');setTimeout(function(){{if(!d.classList.contains('open'))d.hidden=true}},320);}}
 [].forEach.call(document.querySelectorAll('.mcard'),function(b){{
  b.addEventListener('click',function(){{
   var open=b.getAttribute('aria-expanded')==='true';
   [].forEach.call(document.querySelectorAll('.mcard[aria-expanded=true]'),close);
   if(open){{menu.classList.remove('picked');return}}
   var d=document.getElementById(b.getAttribute('aria-controls'));
   d.hidden=false;b.setAttribute('aria-expanded','true');menu.classList.add('picked');
   var r=b.getBoundingClientRect(),m=menu.getBoundingClientRect();
   d.style.setProperty('--arrow',(r.left-m.left+r.width/2)+'px');
   requestAnimationFrame(function(){{d.classList.add('open');}});
   setTimeout(function(){{d.scrollIntoView({{behavior:'smooth',block:'nearest'}})}},340);
  }});
 }});
 [].forEach.call(document.querySelectorAll('.dclose'),function(x){{
  x.addEventListener('click',function(){{
   var d=x.closest('.detail'),b=document.querySelector('.mcard[aria-controls="'+d.id+'"]');
   close(b);menu.classList.remove('picked');b.scrollIntoView({{behavior:'smooth',block:'center'}});
  }});
 }});
}})();
</script>
</body></html>'''
open('index.html','w').write(page)
print('index.html', len(page), 'bytes')

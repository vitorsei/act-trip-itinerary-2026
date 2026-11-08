from route_map import render_route_map
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parents[1]
places = {p['id']: p for p in json.loads((ROOT/'scripts/destinations.json').read_text())}

def photo(url, alt, source):
    return dict(url=url, alt=alt, source=source)

ainslie = photo('https://images.trvl-media.com/place/553248621552334752/7047caa9-9a7f-49bd-82f0-d62653f9e018.jpg', 'Canberra and Lake Burley Griffin from Mount Ainslie lookout', 'https://www.expedia.com/Mount-Ainslie-Canberra.d553248621552334752.Vacation-Attraction')
photos = {k:v['photos'] for k,v in places.items()}
photos['ainslie'] = [ainslie]

photos['newacton'][0] = photo('https://i0.wp.com/thefifthestate.com.au/wp-content/uploads/2015/04/Nishi.jpg?fit=600%2C400&ssl=1', 'Nishi building in NewActon', 'https://thefifthestate.com.au/events/tfeevents/event-news/awards-event-news/canberras-nishi-building-receives-international-acclaim/')

def a(url, label):
    return f'<a href="{e(url,quote=True)}" target="_blank" rel="noopener noreferrer">{e(label)} ↗</a>'

def maps(name):
    return a('https://www.google.com/maps/search/?api=1&query='+quote(name+', Australia'), name)

def gallery(items, label):
    return '<div class="gallery" aria-label="'+e(label)+'">'+''.join(f'<figure><a class="photo-link" href="{e(p["url"],quote=True)}" target="_blank" rel="noopener noreferrer"><img loading="lazy" decoding="async" src="{e(p["url"],quote=True)}" alt="{e(p["alt"],quote=True)}" width="600" height="476"></a><figcaption>{a(p["source"],"Photo credit and source")}</figcaption></figure>' for p in items)+'</div>'

def ps(*keys):
    return [photos[k][0] for k in keys]

days=[]
def day(id,date,num,title,stay,effort,drive,items,note,images,links,swap=None):
    days.append(dict(id=id,date=date,num=num,title=title,stay=stay,effort=effort,drive=drive,items=items,note=note,images=images,links=links,swap=swap))

day('day-1','Thu 24 Dec',1,'Sydney to Canberra, via Goulburn','Canberra · 1 of 2 nights','Easy stops + city evening','About 3½–4 hr driving, before lunch and baby breaks',[
('Morning','Leave Sydney and break in Goulburn. Belmore Park has picnic tables, a playground and toilets; the Big Merino is an optional separate photo stop.'),
('Afternoon','Check in, buy Christmas groceries and settle in. Choose Civic and Braddon for a short wander and early dinner.'),
('Evening','Choose one neighbourhood for dinner, then return to your accommodation. Mount Ainslie has its own planned visit on 26 December.')],
'Keep arrival day simple: a proper Goulburn break, Christmas groceries and one Canberra neighbourhood. Mount Ainslie is a firm stop on 26 December, before the drive south.',
ps('goulburn','civic','braddon'), [('https://www.parks.act.gov.au/find-a-nature-park/canberra-nature-park/mount-ainslie-nature-reserve','Mount Ainslie access and summit track'),('https://www.nsw.gov.au/visiting-and-exploring-nsw/locations-and-attractions/belmore-park','Belmore Park')],swap=('A different city evening','Choose NewActon’s Nishi architecture or Kingston Foreshore’s waterfront promenade and dinner instead of Braddon. Pick one precinct; restaurant Christmas Eve hours need checking.'))

day('day-2','Fri 25 Dec',2,'Christmas at the Arboretum and the lake','Canberra · 2 of 2 nights','Short walks, picnic and a nap break','Local driving · allow 45–75 min across the day',[
('Morning','Explore the National Arboretum grounds and views around Dairy Farmers Hill. Take a look at the POD playground; its higher climbing pods are mainly for older children.'),
('Midday','Return for lunch and your baby’s nap. Bring Christmas food rather than depending on cafés.'),
('Afternoon','Take a short Lake Burley Griffin stroll around Commonwealth Park or the National Carillon. Keep the afternoon flexible around your baby’s nap and the heat; Mount Ainslie is scheduled for tomorrow.')],
'Arboretum grounds and the POD playground are listed as open daily. The visitor centre, café and bonsai collection close on 25 December. Keep this a flexible outdoor Christmas, especially if the day is hot.',
ps('arboretum','lake','ainslie'), [('https://www.nationalarboretum.act.gov.au/visit/opening-hours','Arboretum holiday hours'),('https://www.nca.gov.au/attractions/national-carillon','National Carillon')])

day('day-3','Sat 26 Dec',3,'Mount Ainslie, then south to Jindabyne','Jindabyne · 1 of 3 nights','Drive-up summit · short wander + travel','Canberra → Cooma → Jindabyne · about 2½ hr intercity driving, plus local lookout access and breaks',[
('Morning','Have breakfast, then drive to Mount Ainslie summit. Allow 45–60 minutes for the Canberra panorama, photographs and a short wander. This is the main morning stop, not an optional extra.'),
('Late morning and lunch','Leave Canberra and head towards Cooma. Stop for lunch, feeding and time out of the car at Centennial Park, with a playground, picnic areas, toilets and baby-change facilities. Allow roughly 45–60 minutes, or longer if needed.'),
('Afternoon','Continue to Jindabyne, check into an ensuite cabin or apartment, stock the kitchen and have a relaxed evening.')],
'Driving to Mount Ainslie summit gives you the views without making the steep summit hike part of a transfer day. Cooma is a practical lunch and park break; no Discovery Centre visit or other ticketed attraction is scheduled. Arrive in Jindabyne during the afternoon without rushing the lookout.',
ps('ainslie','cooma','jindabyne'), [('https://www.parks.act.gov.au/find-a-nature-park/canberra-nature-park/mount-ainslie-nature-reserve','Mount Ainslie access'),('https://www.nsw.gov.au/visiting-and-exploring-nsw/locations-and-attractions/cooma-centennial-park','Centennial Park facilities')])

day('day-4','Sun 27 Dec',4,'Thredbo and the Kosciuszko lookout','Jindabyne · 2 of 3 nights','4km return · exposed alpine walking','About 1–1½ hr driving return · allow 4–6 hr for the full outing',[
('Morning','Drive to Thredbo and take the scenic lift, subject to operations and confirmed infant/carrier arrangements.'),
('The walk','Follow the Kosciuszko lookout route: 4km return, about 1–2 hours walking before baby breaks. Enjoy granite formations and open alpine scenery.'),
('Afternoon','Return by lift with a buffer before the last service, then enjoy a relaxed village meal. Keep the rest of the day free.')],
'Confirm how your baby and backpack carrier can travel on the lift before buying tickets. Choose the calmest of the two mountain days for this walk. A village visit or Lake Jindabyne rest day is the lower-effort alternative.',
[photos['thredbo'][0],photos['lookout'][0],photos['lookout'][1]], [('https://www.thredbo.com.au/activities/gondola-and-chairlift/','Scenic lift information'),('https://www.thredbo.com.au/activities/hikes/self-guided-hikes/','Lookout walk'),('https://www.nationalparks.nsw.gov.au/safety/alpine-safety','Alpine weather planning')])

day('day-5','Mon 28 Dec',5,'Charlotte Pass and the Snow Gums boardwalk','Jindabyne · 3 of 3 nights','400m return boardwalk · steps and exposure','About 1½–2 hr driving return from Jindabyne · allow 3–4 hr overall for the outing',[
('Morning','Drive to Charlotte Pass for the Snow Gums boardwalk, twisted alpine trees and views towards the Main Range. Allow 15–30 minutes walking before photographs and baby breaks; the boardwalk includes steps and exposed viewpoints.'),
('Lunch','Picnic at Sawpit Creek on the way back down. Keep it a simple picnic stop rather than adding another hike.'),
('Afternoon','Return to the same Jindabyne accommodation for a nap and an easy afternoon. Prepare for tomorrow’s drive home.')],
'This is deliberately the shorter outing after Thredbo. Short distance still needs warm layers and suitable conditions. Swap 27 and 28 December if that gives the exposed lift-top walk a calmer forecast; both nights are in the same base.',
[photos['charlotte'][0],photos['sawpit'][0],photos['charlotte'][1]], [('https://www.nationalparks.nsw.gov.au/things-to-do/lookouts/charlotte-pass-lookout','Charlotte Pass lookout'),('https://www.nationalparks.nsw.gov.au/-/media/visitor/files/pdf/brochures/kosciuszko-national-park/thredbo-perisher-area-walking-tracks-brochure.pdf','NPWS walking guide')])

day('day-6','Tue 29 Dec',6,'Jindabyne to Sydney, with proper breaks','Home · no overnight','Longest driving day · no sightseeing commitments','Via Cooma, Canberra and Goulburn · roughly 5½–6½ hr driving, potentially 7–9 hr elapsed with baby breaks and holiday traffic',[
('Morning','Check out after breakfast and drive north through Cooma towards Canberra. Take feeding, nappy and leg-stretch breaks whenever needed.'),
('Lunch','Choose a practical Canberra stop for lunch, then another substantial break around Goulburn. Keep the day free of booked attractions.'),
('Afternoon','Continue to Sydney, allowing for holiday traffic. The five-night trip ends at home on 29 December.')],
'This is the main tradeoff of the shorter trip. If the drive feels too long with your baby, a sixth night in Canberra can split it, returning home on 30 December. That would be a driving break rather than another sightseeing day; it is not included in the five-night accommodation total. All driving times are planning allowances rather than live routing estimates.',
ps('jindabyne','cooma','goulburn'), [('https://www.livetraffic.com/','Check roads before departure')])

climate_sources = {
    'canberra': ('Canberra Airport', 'https://www.bom.gov.au/climate/averages/tables/cw_070351.shtml'),
    'jindabyne': ('Cooma Airport regional reference', 'https://www.bom.gov.au/climate/averages/tables/cw_070217.shtml'),
    'alpine': ('Thredbo Top Station reference', 'https://www.bom.gov.au/climate/averages/tables/cw_071032.shtml'),
}
weather = {
    'day-1': ('Canberra: average high ~27°C / low ~12°C · cool early and late', ['canberra']),
    'day-2': ('Canberra: average high ~27°C / low ~12°C · cool early and late', ['canberra']),
    'day-3': ('Canberra ~27°C / 12°C → Jindabyne region ~24°C / 9°C · average high / low', ['canberra', 'jindabyne']),
    'day-4': ('Lift-top reference: average high ~14°C / low ~5°C · wind, rain and sudden cold possible', ['alpine']),
    'day-5': ('Alpine reference ~14°C / 5°C; lower regional reference ~24°C / 9°C · average high / low; local conditions vary', ['alpine', 'jindabyne']),
    'day-6': ('Jindabyne region: average high ~24°C / low ~9°C · conditions change along the route north', ['jindabyne']),
}

def render_day(d):
    swap=f'<aside class="swap"><strong>{e(d["swap"][0])}</strong><p>{e(d["swap"][1])}</p></aside>' if d['swap'] else ''
    weather_text, sources = weather[d['id']]
    weather_links = ' · '.join(a(climate_sources[key][1], climate_sources[key][0]) for key in sources)
    return f'''<article class="day" id="{d['id']}">
<div class="day-heading-layout"><div><span class="date-line">{d['date']} · Day {d['num']}</span><h3>{e(d['title'])}</h3></div><aside class="day-heading-meta"><div class="header-weather"><span class="header-meta-label">Typical weather · not a forecast</span>{e(weather_text)}<div class="weather-sources">{weather_links}</div></div><div class="header-effort"><span class="header-meta-label">Walking and pace</span>{e(d['effort'])}</div><div class="header-stay"><span class="header-meta-label">Overnight</span>{e(d['stay'])}</div></aside></div>
{gallery(d['images'],d['title']+' photographs')}<p class="drive">{e(d['drive'])}</p><ul class="schedule">{''.join('<li><strong>'+e(k)+':</strong> '+e(v)+'</li>' for k,v in d['items'])}</ul><p class="day-note">{e(d['note'])}</p>{swap}<div class="links">{''.join(a(url,label) for url,label in d['links'])}{maps(d['title'].split(',')[0])}</div></article>'''

def jump(d):
    return f'<li><a href="#{d["id"]}"><img src="{e(d["images"][0]["url"],quote=True)}" loading="lazy" alt="" width="88" height="66"><span class="index-copy"><time>{d["date"]} · Day {d["num"]}</time><strong>{e(d["title"])}</strong></span><span class="index-arrow" aria-hidden="true">›</span></a></li>'

checklist=[
('Book the five overnight stays','Canberra 24–25 Dec, Jindabyne 26–28 Dec. Confirm private bathroom, cot, parking, kitchen, minimum stays and check-in times.'),
('Keep Mount Ainslie on 26 December','Plan 45–60 minutes at the drive-up summit after breakfast, then leave Canberra for Cooma and Jindabyne.'),
('Confirm Thredbo infant and carrier arrangements','For 27 Dec, or 28 Dec if swapping for weather: check the exact lift, loading procedure, operating dates and last return time before buying tickets.'),
('Buy Christmas and picnic supplies','Buy Christmas Day food on 24 Dec, plus feeding supplies, nappies and drinking water. Confirm individual restaurant holiday hours.'),
('Recheck roads and mountain weather','Use NPWS, BOM and Live Traffic NSW. Choose the calmer of 27–28 Dec for the Thredbo lift-top walk.'),
('Pack for the carrier and summer mountains','Warm and waterproof layers for both of you, sun protection, enclosed shoes and picnic supplies. Allow frequent feeding, rest and time out of the carrier.'),
('Plan the long drive home','29 Dec is a driving day with substantial breaks. If needed, book an additional Canberra night and return 30 Dec; that changes the trip to six nights.')]

must=[('ainslie','Mount Ainslie · 26 Dec','day-3'),('arboretum','Arboretum + lake','day-2'),('thredbo','Thredbo + lookout','day-4'),('charlotte','Charlotte Pass','day-5')]

style_extra='''
.route-hero{position:relative}.route-hero img{display:block;width:100%;height:auto;object-fit:contain;border-radius:18px}.route-hero .hero-caption{margin:9px 0 0;font-size:11px;color:var(--muted)}
.day .gallery img,.alt-grid .gallery img{height:auto}
.header-effort{margin-top:14px;color:var(--muted);font-size:13px;line-height:1.6}.weather-sources{font-size:10px;line-height:1.5;margin-top:7px}.weather-sources a{font-size:10px;color:var(--link)}.weather-note{font-size:12px;color:var(--muted);max-width:900px;margin:15px 0 24px}
.route-switch{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 10px}.route-switch button{font:inherit;font-size:13px;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:22px;padding:10px 17px;cursor:pointer}.route-switch button[aria-pressed=true]{background:#d8eaf7;color:#10232f;border-color:#d8eaf7}.route-note{font-size:13px;color:var(--muted)}
.must-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:24px 0}.must-card{position:relative;overflow:hidden;border-radius:15px;background:var(--panel);text-decoration:none}.must-card img{width:100%;height:135px;object-fit:cover;display:block}.must-card span{display:block;padding:12px;font-size:13px;font-weight:550}.must-card small{display:block;color:var(--muted);font-size:10px;font-weight:400;margin-top:4px}.must-card:hover{outline:1px solid #a3c9e9}
.photo-link{display:block}.day .gallery figcaption{position:static;width:auto;height:auto;margin:7px 2px;overflow:visible;clip-path:none;white-space:normal;font-size:10px}.day .gallery figcaption a{color:var(--muted)}.photo-link img{transition:filter .2s}.photo-link:hover img{filter:brightness(1.12)}
.swap{border-left:2px solid #91b0c5;padding:13px 18px;margin:20px 0;background:#171e23;border-radius:0 10px 10px 0;font-size:14px}.swap p{margin:6px 0 0;color:#bcc5cf}.links{display:flex;flex-wrap:wrap;gap:8px 18px}.links a{font-size:12px}.trip-index ol{grid-template-rows:repeat(3,auto)}.trip-index li::before,.trip-index li::after{display:none}.trip-index a{gap:18px}
.overview-table{width:100%;border-collapse:collapse;font-size:14px;margin:22px 0}.table-scroll{overflow:auto}.overview-table th,.overview-table td{text-align:left;padding:13px 15px;border-bottom:1px solid var(--line);vertical-align:top}.overview-table th{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.7px}.overview-table td:first-child{font-weight:600}.comparison{min-width:600px}.section-intro{max-width:850px;font-size:15px;color:var(--muted)}.alt-card{padding:25px 0;border-top:1px solid var(--line)}.alt-card h3{font-size:23px}.alt-card p{font-size:14px}.alt-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px}.alt-grid .gallery{grid-template-columns:1fr 1fr}.alt-grid .gallery img{aspect-ratio:1.4;border-radius:14px}.selected-note{border:1px solid var(--line);background:var(--panel);border-radius:16px;padding:20px 23px;margin:22px 0;font-size:14px}.selected-note p:last-child{margin-bottom:0}.check-list{display:grid;grid-template-columns:1fr 1fr;gap:0 30px}.check{padding:19px 0;border-bottom:1px solid var(--line);display:flex;gap:13px;cursor:pointer}.check input{width:18px;height:18px;margin-top:6px;flex:none;accent-color:#a3c9e9}.check strong{font-size:15px;display:block}.check span span{display:block;color:var(--muted);font-size:13px;margin-top:5px}.extension-intro{margin-top:35px}.source-list{font-size:12px;color:var(--muted)}.source-list a{color:var(--muted)}.source-list li{margin:10px 0}.photo-unavailable{object-fit:contain!important;padding:15px;font-size:13px}.route-switch button:focus-visible{outline:2px solid white;outline-offset:3px}[hidden]{display:none!important}
@media(max-width:800px){.route-hero img{height:auto}.must-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.alt-grid{grid-template-columns:1fr}.check-list{grid-template-columns:1fr}}
@media(max-width:480px){.route-hero img{height:auto}.must-card img{height:125px}.must-grid{gap:10px}.route-switch button{font-size:12px;padding:9px 13px}.day .gallery figure{flex-basis:86%}.alt-grid .gallery{display:grid}.alt-grid .gallery figure{min-width:0}.alt-grid .gallery figcaption{font-size:10px}.overview-table td,.overview-table th{padding:10px}.route-note{font-size:12px}}
@media print{.route-switch,.must-grid,.photo-link:after{display:none}.day-heading-layout{grid-template-columns:1.5fr 1fr}.alt-grid{grid-template-columns:1fr 1fr}.route-hero img{height:auto;max-height:600px}.day{break-inside:auto}.day-heading-layout,.gallery{break-inside:avoid}.check-list{grid-template-columns:1fr 1fr}.swap{background:white;border-color:#555}.day .gallery figcaption{font-size:8px}.section{break-inside:auto}}
'''

script='''
(()=>{
 const boxes=[...document.querySelectorAll('[data-check]')],key='act-snowies-trip-2026-five-nights-checklist-v1';
 function update(){document.getElementById('progress').textContent=boxes.filter(b=>b.checked).length+' of '+boxes.length+' items checked'}
 try{const saved=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(saved))boxes.forEach((b,i)=>b.checked=saved[i]===true)}catch{}
 boxes.forEach(b=>b.addEventListener('change',()=>{update();try{localStorage.setItem(key,JSON.stringify(boxes.map(b=>b.checked)))}catch{}}));update();
 document.getElementById('print-trip').addEventListener('click',()=>window.print());
 document.querySelectorAll('img').forEach(img=>img.addEventListener('error',()=>{img.classList.add('photo-unavailable');img.alt+=' — photo unavailable; use the source link';}));
})();
'''

highlights=''.join(f'<a class="must-card" data-place="{key}" href="#{id}"><img src="{e(photos[key][0]["url"],quote=True)}" alt="{e(photos[key][0]["alt"],quote=True)}" width="260" height="135" loading="lazy"><span>{e(label)}<small>Main itinerary</small></span></a>' for key,label,id in must)

alternatives=[]
for title,keys,copy,url in [
('Civic, Braddon and NewActon',['civic','newacton'],'A 2–3-hour city wander and early meal. Braddon suits cafés and small shops; NewActon adds Nishi’s architecture. Choose a precinct on the arrival evening rather than driving between them all.','https://trade.visitcanberra.com.au/Visit/Publications/neighbourhood-guide-city.pdf'),
('Kingston Foreshore',['kingston','kingston'],'Choose waterfront dinner and a pram stroll instead of Braddon. Check Christmas Eve service at your chosen restaurant; normal trading hours are not a holiday guarantee.','https://visitcanberra.com.au/our-neighbourhoods/inner-south/kingston-and-foreshore'),
]:
    imgs=ps(*keys)
    if keys[0]==keys[1]:imgs[1]=photos[keys[0]][1]
    alternatives.append(f'<article class="alt-card"><h3>{e(title)}</h3>{gallery(imgs,title)}<p>{e(copy)}</p>{a(url,"Visitor information")}</article>')

all_photos={p['url']:p for d in days for p in d['images']}
for key in ['civic','newacton','kingston']:
    all_photos.update({p['url']:p for p in photos[key]})

html=f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101010"><meta name="description" content="Five nights from Sydney to Canberra and Kosciuszko, 24–29 December 2026, with Mount Ainslie, Thredbo and Charlotte Pass."><title>Canberra and Kosciuszko road trip · Christmas 2026</title><link rel="stylesheet" href="assets/styles.css?v=five-nights-1"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"></head><body>
<a class="skip" href="#itinerary">Skip to day-by-day itinerary</a><div class="wrap" id="top"><section class="section" id="route"><div class="route-layout"><div><div class="section-label">01 / The big picture</div><h1 id="trip-title">5 nights from Canberra to the mountains</h1><p class="lede" id="trip-dates">24–29 December 2026 · 6 days / 5 nights · Sydney return</p><p class="lede">A Christmas road trip with a one-year-old: Canberra city views, alpine walks and snow-gum scenery. Comfortable stays with private bathrooms, time for naps, and space to change the plan.</p><ol class="route-list"><li><div><strong>Sydney → Goulburn → Canberra</strong><small>24–25 Dec · 2 nights · city evening, Arboretum and lake</small></div></li><li><div><strong>Mount Ainslie → Cooma → Jindabyne</strong><small>26–28 Dec · 3 nights · summit views, Thredbo and Charlotte Pass</small></div></li><li><div><strong>Jindabyne → Canberra → Goulburn → Sydney</strong><small>29 Dec · home after a driving day with proper breaks</small></div></li></ol></div><figure class="route-hero"><a href="assets/route-map.svg" target="_blank" rel="noopener" aria-label="Open full-size road-trip route map"><img src="assets/route-map.svg" alt="Five-night route schematic: Sydney, Goulburn, Canberra, Cooma and Jindabyne, with outings to Thredbo and Charlotte Pass, then return to Sydney" width="760" height="950" fetchpriority="high"></a><figcaption class="hero-caption">Five-night route schematic · approximate driving times · {a('assets/route-map.svg','Open full-size map')}</figcaption></figure></div>
<p class="route-note" id="route-description">2 nights Canberra · 3 nights Jindabyne</p><p class="route-note">Mount Ainslie is a firm stop on 26 December. Thredbo and Charlotte Pass each have their own day, with one Jindabyne base for all three nights.</p><p class="route-note">{a('https://www.google.com/maps/dir/?api=1&origin=Sydney+NSW&destination=Jindabyne+NSW&waypoints=Goulburn+NSW%7CCanberra+ACT%7CMount+Ainslie+Lookout%7CCooma+NSW&travelmode=driving','Open outward driving route')} · {a('https://www.google.com/maps/dir/?api=1&origin=Jindabyne+NSW&destination=Sydney+NSW&waypoints=Cooma+NSW%7CCanberra+ACT%7CGoulburn+NSW&travelmode=driving','Open return driving route')}</p></section></div>
<nav class="nav" aria-label="Main navigation"><div class="wrap nav-inner"><a href="#route">The route</a><a href="#itinerary">Day by day</a><a href="#choices">Other choices</a><a href="#stays">Stays + costs</a><a href="#bookings">Before we go</a><button class="print" id="print-trip" type="button">Print / save PDF</button></div></nav>
<main class="wrap"><section class="section" id="priorities"><h2>Your places to go</h2><p class="section-intro">Tap a destination to jump to its day. Mount Ainslie is planned for 26 December, followed by separate Thredbo and Charlotte Pass outings from Jindabyne.</p><div class="must-grid">{highlights}</div></section>
<section class="section" id="itinerary"><div class="days-header"><h2>2. Your trip, day by day</h2><p class="lede">Choose a date to jump to its plan. Driving times are approximate and exclude sightseeing, traffic and baby breaks. Use the calmest conditions on 27–28 December for your preferred mountain walk. Both mountain days return to the same Jindabyne accommodation, so you can swap them for weather.</p><p class="weather-note">Weather notes show rounded monthly averages, not forecasts. December station averages provide regional references rather than exact trail temperatures. The alpine reference is much cooler than the Jindabyne town reference. Check <a href="https://www.bom.gov.au/nsw/forecasts/" target="_blank" rel="noopener noreferrer">BOM forecasts</a> before travelling.</p></div><nav class="trip-index" aria-label="Daily itinerary index"><ol>{''.join(jump(d) for d in days)}</ol></nav>{''.join(render_day(d) for d in days)}</section>
<section class="section" id="choices"><h2>3. Other choices, without overfilling the day</h2><p class="section-intro">Choose one Canberra neighbourhood for the arrival evening. Keep Mount Ainslie on the departure morning and the two mountain days clear for the main outings.</p><div class="alt-grid">{''.join(alternatives)}</div><details class="sources"><summary>More demanding hikes and other stops we discussed</summary><p><strong>Mount Kosciuszko summit:</strong> about 13km return from the lift top, 4–5 hours before breaks. <strong>Dead Horse Gap:</strong> 5km one-way, Grade 4, 1½–2½ hours; arrange pickup or add the return river walk. <strong>Main Range:</strong> 22km, 7–9 hours and Grade 4. These are larger hiking days rather than easy additions with the carrier. {a('https://www.nationalparks.nsw.gov.au/-/media/visitor/files/pdf/brochures/kosciuszko-national-park/thredbo-perisher-area-walking-tracks-brochure.pdf','NPWS walking guide')}</p><p><strong>Island Bend and Thredbo Diggings:</strong> riverside picnic alternatives if you want a quieter mountain day. <strong>Mount Kosciuszko summit:</strong> keep this as a larger hike to evaluate for a future trip rather than adding it to the five-night plan.</p><p><strong>Gibraltar Peak and Camels Hump:</strong> steep Tidbinbilla hikes with scrambling; choose The Sanctuary for a gentler visit. <strong>Gibraltar Falls:</strong> leave off the December route; the walking track and platform are currently closed until early 2027. {a('https://www.parks.act.gov.au/find-a-nature-park/namadgi-national-park/gibraltar-falls','Current closure')}</p></details></section>
<section class="section" id="stays"><h2>4. Five nights: stays and costs</h2><p class="section-intro">Comfortable budget studios, motels or ensuite cabins, with a private bathroom in the exact room category. These AUD planning targets assume two adults and one infant, using your own car; those party and car assumptions are still to confirm. No date-specific availability or prices have been checked.</p><div class="table-scroll"><table class="overview-table comparison"><thead><tr><th>Base</th><th>Nights</th><th>Target / night</th><th>Stay allowance</th></tr></thead><tbody><tr><td>Canberra</td><td>24–25 Dec · 2 nights</td><td>$160–230</td><td>$320–460 · {a('https://yourabode.abodehotels.com.au/woden/','Abode Woden')} / {a('https://aliviotouristparkcanberra.com.au/accommodation/cabins/','Alivio ensuite cabins')}</td></tr><tr><td>Jindabyne</td><td>26–28 Dec · 3 nights</td><td>$200–320</td><td>$600–960 · {a('https://www.discoveryholidayparks.com.au/caravan-parks/new-south-wales/snowy-mountains/jindabyne','Ensuite cabins')} / self-contained apartments</td></tr><tr><td>Total accommodation</td><td>5 nights</td><td colspan="2">$920–1,420 · planning allowance, not a quote</td></tr></tbody></table></div><p class="day-note">Confirm Christmas minimum stays, cot space, parking, kitchen facilities, private bathroom and cancellation terms before booking. Food, fuel, activities and park entry are additional. Staying in Jindabyne for all three mountain nights avoids another accommodation change.</p><div class="selected-note"><strong>Own car + private-bathroom stays remains the starting point.</strong><p>Compare the $920–1,420 accommodation allowance with an exact-date campervan quote including hire, child restraint, sites, fuel and extras. A campervan needs a confirmed child-restraint position and infant sleeping arrangement; earlier longer-trip totals no longer apply.</p><p>If the 29 December drive is too long, an additional Canberra night can split the journey, returning home on 30 December. That optional sixth night is outside this total.</p></div></section>
<section class="section" id="bookings"><h2>5. Before we go</h2><p class="section-intro">Start with the five overnight stays, then confirm lift arrangements and the drive home. This checklist is saved only in this browser; ticks do not make bookings or sync between people.</p><p class="counter" id="progress" role="status">0 of {len(checklist)} items checked</p><div class="check-list">{''.join(f'<label class="check"><input type="checkbox" data-check="{i}"><span><strong>{e(title)}</strong><span>{e(copy)}</span></span></label>' for i,(title,copy) in enumerate(checklist))}</div><div class="practical"><article><h3>Christmas opening hours</h3><div class="practical-copy"><p>Buy Christmas food and feeding supplies on 24 December. Arboretum grounds remain the outdoor Christmas Day choice, with the café and visitor centre closed. Confirm individual restaurants and accommodation reception hours before arrival.</p>{a('https://www.nationalarboretum.act.gov.au/visit/opening-hours','Arboretum holiday hours')}</div></article><article><h3>Small walks, big weather</h3><div class="practical-copy"><p>Summer alpine weather can change quickly. Bring warm, waterproof and sun-protective layers for both you and the baby. Short distance does not imply pram access: steps, wet rock, creek crossings and wind matter. Keep a turnaround option and choose dry, stable footing.</p>{a('https://www.nationalparks.nsw.gov.au/safety/alpine-safety','Alpine safety')} {a('https://www.livetraffic.com/','Live Traffic NSW')}</div></article><article><h3>Five nights, two bases</h3><div class="practical-copy"><p>24–29 December is six calendar days and five nights: two in Canberra and three in Jindabyne. Mount Ainslie is a firm stop on 26 December; Thredbo and Charlotte Pass have separate days. The final day is for driving and substantial breaks. A sixth night would split that drive rather than add sightseeing.</p></div></article></div></section>
<footer class="footer"><h2>Sources and photo credits</h2><p>Five-night route finalised 8 November 2026. Mount Ainslie, Arboretum, Charlotte Pass and lift information rechecked; other venue information was researched on 5 November 2026. Recheck holiday schedules, access, lift operations and weather before departure. Photographs show different seasons and sometimes older facilities; they are not a promise of December conditions. Photos remain hosted by their credited sources.</p><details class="sources"><summary>Photo credits and original pages</summary><ul class="source-list">{''.join('<li>'+a(p['source'],p['alt'])+'</li>' for p in all_photos.values())}</ul></details><p>Style adapted from your {a('https://vitorsei.github.io/nz-trip-itinerary-2026/','New Zealand itinerary')}. {a('https://github.com/vitorsei/act-trip-itinerary-2026','Source repository')} · <a href="#top">Back to top ↑</a></p></footer></main><script src="assets/app.js?v=five-nights-1" defer></script></body></html>'''

(ROOT/'index.html').write_text(html)
css=ROOT/'assets/styles.css'
base=css.read_text().split('/* ACT itinerary additions */')[0]
css.write_text(base.rstrip()+'\n/* ACT itinerary additions */\n'+style_extra)
(ROOT/'assets/app.js').write_text(script)
(ROOT/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#101010"/><path d="M8 48 26 17l10 18 7-11 14 24Z" fill="#a3c9e9"/><path d="m21 26 5-9 6 11-6-3Z" fill="#fff"/></svg>')
(ROOT/'.nojekyll').touch()
print(json.dumps({'days':len(days),'unique_photos':len(all_photos),'html_bytes':len(html.encode())}))

(ROOT/'assets/route-map.svg').write_text(render_route_map())

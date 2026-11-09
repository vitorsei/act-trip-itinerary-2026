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

day('day-1','Fri 25 Dec',1,'Sydney to Canberra, via Goulburn','Canberra · 1 of 2 nights','Easy stops + city evening','About 3½–4 hr driving, before lunch and baby breaks',[
('Morning','Leave Sydney with Christmas food, snacks and feeding supplies bought on 24 December. Break in Goulburn for a picnic and time out of the car; do not depend on cafés or supermarkets opening today.'),
('Afternoon','Check in using the Christmas Day arrival arrangements confirmed with your accommodation. Have a short Civic or Braddon wander if you feel like it, then your pre-booked Christmas meal or self-catered dinner.'),
('Evening','Choose one neighbourhood for dinner, then return to your accommodation. Mount Ainslie has its own planned visit on 30 December, during the return Canberra stay.')],
'Christmas Day is now the arrival day. Buy groceries on 24 December in Sydney, confirm reception/key collection and book any restaurant meal ahead. Keep the Goulburn break and Canberra evening flexible. Mount Ainslie is a firm stop on 30 December, on the return journey.',
ps('goulburn','civic','braddon'), [('https://www.parks.act.gov.au/find-a-nature-park/canberra-nature-park/mount-ainslie-nature-reserve','Mount Ainslie access and summit track'),('https://www.nsw.gov.au/visiting-and-exploring-nsw/locations-and-attractions/belmore-park','Belmore Park')],swap=('A different city evening','Choose NewActon’s Nishi architecture or Kingston Foreshore’s waterfront promenade and dinner instead of Braddon. Pick one precinct; Christmas Day restaurant service must be confirmed and booked.'))

day('day-2','Sat 26 Dec',2,'Boxing Day at the Arboretum and the lake','Canberra · 2 of 2 nights','Short walks, picnic and a nap break','Local driving · allow 45–75 min across the day',[
('Morning','Explore the National Arboretum grounds and views around Dairy Farmers Hill. Take a look at the POD playground; its higher climbing pods are mainly for older children.'),
('Midday','Return for lunch and your baby’s nap. Bring picnic supplies and allow for Boxing Day crowds.'),
('Afternoon','Take a short Lake Burley Griffin stroll around Commonwealth Park or the National Carillon. Keep the afternoon flexible around your baby’s nap and the heat; Mount Ainslie is scheduled for the return Canberra stay on 30 December.')],
'The Arboretum visit is now on Boxing Day. Grounds and the POD playground are listed as open daily; confirm individual visitor centre, café and collection holiday hours. Keep this a flexible outdoor day, especially if it is hot.',
ps('arboretum','lake','ainslie'), [('https://www.nationalarboretum.act.gov.au/visit/opening-hours','Arboretum holiday hours'),('https://www.nca.gov.au/attractions/national-carillon','National Carillon')])

day('day-3','Sun 27 Dec',3,'Into the mountains: Bundilla or Meadows','Thredbo · 1 of 3 nights','Choose one · 1.1km easy return or 3km Grade 3 circuit','Canberra → Cooma → Thredbo · about 3–3½ hr driving before baby, charging and walking breaks',[
('Morning','Leave Canberra straight after breakfast, aiming for around 8am if the baby’s routine allows. Use Cooma for a short feeding, toilet and leg-stretch break; no sightseeing stop is planned.'),
('Option A · Bundilla','Stop at Bullocks Flat on the Alpine Way before reaching Thredbo. Walk Bundilla to Bullocks Hut: 1.1km return, Grade 1, 30–90 minutes before baby breaks. Mostly flat river scenery and a picnic, with pram access. Then continue to your Thredbo hotel.'),
('Option B · Meadows','Drive straight to Thredbo, have lunch and check in or leave your bags if the hotel permits. Walk Meadows Nature Track from Valley Terminal: 3km circuit, Grade 3, 1–2 hours before baby breaks. Expect uphill sections, forest, open ski runs and a mossy creek; use the carrier rather than a pram.'),
('Evening','Dinner in Thredbo and an early night. Choose either Bundilla or Meadows, not both; the decision is still open.')],
'Arrival-day choice still undecided: Bundilla is the easier river-and-picnic stop on the approach; Meadows is the more active forest-and-slope walk from Thredbo village. Neither is a high-alpine summit panorama. Mount Ainslie moves to 30 December, and Charlotte Pass keeps its own day on the 29th.',
[photo('https://www.nationalparks.nsw.gov.au/-/media/npws/images/parks/kosciuszko-national-park/thredbo-perisher-area/bundilla-accessible-track/bundilla-accessible-track-02.jpg', 'Thredbo River from Bullocks Hut on the Bundilla outing · Stephen Townsend / DPE', 'https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/bundilla-accessible-track'),photos['thredbo'][0]], [('https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/bundilla-accessible-track','Bundilla route and access'),('https://www.thredbo.com.au/activities/hikes/self-guided-hikes/','Meadows Nature Track'),('https://www.thredbo.com.au/weather/lifts-trails/','Current Thredbo trail status')])

day('day-4','Mon 28 Dec',4,'Thredbo and the Kosciuszko lookout','Thredbo · 2 of 3 nights','4km return · exposed alpine walking','Start from Thredbo village · allow 4–6 hr for the lookout outing; summit option needs the full activity day',[
('Morning','Walk or make a short local transfer from your hotel to Valley Terminal and take the scenic lift, subject to operations and confirmed infant/carrier arrangements.'),
('The walk','Follow the Kosciuszko lookout route: 4km return, about 1–2 hours walking before baby breaks. Enjoy granite formations and open alpine scenery.'),
('Afternoon','Return by lift with a buffer before the last service, then enjoy a relaxed village meal. Keep the rest of the day free.')],
'The lookout is the main plan; choose one of the alternatives below instead if you want a bigger hike or cannot use the chairlift. Confirm infant/carrier access and the last descent directly with Thredbo. Swap the mountain days for weather; lift-free does not mean sheltered from alpine weather.',
[photos['thredbo'][0],photos['lookout'][0],photos['lookout'][1]], [('https://www.thredbo.com.au/activities/gondola-and-chairlift/','Scenic lift information'),('https://www.thredbo.com.au/activities/hikes/self-guided-hikes/','Lookout walk'),('https://www.nationalparks.nsw.gov.au/safety/alpine-safety','Alpine weather planning')])

day('day-5','Tue 29 Dec',5,'Charlotte Pass and the Snow Gums boardwalk','Thredbo · 3 of 3 nights','400m return boardwalk · steps and exposure','About 2½–3½ hr driving return from Thredbo · allow 4–6 hr overall for the boardwalk outing, longer with a hike',[
('Morning','Drive back towards Jindabyne, then take Kosciuszko Road via Perisher to Charlotte Pass for the Snow Gums boardwalk, twisted alpine trees and views towards the Main Range. Allow 15–30 minutes walking before photographs and baby breaks; the boardwalk includes steps and exposed viewpoints.'),
('Lunch','Picnic at Sawpit Creek on the way back down. Keep it a simple picnic stop rather than adding another hike.'),
('Afternoon','Return to the same Thredbo hotel for a nap and an easy evening. Tomorrow’s drive ends in Canberra rather than Sydney.')],
'This is a short walk but a longer driving outing from Thredbo; there is no direct public road across to Charlotte Pass. Short distance still needs warm layers and suitable conditions. Swap 28 and 29 December if that gives the exposed lift-top walk a calmer forecast; both nights are in Thredbo.',
[photos['charlotte'][0],photos['sawpit'][0],photos['charlotte'][1]], [('https://www.nationalparks.nsw.gov.au/things-to-do/lookouts/charlotte-pass-lookout','Charlotte Pass lookout'),('https://www.nationalparks.nsw.gov.au/-/media/visitor/files/pdf/brochures/kosciuszko-national-park/thredbo-perisher-area-walking-tracks-brochure.pdf','NPWS walking guide')])

day('day-6','Wed 30 Dec',6,'Back to Canberra, then Mount Ainslie','Canberra · return stay · 1 night','Drive-up summit · allow 45–60 min at the lookout','Thredbo → Cooma → Canberra · about 3–3½ hr driving, plus breaks and local lookout access',[
('Morning','Have breakfast and leave Thredbo without rushing. Drive north through Jindabyne and Cooma, taking feeding, charging and leg-stretch breaks as needed.'),
('Lunch and rest','Reach Canberra for lunch or the early afternoon, depending on breaks. Check in when the room is available and leave time for a nap.'),
('Late afternoon','Drive to Mount Ainslie summit for the Canberra panorama. Allow 45–60 minutes for photographs and a short wander. This is a firm stop, moved from the outward journey.'),
('Evening','Have dinner near your accommodation. Keep the evening easy; tomorrow is the shorter drive home.')],
'The extra Canberra night splits the return journey. Mount Ainslie is the main attraction today, with no museum or other ticketed visit added. Check current reserve and road access before heading up.',
ps('ainslie','lake','braddon'), [('https://www.parks.act.gov.au/find-a-nature-park/canberra-nature-park/mount-ainslie-nature-reserve','Mount Ainslie summit access'),('https://www.livetraffic.com/','Road conditions')])

day('day-7','Thu 31 Dec',7,'Canberra to Sydney, via Goulburn','Home · no overnight','Travel day · flexible breaks','About 3–3½ hr driving, before baby, charging and holiday traffic breaks',[
('Morning','Check out after breakfast and head towards Sydney. There are no sightseeing commitments today.'),
('On the road','Take a substantial Goulburn break for feeding, lunch or a picnic, plus any other stops the baby needs. Combine charging with a break where possible.'),
('Afternoon','Continue home with a buffer for New Year’s Eve traffic. The six-night trip ends in Sydney on 31 December.')],
'An overnight in Canberra makes this a more manageable drive than travelling directly from Thredbo. Driving times are planning allowances, not live routing estimates.',
ps('civic','goulburn'), [('https://www.livetraffic.com/','Check return traffic')])

climate_sources = {
    'canberra': ('Canberra Airport', 'https://www.bom.gov.au/climate/averages/tables/cw_070351.shtml'),
    'jindabyne': ('Cooma Airport regional reference', 'https://www.bom.gov.au/climate/averages/tables/cw_070217.shtml'),
    'alpine': ('Thredbo Top Station reference', 'https://www.bom.gov.au/climate/averages/tables/cw_071032.shtml'),
}
weather = {
    'day-1': ('Canberra: average high ~27°C / low ~12°C · cool early and late', ['canberra']),
    'day-2': ('Canberra: average high ~27°C / low ~12°C · cool early and late', ['canberra']),
    'day-3': ('Canberra ~27°C / 12°C → upper-mountain reference ~14°C / 5°C; Thredbo village differs from the lift top', ['canberra', 'alpine']),
    'day-4': ('Lift-top reference: average high ~14°C / low ~5°C · wind, rain and sudden cold possible', ['alpine']),
    'day-5': ('Alpine reference ~14°C / 5°C; lower regional reference ~24°C / 9°C · average high / low; local conditions vary', ['alpine', 'jindabyne']),
    'day-6': ('Mountain conditions → Canberra: average high ~27°C / low ~12°C', ['alpine', 'canberra']),
    'day-7': ('Canberra: average high ~27°C / low ~12°C · conditions vary north towards Sydney', ['canberra']),
}

mountain_options = [
    ('Bigger goal · Mount Kosciuszko summit', '13km return · Grade 3 · 4–5 hr walking before baby breaks',
     'Reach Australia’s highest summit from the top of the Kosciuszko Express Chairlift. This replaces the 4km lookout outing and takes the whole activity day; keep the village meal flexible. It can be realistic if you already carry your baby comfortably for several hours, your baby tolerates the carrier and the forecast is settled. The lookout remains an early turnaround.',
     'Confirm infant/carrier lift access first. Take an early lift, agree a firm turnaround time and leave enough margin for the final descent. Published lift hours are currently 9am–4pm, not a confirmed 28 December timetable. Walking up from the village adds a difficult 4km uphill approach taking 2–3 hours before the summit walk; it is not the easy lift-free fallback.',
     [('https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/kosciuszko-walk-thredbo-to-mount-kosciuszko', 'Summit route and approach'), ('https://www.thredbo.com.au/weather/lifts-trails/', 'Lift hours and status')]),
    ('Easy lift-free choice · Bundilla and Bullocks Hut', '1.1km return · Grade 1 · 30–90 min walking',
     'Choose river scenery, snow gums and a picnic around Bullocks Hut instead of the exposed lift-top outing. Bundilla is mostly flat and designed for wheelchair and pram access. Add a village lunch or return to your Thredbo hotel for a nap rather than filling the day with extra hikes.',
     'Access via Bullocks Flat on the Alpine Way, on the Jindabyne–Thredbo corridor. This is a separate walk from the longer Bullocks walking track. Check access alerts and the surface before setting out.',
     [('https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/bundilla-accessible-track', 'Bundilla access and facilities')]),
    ('Scenic ride possibility · Merritts Gondola + village', 'Enclosed gondola · short village strolls · flexible half-day',
     'Thredbo does have an enclosed gondola. If the operator confirms public scenic access with your baby on your date, choose a ride and village lunch instead of the Kosciuszko lookout walk. A short Riverside Walk / Golf Course wander is another village option; choose your turnaround to suit the baby.',
     'The gondola reaches the Cruiser area, not the Kosciuszko Express summit-walk starting point. Confirm 28 December scenic operation, infant and carrier rules, tickets and last return. It is an option to enquire about, not a confirmed booking. The full Thredbo River track is Grade 4 and is not the short village stroll suggested here.',
     [('https://www.thredbo.com.au/activities/gondola/', 'Merritts Gondola'), ('https://www.thredbo.com.au/weather/lifts-trails/', 'Gondola and village trail status')]),
    ('Moderate lift-free hike · Illawong from Guthega', '5km return · Grade 3 · 2–3 hr walking before baby breaks',
     'Follow the Snowy River valley through snow gums towards historic Illawong Hut. Choose this instead of Thredbo if you want a proper mountain walk without a lift. Allow most of the day for the drive, walk, picnic and baby breaks.',
     'Guthega uses a different road approach from Thredbo: return towards Jindabyne, then use Kosciuszko Road and Guthega Road. Check current road and track alerts; uneven ground and creek crossings need care with a carrier. Do not combine it with the summit or a full Charlotte Pass outing.',
     [('https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/illawong-walk', 'Illawong route and access')]),
    ('Mountain views without a lift · Mount Stilwell first lookout', '2km return to first lookout · moderate uphill alpine walking',
     'Use Charlotte Pass as your mountain destination and walk to the first Mount Stilwell lookout for views of the Main Range. Choose the first lookout as the turnaround; the longer summit extension follows an unmarked route. Allow extra time for climbing, photographs and carrier breaks.',
     'This fits most naturally on 29 December alongside the Snow Gums boardwalk. If you choose it on the 28th instead of Thredbo, move the Charlotte Pass visit to this day and use the 29th for Bundilla or a relaxed lake day. Perisher can be a brief roadside stop en route; its operator currently offers no scenic chairlift rides.',
     [('https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/mount-stilwell-walk', 'Mount Stilwell lookout'), ('https://help.perisher.com.au/hc/en-gb/articles/14993153888019-Do-you-offer-Scenic-Chairlift-rides', 'Perisher scenic lift policy')]),
    ('Lowest-effort day · Lake Jindabyne', 'Short foreshore stroll · picnic · flexible turnaround',
     'Drive to Lake Jindabyne for a foreshore wander and lunch, then return to Thredbo; allow about 1–1½ hours driving return before stops. This replaces the mountain outing if the family wants a rest or conditions higher up are poor.',
     'Keep the calmer of 28–29 December for your preferred alpine walk. Both nights remain in Thredbo, so choosing a shorter day does not require changing hotels.',
     [('https://www.visitnsw.com/destinations/snowy-mountains/jindabyne-area/jindabyne', 'Jindabyne visitor information')]),
]

def render_mountain_options():
    cards = ''.join(f'<article class="mountain-option"><h5>{e(title)}</h5><p class="option-effort">{e(effort)}</p><p>{e(copy)}</p><p class="option-logistics">{e(logistics)}</p><div class="links">'+''.join(a(url, label) for url, label in links)+'</div></article>' for title, effort, copy, logistics, links in mountain_options)
    return '<section class="mountain-choices" aria-labelledby="mountain-choices-title"><h4 id="mountain-choices-title">28 December · choose your mountain day</h4><p>The lookout stays the main plan. These are replacements, not extra stops: pick one to suit your carrying experience, the baby, lift access and the forecast. Walking times below exclude feeding, nappy and rest breaks. Access information checked 9 November 2026; recheck before travelling.</p><div class="mountain-options">'+cards+'</div><p class="day-note"><strong>Another summit route:</strong> Charlotte Pass to Kosciuszko is 18.6km return, Grade 3, with a published 6–8 hours walking before baby breaks. It needs no lift, but is a much longer outing and is not the default fallback with your baby. '+a('https://www.nationalparks.nsw.gov.au/things-to-do/walking-tracks/mount-kosciuszko-summit-walk', 'Charlotte Pass summit route')+'</p></section>'

def render_day(d):
    swap=f'<aside class="swap"><strong>{e(d["swap"][0])}</strong><p>{e(d["swap"][1])}</p></aside>' if d['swap'] else ''
    weather_text, sources = weather[d['id']]
    weather_links = ' · '.join(a(climate_sources[key][1], climate_sources[key][0]) for key in sources)
    return f'''<article class="day" id="{d['id']}">
<div class="day-heading-layout"><div><span class="date-line">{d['date']} · Day {d['num']}</span><h3>{e(d['title'])}</h3></div><aside class="day-heading-meta"><div class="header-weather"><span class="header-meta-label">Typical weather · not a forecast</span>{e(weather_text)}<div class="weather-sources">{weather_links}</div></div><div class="header-effort"><span class="header-meta-label">Walking and pace</span>{e(d['effort'])}</div><div class="header-stay"><span class="header-meta-label">Overnight</span>{e(d['stay'])}</div></aside></div>
{gallery(d['images'],d['title']+' photographs')}<p class="drive">{e(d['drive'])}</p><ul class="schedule">{''.join('<li><strong>'+e(k)+':</strong> '+e(v)+'</li>' for k,v in d['items'])}</ul><p class="day-note">{e(d['note'])}</p>{swap}<div class="links">{''.join(a(url,label) for url,label in d['links'])}{maps({'day-1':'Canberra ACT','day-2':'National Arboretum Canberra','day-3':'Thredbo NSW','day-4':'Thredbo Valley Terminal','day-5':'Charlotte Pass lookout','day-6':'Mount Ainslie lookout','day-7':'Goulburn NSW'}[d['id']])}</div>{render_mountain_options() if d['id'] == 'day-4' else ''}</article>'''

def jump(d):
    return f'<li><a href="#{d["id"]}"><img src="{e(d["images"][0]["url"],quote=True)}" loading="lazy" alt="" width="88" height="66"><span class="index-copy"><time>{d["date"]} · Day {d["num"]}</time><strong>{e(d["title"])}</strong></span><span class="index-arrow" aria-hidden="true">›</span></a></li>'

checklist=[
('Book all six overnight stays','Three adults and one infant: Canberra 25–26 Dec, Thredbo 27–29 Dec and Canberra 30 Dec. Confirm adult bed layout, private bathroom, cot, parking, minimum stays and Christmas Day key collection.'),
('Keep Mount Ainslie on 30 December','Allow 45–60 minutes at the drive-up summit after arriving back in Canberra and taking a rest.'),
('Confirm Thredbo infant and carrier arrangements','For 28 Dec, or 29 Dec if swapping for weather: check the exact lift, loading procedure, operating dates and last return time before buying tickets.'),
('Buy Christmas and picnic supplies','Buy Christmas Day food in Sydney on 24 Dec before travelling on the 25th, plus feeding supplies, nappies and drinking water. Confirm individual restaurant holiday hours.'),
('Recheck roads and mountain weather','Use NPWS, BOM and Live Traffic NSW. Choose the calmer of 28–29 Dec for the Thredbo lift-top walk.'),
('Prepare the EQB charging plan','Confirm the EQB 250 model year, start charge and accommodation charger access. Set up Chargefox, myNRMA, Exploren and any other selected operator apps, add payment details yourself, and bring a Type 2 cable. Check live sites and backup stops before leaving.'),
('Pack for the carrier and summer mountains','Warm and waterproof layers for both of you, sun protection, enclosed shoes and picnic supplies. Allow frequent feeding, rest and time out of the carrier.'),
('Choose the 27 December walk','Bundilla / Bullocks Hut or Meadows Nature Track: both remain options. Choose one based on arrival time, energy, weather and the baby’s routine.')]

must=[('ainslie','Mount Ainslie · 30 Dec','day-6'),('arboretum','Arboretum + lake','day-2'),('thredbo','Thredbo + lookout','day-4'),('charlotte','Charlotte Pass','day-5')]

style_extra='''
.mountain-choices{margin-top:32px;padding-top:24px;border-top:1px solid var(--line)}.mountain-choices h4{font-size:25px;margin:0 0 12px}.mountain-choices>p{font-size:14px;color:var(--muted)}.mountain-options{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:18px;margin:24px 0}.mountain-option{padding:22px;border:1px solid var(--line);border-radius:16px;background:var(--panel)}.mountain-option h5{font-size:19px;line-height:1.4;margin:0 0 12px}.mountain-option p{font-size:14px}.mountain-option .option-effort{color:var(--link);font-size:13px}.mountain-option .option-logistics{color:var(--muted);font-size:13px}
.route-hero{position:relative}.route-hero img{display:block;width:100%;height:auto;object-fit:contain;border-radius:18px}.route-hero .hero-caption{margin:9px 0 0;font-size:11px;color:var(--muted)}
.day .gallery img,.alt-grid .gallery img{height:auto}
.header-effort{margin-top:14px;color:var(--muted);font-size:13px;line-height:1.6}.weather-sources{font-size:10px;line-height:1.5;margin-top:7px}.weather-sources a{font-size:10px;color:var(--link)}.weather-note{font-size:12px;color:var(--muted);max-width:900px;margin:15px 0 24px}
.route-switch{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 10px}.route-switch button{font:inherit;font-size:13px;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:22px;padding:10px 17px;cursor:pointer}.route-switch button[aria-pressed=true]{background:#d8eaf7;color:#10232f;border-color:#d8eaf7}.route-note{font-size:13px;color:var(--muted)}
.must-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:24px 0}.must-card{position:relative;overflow:hidden;border-radius:15px;background:var(--panel);text-decoration:none}.must-card img{width:100%;height:135px;object-fit:cover;display:block}.must-card span{display:block;padding:12px;font-size:13px;font-weight:550}.must-card small{display:block;color:var(--muted);font-size:10px;font-weight:400;margin-top:4px}.must-card:hover{outline:1px solid #a3c9e9}
.photo-link{display:block}.day .gallery figcaption{position:static;width:auto;height:auto;margin:7px 2px;overflow:visible;clip-path:none;white-space:normal;font-size:10px}.day .gallery figcaption a{color:var(--muted)}.photo-link img{transition:filter .2s}.photo-link:hover img{filter:brightness(1.12)}
.swap{border-left:2px solid #91b0c5;padding:13px 18px;margin:20px 0;background:#171e23;border-radius:0 10px 10px 0;font-size:14px}.swap p{margin:6px 0 0;color:#bcc5cf}.links{display:flex;flex-wrap:wrap;gap:8px 18px}.links a{font-size:12px}.trip-index ol{grid-template-rows:repeat(4,auto)}.trip-index li::before,.trip-index li::after{display:none}.trip-index a{gap:18px}
.overview-table{width:100%;border-collapse:collapse;font-size:14px;margin:22px 0}.table-scroll{overflow:auto}.overview-table th,.overview-table td{text-align:left;padding:13px 15px;border-bottom:1px solid var(--line);vertical-align:top}.overview-table th{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.7px}.overview-table td:first-child{font-weight:600}.comparison{min-width:600px}.section-intro{max-width:850px;font-size:15px;color:var(--muted)}.alt-card{padding:25px 0;border-top:1px solid var(--line)}.alt-card h3{font-size:23px}.alt-card p{font-size:14px}.alt-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px}.alt-grid .gallery{grid-template-columns:1fr 1fr}.alt-grid .gallery img{aspect-ratio:1.4;border-radius:14px}.selected-note{border:1px solid var(--line);background:var(--panel);border-radius:16px;padding:20px 23px;margin:22px 0;font-size:14px}.selected-note p:last-child{margin-bottom:0}.check-list{display:grid;grid-template-columns:1fr 1fr;gap:0 30px}.check{padding:19px 0;border-bottom:1px solid var(--line);display:flex;gap:13px;cursor:pointer}.check input{width:18px;height:18px;margin-top:6px;flex:none;accent-color:#a3c9e9}.check strong{font-size:15px;display:block}.check span span{display:block;color:var(--muted);font-size:13px;margin-top:5px}.extension-intro{margin-top:35px}.source-list{font-size:12px;color:var(--muted)}.source-list a{color:var(--muted)}.source-list li{margin:10px 0}.photo-unavailable{object-fit:contain!important;padding:15px;font-size:13px}.route-switch button:focus-visible{outline:2px solid white;outline-offset:3px}[hidden]{display:none!important}
@media(max-width:800px){.route-hero img{height:auto}.must-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.alt-grid{grid-template-columns:1fr}.check-list{grid-template-columns:1fr}}
@media(max-width:480px){.route-hero img{height:auto}.must-card img{height:125px}.must-grid{gap:10px}.route-switch button{font-size:12px;padding:9px 13px}.day .gallery figure{flex-basis:86%}.alt-grid .gallery{display:grid}.alt-grid .gallery figure{min-width:0}.alt-grid .gallery figcaption{font-size:10px}.overview-table td,.overview-table th{padding:10px}.route-note{font-size:12px}}
@media print{.route-switch,.must-grid,.photo-link:after{display:none}.day-heading-layout{grid-template-columns:1.5fr 1fr}.alt-grid{grid-template-columns:1fr 1fr}.route-hero img{height:auto;max-height:600px}.day{break-inside:auto}.day-heading-layout,.gallery{break-inside:avoid}.check-list{grid-template-columns:1fr 1fr}.swap{background:white;border-color:#555}.day .gallery figcaption{font-size:8px}.section{break-inside:auto}}
'''

script='''
(()=>{
 const boxes=[...document.querySelectorAll('[data-check]')],key='act-snowies-trip-2026-six-nights-thredbo-checklist-v1';
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
('Civic, Braddon and NewActon',['civic','newacton'],'A short arrival-day city wander, or a 2–3-hour visit after the lake on Boxing Day. Braddon suits cafés and small shops; NewActon adds Nishi’s architecture. Choose a precinct on the arrival evening rather than driving between them all.','https://trade.visitcanberra.com.au/Visit/Publications/neighbourhood-guide-city.pdf'),
('Kingston Foreshore',['kingston','kingston'],'Choose waterfront dinner and a pram stroll instead of Braddon. Book ahead if eating here on Christmas Day; normal trading hours are not a holiday guarantee.','https://visitcanberra.com.au/our-neighbourhoods/inner-south/kingston-and-foreshore'),
]:
    imgs=ps(*keys)
    if keys[0]==keys[1]:imgs[1]=photos[keys[0]][1]
    alternatives.append(f'<article class="alt-card"><h3>{e(title)}</h3>{gallery(imgs,title)}<p>{e(copy)}</p>{a(url,"Visitor information")}</article>')

all_photos={p['url']:p for d in days for p in d['images']}
for key in ['civic','newacton','kingston']:
    all_photos.update({p['url']:p for p in photos[key]})

html=f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101010"><meta name="description" content="Six nights from Sydney to Canberra and Kosciuszko, 25–31 December 2026, with Mount Ainslie, Thredbo and Charlotte Pass."><title>Canberra and Kosciuszko road trip · Christmas 2026</title><link rel="stylesheet" href="assets/styles.css?v=thredbo-six-nights-1"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"></head><body>
<a class="skip" href="#itinerary">Skip to day-by-day itinerary</a><div class="wrap" id="top"><section class="section" id="route"><div class="route-layout"><div><div class="section-label">01 / The big picture</div><h1 id="trip-title">6 nights from Canberra to the mountains</h1><p class="lede" id="trip-dates">25–31 December 2026 · 7 days / 6 nights · Sydney return</p><p class="lede">A Christmas road trip with a one-year-old: Canberra city views, alpine walks and snow-gum scenery. Comfortable stays with private bathrooms, time for naps, and room for three adults plus your baby. Travelling in your Mercedes EQB 250.</p><ol class="route-list"><li><div><strong>Sydney → Goulburn → Canberra</strong><small>25–26 Dec · 2 nights · city evening, Arboretum and lake</small></div></li><li><div><strong>Canberra → Cooma → Thredbo</strong><small>27–29 Dec · 3 nights · Bundilla or Meadows, Kosciuszko and Charlotte Pass</small></div></li><li><div><strong>Thredbo → Canberra → Sydney</strong><small>30 Dec · Canberra night + Mount Ainslie · home 31 Dec</small></div></li></ol></div><figure class="route-hero"><a href="assets/route-map.svg?v=thredbo-six-nights-1" target="_blank" rel="noopener" aria-label="Open full-size road-trip route map"><img src="assets/route-map.svg?v=thredbo-six-nights-1" alt="Six-night route schematic: Sydney, Goulburn, Canberra, Cooma and Thredbo, with Charlotte Pass outing and a return Canberra night before Sydney" width="760" height="1000" fetchpriority="high"></a><figcaption class="hero-caption">Six-night route schematic · approximate driving times · {a('assets/route-map.svg?v=thredbo-six-nights-1','Open full-size map')}</figcaption></figure></div>
<p class="route-note" id="route-description">2 nights Canberra · 3 nights Thredbo · 1 return night Canberra</p><p class="route-note">Mount Ainslie is a firm stop on 30 December, during the return Canberra stay. Choose Bundilla or Meadows on the 27th; Kosciuszko and Charlotte Pass keep separate days from the Thredbo base.</p><p class="route-note">{a('https://www.google.com/maps/dir/?api=1&origin=Sydney+NSW&destination=Thredbo+NSW&waypoints=Goulburn+NSW%7CCanberra+ACT%7CCooma+NSW&travelmode=driving','Open outward driving route')} · {a('https://www.google.com/maps/dir/?api=1&origin=Thredbo+NSW&destination=Sydney+NSW&waypoints=Cooma+NSW%7CMount+Ainslie+Lookout%7CCanberra+ACT%7CGoulburn+NSW&travelmode=driving','Open return driving route')}</p></section></div>
<nav class="nav" aria-label="Main navigation"><div class="wrap nav-inner"><a href="#route">The route</a><a href="#itinerary">Day by day</a><a href="#choices">Other choices</a><a href="#stays">Stays + costs</a><a href="#bookings">Before we go</a><button class="print" id="print-trip" type="button">Print / save PDF</button></div></nav>
<main class="wrap"><section class="section" id="priorities"><h2>Your places to go</h2><p class="section-intro">Tap a destination to jump to its day. Thredbo is your mountain base for 27–30 December. Mount Ainslie is planned for the return Canberra stay on 30 December.</p><div class="must-grid">{highlights}</div></section>
<section class="section" id="itinerary"><div class="days-header"><h2>2. Your trip, day by day</h2><p class="lede">Choose a date to jump to its plan. Driving times are approximate and exclude sightseeing, traffic and baby breaks. Use the calmest conditions on 28–29 December for your preferred mountain walk. Both mountain days return to the same Thredbo hotel, so you can swap them for weather.</p><p class="weather-note">Weather notes show rounded monthly averages, not forecasts. December station averages provide regional references rather than exact trail temperatures. The alpine reference is much cooler than the Jindabyne town reference. Check <a href="https://www.bom.gov.au/nsw/forecasts/" target="_blank" rel="noopener noreferrer">BOM forecasts</a> before travelling.</p></div><nav class="trip-index" aria-label="Daily itinerary index"><ol>{''.join(jump(d) for d in days)}</ol></nav>{''.join(render_day(d) for d in days)}</section>
<section class="section" id="choices"><h2>3. Other choices, without overfilling the day</h2><p class="section-intro">Choose one Canberra neighbourhood for the arrival evening. Keep Mount Ainslie on 30 December and the two full mountain days clear for the main outings.</p><div class="alt-grid">{''.join(alternatives)}</div><details class="sources"><summary>More demanding hikes and other stops we discussed</summary><p><strong>Mount Kosciuszko summit:</strong> about 13km return from the lift top, 4–5 hours before breaks. <strong>Dead Horse Gap:</strong> 5km one-way, Grade 4, 1½–2½ hours; arrange pickup or add the return river walk. <strong>Main Range:</strong> 22km, 7–9 hours and Grade 4. These are larger hiking days rather than easy additions with the carrier. {a('https://www.nationalparks.nsw.gov.au/-/media/visitor/files/pdf/brochures/kosciuszko-national-park/thredbo-perisher-area-walking-tracks-brochure.pdf','NPWS walking guide')}</p><p><strong>Island Bend and Thredbo Diggings:</strong> riverside picnic alternatives if you want a quieter mountain day. The summit and lift-free mountain alternatives are compared in the 28 December plan above; choose one rather than adding several hikes to the same day.</p><p><strong>Gibraltar Peak and Camels Hump:</strong> steep Tidbinbilla hikes with scrambling; choose The Sanctuary for a gentler visit. <strong>Gibraltar Falls:</strong> leave off the December route; the walking track and platform are currently closed until early 2027. {a('https://www.parks.act.gov.au/find-a-nature-park/namadgi-national-park/gibraltar-falls','Current closure')}</p></details></section>
<section class="section" id="stays"><h2>4. Stays and charging for the EQB</h2><p class="section-intro">Three adults and your one-year-old, travelling in a Mercedes EQB 250. Canberra: check in 25 December, check out 27 December. Thredbo: check in 27 December, check out 30 December. Return Canberra stay: check in 30 December, check out 31 December. A two-bedroom apartment or cabin with a private bathroom is a useful starting point. The table below retains the initial Canberra search. Those prices cover only 25–27 December, not the extra return night or Thredbo. Prices are AUD totals, searched for three adults and one child aged one on 8 November 2026. Taxes and charges are included as displayed; parking and cot arrangements need checking at checkout.</p>
<h3>Canberra · 25–27 December · two nights</h3>
<div class="table-scroll"><table class="overview-table comparison"><thead><tr><th>Stay</th><th>Layout</th><th>Total / per night</th><th>Trade-off</th></tr></thead><tbody>
<tr><td>{a('https://www.booking.com/hotel/au/mercure-canberra-belconnen.en-gb.html?checkin=2026-12-25&checkout=2026-12-27&group_adults=3&group_children=1&age=1&no_rooms=1','Mercure Canberra Belconnen')}</td><td>One Superior Queen Room with two queen beds</td><td>$380 / $190</td><td>Lowest shortlisted shared-room price; everyone sleeps in one room. Charging unverified.</td></tr>
<tr><td>{a('https://www.booking.com/hotel/au/abode-narrabundah.en-gb.html?checkin=2026-12-25&checkout=2026-12-27&group_adults=3&group_children=1&age=1&no_rooms=1','Punthill Narrabundah')}</td><td>Two Bedroom Apartment – Open Plan</td><td>$433 / $216.50</td><td>Best initial apartment price. Check bedroom separation, beds and cot; charging unverified.</td></tr>
<tr><td>{a('https://www.booking.com/hotel/au/forrest-apartments.en-gb.html?checkin=2026-12-25&checkout=2026-12-27&group_adults=3&group_children=1&age=1&no_rooms=2','Forrest Hotel & Apartments')}</td><td>Two separate Queen Rooms</td><td>$496 / $248 combined</td><td>Separate sleeping rooms for $63 more than Punthill across both nights. Connecting rooms not confirmed.</td></tr>
<tr><td>{a('https://www.booking.com/hotel/au/alivio-tourist-park.en-gb.html?checkin=2026-12-25&checkout=2026-12-27&group_adults=3&group_children=1&age=1&no_rooms=1','Alivio Ridge View Cabin')}</td><td>Two bedrooms, two doubles plus a single bunk; kitchen and private bathroom</td><td>$548 / $274</td><td>Cabin alternative with space to cook. Confirm cot space. On-site charging unverified.</td></tr>
<tr><td>{a('https://www.booking.com/hotel/au/medina-executive-james-court.en-gb.html?checkin=2026-12-25&checkout=2026-12-27&group_adults=3&group_children=1&age=1&no_rooms=1','Adina James Court')}</td><td>Two-bedroom apartment, queen + two singles, two bathrooms, kitchen</td><td>$628 / $314</td><td>Central base with clearer adult bed separation; charging unverified.</td></tr>
</tbody></table></div>
<h3>Thredbo · 27–30 December · three nights</h3>
<p>Your chosen mountain base is now Thredbo because you prefer the hotel options. The exact property is still to be added. Confirm the room fits three adults and an infant, private bathroom, cot, parking, distance or steps to Valley Terminal and any breakfast or kitchen facilities. {a('https://www.thredbo.com.au/accommodation/','Thredbo accommodation')}</p>
<h3>Canberra return · 30–31 December · one night</h3>
<p>Book one additional Canberra night to split the drive home, with Mount Ainslie planned after arrival and a rest. Reusing your first hotel may simplify arrival, but this is a separate stay and needs its own price and availability check.</p>
<p class="day-note"><strong>Six-night cost:</strong> initial Canberra stay + three Thredbo nights + one return Canberra night. Thredbo and 30 December have not been priced in this version, so the former five-night Jindabyne totals no longer apply. No accommodation is booked by this page.</p>
<div class="selected-note"><strong>Charging plan · confirm live sites in the operator apps</strong><p>This is a provisional stop plan, not a calculated battery itinerary. Your EQB 250 uses CCS2 DC and Type 2 AC charging, with up to 100kW DC and 11kW AC according to the Australian AEVA model sheet. A 22kW AC post will therefore supply at most the car’s 11kW AC limit. Model year, starting charge, terrain and load still affect the battery plan. Bring your Type 2 cable for socketed AC chargers. {a('https://aeva.asn.au/files/3836/','Australian EQB charging specifications')}</p>
<ul><li><strong>25 December · Sydney → Goulburn → Canberra:</strong> start well charged and combine the Goulburn picnic break with a DC top-up if needed. Candidate: Chargefox/NRMA Gateway Service Station, 53 Sydney Road. Verify current plug, access and status in the app; Christmas Day café and toilet access can differ from charger access. {a('https://www.goulburnaustralia.com.au/wp-content/uploads/2025/03/EV-Brochure_DL-20250327.pdf','Goulburn charging locations')}</li>
<li><strong>Canberra · 25–27 December:</strong> charge at your stay if confirmed, or top up at a compatible public fast charger before departing on the 27th. Hotel parking does not itself imply charging access.</li>
<li><strong>27 December · Cooma break:</strong> candidate DC top-up at the Chargefox site at Snowy Hydro Discovery Centre, Yulin Avenue. Check the current listing in Chargefox; the charging stop does not add a Discovery Centre tour. A Tesla site is a backup only if the Tesla app shows it accepts your EQB.</li>
<li><strong>Thredbo · 27–30 December:</strong> confirm approved hotel charging, plug type and access before relying on it. Jindabyne is an en-route backup: check the NRMA CCS2 site at Snowy River Avenue / Kalkite Street in the operator app. Charge before driving up to Thredbo if hotel charging is unavailable; do not depend on a charger at a trailhead.</li>
<li><strong>30–31 December · return:</strong> leave Thredbo with enough charge to reach a verified backup. Use Cooma or Canberra on the 30th, then Canberra or Goulburn on the 31st as needed, guided by the EQB navigation and live charger status. Charging and queues are extra to the driving allowances; combine them with feeding and meal breaks.</li></ul>
<p>{a('https://www.mynrma.com.au/open-road/advice-and-how-to/ev-charging-stations-australia','Networks and apps')} · {a('https://www.service.nsw.gov.au/referral/find-an-electric-vehicle-charging-station','NSW charger map')} · {a('https://www.tesla.com/support/charging/supercharging','Tesla access for other EVs')}</p>
</div></section>
<section class="section" id="bookings"><h2>5. Before we go</h2><p class="section-intro">Start with the six overnight stays, then confirm lift arrangements and the drive home. This checklist is saved only in this browser; ticks do not make bookings or sync between people.</p><p class="counter" id="progress" role="status">0 of {len(checklist)} items checked</p><div class="check-list">{''.join(f'<label class="check"><input type="checkbox" data-check="{i}"><span><strong>{e(title)}</strong><span>{e(copy)}</span></span></label>' for i,(title,copy) in enumerate(checklist))}</div><div class="practical"><article><h3>Christmas opening hours</h3><div class="practical-copy"><p>Buy Christmas food and feeding supplies in Sydney on 24 December, before the Christmas Day departure. Confirm accommodation key collection and book any Christmas restaurant meal. The Arboretum visit is on Boxing Day; check its venue-specific holiday hours.</p>{a('https://www.nationalarboretum.act.gov.au/visit/opening-hours','Arboretum holiday hours')}</div></article><article><h3>Small walks, big weather</h3><div class="practical-copy"><p>Summer alpine weather can change quickly. Bring warm, waterproof and sun-protective layers for both you and the baby. Short distance does not imply pram access: steps, wet rock, creek crossings and wind matter. Keep a turnaround option and choose dry, stable footing.</p>{a('https://www.nationalparks.nsw.gov.au/safety/alpine-safety','Alpine safety')} {a('https://www.livetraffic.com/','Live Traffic NSW')}</div></article><article><h3>Six nights, two destinations</h3><div class="practical-copy"><p>25–31 December is seven calendar days and six nights: Canberra 25–26 December, Thredbo 27–29 December and Canberra again on 30 December. Mount Ainslie is a firm stop on the return stay. Bundilla versus Meadows on the 27th is still undecided; Charlotte Pass stays on the 29th.</p></div></article></div></section>
<footer class="footer"><h2>Sources and photo credits</h2><p>Six-night Thredbo route updated 9 November 2026. Mount Ainslie, Arboretum, Charlotte Pass and lift information rechecked; other venue information was researched on 5 November 2026. Recheck holiday schedules, access, lift operations and weather before departure. Photographs show different seasons and sometimes older facilities; they are not a promise of December conditions. Photos remain hosted by their credited sources.</p><details class="sources"><summary>Photo credits and original pages</summary><ul class="source-list">{''.join('<li>'+a(p['source'],p['alt'])+'</li>' for p in all_photos.values())}</ul></details><p>Style adapted from your {a('https://vitorsei.github.io/nz-trip-itinerary-2026/','New Zealand itinerary')}. {a('https://github.com/vitorsei/act-trip-itinerary-2026','Source repository')} · <a href="#top">Back to top ↑</a></p></footer></main><script src="assets/app.js?v=thredbo-six-nights-1" defer></script></body></html>'''

(ROOT/'index.html').write_text(html)
css=ROOT/'assets/styles.css'
base=css.read_text().split('/* ACT itinerary additions */')[0]
css.write_text(base.rstrip()+'\n/* ACT itinerary additions */\n'+style_extra)
(ROOT/'assets/app.js').write_text(script)
(ROOT/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#101010"/><path d="M8 48 26 17l10 18 7-11 14 24Z" fill="#a3c9e9"/><path d="m21 26 5-9 6 11-6-3Z" fill="#fff"/></svg>')
(ROOT/'.nojekyll').touch()
print(json.dumps({'days':len(days),'unique_photos':len(all_photos),'html_bytes':len(html.encode())}))

(ROOT/'assets/route-map.svg').write_text(render_route_map())

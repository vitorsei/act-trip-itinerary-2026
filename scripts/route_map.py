from html import escape


def render_route_map():
    nodes = [
        (645, 86, 'Sydney', 621, 60, 'end', True),
        (397, 240, 'Goulburn', 417, 244, 'start', False),
        (332, 334, 'Canberra', 353, 339, 'start', True),
        (354, 445, 'Cooma', 376, 450, 'start', False),
        (288, 530, 'Jindabyne', 313, 540, 'start', False),
        (137, 566, 'Thredbo', 113, 593, 'middle', True),
        (148, 480, 'Charlotte Pass', 126, 459, 'middle', False),
        (230, 300, 'Arboretum', 210, 280, 'end', False),
        (240, 365, 'Lake Burley Griffin', 210, 405, 'middle', False),
        (390, 280, 'Mount Ainslie', 414, 276, 'start', False),
    ]
    markers = ''.join(f'<circle cx="{x}" cy="{y}" r="{9 if stay else 5}" fill="{"#09152b" if stay else "#f4f6fc"}" stroke="{"#d6e3f2" if stay else "#f4f6fc"}" stroke-width="3"/><text x="{tx}" y="{ty}" text-anchor="{anchor}" class="place">{escape(label)}</text>' for x, y, label, tx, ty, anchor, stay in nodes)
    rows = [
        ('#31d5ec', '25 Dec · D1', 'Sydney → Goulburn → Canberra', '3½–4 hr'),
        ('#f4d35e', '26 Dec · D2', 'Arboretum + lake · local driving', '45–75 min'),
        ('#95df8e', '27 Dec · D3', 'Canberra → Cooma → Thredbo', '3–3½ hr'),
        ('#bca5ff', '28 Dec · D4', 'Thredbo · Kosciuszko lift / walk', 'Local'),
        ('#f18bb6', '29 Dec · D5', 'Thredbo ↔ Charlotte Pass · return', '2½–3½ hr'),
        ('#ffad62', '30 Dec · D6', 'Thredbo → Canberra + Mount Ainslie', '3–3½ hr*'),
        ('#71b9ff', '31 Dec · D7', 'Canberra → Goulburn → Sydney', '3–3½ hr'),
    ]
    timings = ''.join(f'<path d="M38 {681+i*34}h25" stroke="{colour}" stroke-width="4" stroke-linecap="round"/><text x="79" y="{686+i*34}" class="date">{date}</text><text x="190" y="{686+i*34}" class="timing">{escape(label)}</text><text x="721" y="{686+i*34}" text-anchor="end" class="timing">{time}</text>' for i, (colour, date, label, time) in enumerate(rows))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1000" role="img" aria-labelledby="title desc">
<title id="title">Six-night Sydney to Kosciuszko route schematic</title><desc id="desc">25–31 December 2026. Canberra 25–26 December, Thredbo 27–29 December and Canberra again on 30 December. Choose Bundilla or Meadows on arrival. Kosciuszko and Charlotte Pass have separate days. Mount Ainslie on 30 December, home 31 December. Each day has its own colour. Schematic, not to scale. Driving times exclude stops.</desc>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#071027"/><stop offset="1" stop-color="#101e35"/></linearGradient><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="#31d5ec"/></marker></defs>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:#f2f5fb}}.place{{font-size:18px;font-weight:600;paint-order:stroke;stroke:#0b172c;stroke-width:5px;stroke-linejoin:round}}.timing{{font-size:16px}}.date{{font-size:15px;font-weight:700}}.muted{{fill:#aebed3;font-size:15px}}.heading{{font-size:22px;font-weight:700}}</style>
<rect width="760" height="1000" rx="24" fill="url(#bg)"/>
<path d="M36 563C35 385 122 313 151 188S326 112 434 68 660 87 689 236 531 384 458 505 288 634 36 563Z" fill="#152c40" opacity=".55"/>
<g fill="none" stroke="#385067" opacity=".23"><path d="M42 526Q122 343 265 261T642 118"/><path d="M55 557Q169 365 295 291T668 164"/><path d="M76 589Q199 395 325 321T686 211"/></g>
<text x="35" y="45" class="heading">6 nights · Canberra and Thredbo</text>
<path d="M645 86Q530 125 397 240L332 334" fill="none" stroke="#31d5ec" stroke-width="5"/>
<path d="M332 334Q280 293 230 300Q212 340 240 365Q300 380 332 334" fill="none" stroke="#f4d35e" stroke-width="4" stroke-dasharray="6 7"/>
<path d="M332 334Q335 388 354 445L288 530Q202 582 137 566" fill="none" stroke="#95df8e" stroke-width="5"/>
<path d="M145 574Q225 591 301 539L366 450Q345 389 344 344Q366 300 390 280Q385 326 344 344" fill="none" stroke="#ffad62" stroke-width="4"/>
<path d="M137 566Q100 533 98 506Q81 539 137 566" fill="none" stroke="#bca5ff" stroke-width="4" stroke-dasharray="6 7"/>
<path d="M137 566Q210 565 280 523Q214 512 148 480" fill="none" stroke="#f18bb6" stroke-width="4" stroke-dasharray="6 7"/>
<path d="M351 333L414 251Q544 139 654 99" fill="none" stroke="#71b9ff" stroke-width="4"/>
{markers}

<text x="420" y="600" class="muted">Kosciuszko National Park</text>
<text x="355" y="365" class="muted">25–26 + 30 Dec · 3 nights total</text><text x="35" y="600" class="muted">Thredbo · 27–29 Dec · 3 nights</text>
<path d="M690 340v-44m-7 11 7-13 7 13" fill="none" stroke="#f2f5fb" stroke-width="2"/><text x="690" y="365" text-anchor="middle" class="muted">N</text>
<g class="muted"><circle cx="39" cy="625" r="7" fill="#09152b" stroke="#d6e3f2" stroke-width="2"/><text x="55" y="630" class="muted">Base / home</text><circle cx="213" cy="625" r="4" fill="#f4f6fc"/><text x="228" y="630" class="muted">Visit / break</text><path d="M366 625h25" stroke="#aebed3" stroke-width="3" stroke-dasharray="5 5"/><text x="402" y="630" class="muted">Day outing</text><text x="721" y="630" text-anchor="end" class="muted">Not to scale</text></g>
<path d="M35 650H725" stroke="#425067"/>
{timings}
<text x="38" y="956" class="muted">One colour per day · dates match the itinerary · dashed: local / return outing</text>
<text x="38" y="979" class="muted">Driving only · excludes stops · *30 Dec excludes local lookout access</text>
</svg>'''

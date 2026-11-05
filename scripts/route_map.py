from html import escape


def render_route_map():
    nodes = [
        (645, 86, 'Sydney', 621, 60, 'end', True),
        (500, 165, 'Southern Highlands', 525, 168, 'start', True),
        (397, 240, 'Goulburn', 417, 244, 'start', False),
        (332, 334, 'Canberra', 353, 339, 'start', True),
        (354, 445, 'Cooma', 376, 450, 'start', False),
        (288, 530, 'Jindabyne', 313, 540, 'start', True),
        (137, 566, 'Thredbo', 113, 593, 'middle', False),
        (148, 480, 'Charlotte Pass', 126, 459, 'middle', False),
        (101, 263, 'Tumut', 77, 250, 'end', True),
        (151, 370, 'Yarrangobilly', 130, 392, 'middle', False),
        (232, 421, 'Adaminaby', 209, 441, 'middle', False),
    ]
    markers = ''.join(f'<circle cx="{x}" cy="{y}" r="{9 if stay else 5}" fill="{"#09152b" if stay else "#f4f6fc"}" stroke="{"#48dcef" if stay else "#f4f6fc"}" stroke-width="3"/><text x="{tx}" y="{ty}" text-anchor="{anchor}" class="place">{escape(label)}</text>' for x, y, label, tx, ty, anchor, stay in nodes)
    rows = [
        ('#31d5ec', 'Sydney → Canberra · via Goulburn', '3½–4 hr'),
        ('#31d5ec', 'Canberra → Jindabyne · via Cooma', '2½ hr'),
        ('#ffad62', 'Jindabyne → Southern Highlands', '4½–5½ hr'),
        ('#ffad62', 'Highlands → Sydney · via the falls', '2–3 hr'),
        ('#9bdf94', 'Jindabyne → Tumut · optional', '3½–4½ hr'),
        ('#9bdf94', 'Tumut ↔ Yarrangobilly · return drive', '2½–3 hr'),
        ('#9bdf94', 'Tumut → Highlands · optional', '3½–4½ hr'),
    ]
    timings = ''.join(f'<path d="M38 {675+i*30}h25" stroke="{colour}" stroke-width="4" stroke-linecap="round"/><text x="79" y="{680+i*30}" class="timing">{escape(label)}</text><text x="721" y="{680+i*30}" text-anchor="end" class="timing">{time}</text>' for i, (colour, label, time) in enumerate(rows))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 950" role="img" aria-labelledby="title desc">
<title id="title">Sydney to Kosciuszko road-trip route map</title><desc id="desc">Main route: Sydney, Goulburn, Canberra, Cooma, Jindabyne, Southern Highlands and Sydney. Mountain outings to Charlotte Pass and Thredbo. Optional return via Adaminaby, Tumut and Yarrangobilly. Schematic, not to scale. Approximate driving times exclude stops.</desc>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#071027"/><stop offset="1" stop-color="#101e35"/></linearGradient><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="#31d5ec"/></marker></defs>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:#f2f5fb}}.place{{font-size:18px;font-weight:600;paint-order:stroke;stroke:#0b172c;stroke-width:5px;stroke-linejoin:round}}.timing{{font-size:17px}}.muted{{fill:#aebed3;font-size:15px}}.heading{{font-size:22px;font-weight:700}}</style>
<rect width="760" height="950" rx="24" fill="url(#bg)"/>
<path d="M36 563C35 385 122 313 151 188S326 112 434 68 660 87 689 236 531 384 458 505 288 634 36 563Z" fill="#152c40" opacity=".55"/>
<g fill="none" stroke="#385067" opacity=".23"><path d="M42 526Q122 343 265 261T642 118"/><path d="M55 557Q169 365 295 291T668 164"/><path d="M76 589Q199 395 325 321T686 211"/></g>
<text x="35" y="45" class="heading">The road to the high country</text>
<path d="M645 86Q590 91 500 155T397 240L332 334Q327 389 354 445L288 530" fill="none" stroke="#31d5ec" stroke-width="5" marker-end="url(#arrow)"/>
<path d="M296 535Q398 475 375 437T354 336 415 250 508 175 650 94" fill="none" stroke="#ffad62" stroke-width="4"/>
<path d="M288 530Q270 451 232 421T174 315 101 263Q151 205 262 210T397 240L500 165" fill="none" stroke="#9bdf94" stroke-width="4" stroke-dasharray="10 8"/>
<path d="M101 263Q96 322 151 370" fill="none" stroke="#9bdf94" stroke-width="3" stroke-dasharray="3 7"/>
<path d="M288 530Q214 512 148 480M288 530Q202 582 137 566" fill="none" stroke="#c3adff" stroke-width="3" stroke-dasharray="6 7"/>
{markers}
<text x="420" y="570" class="muted">Kosciuszko National Park</text>
<text x="525" y="190" class="muted">Fitzroy Falls</text>
<path d="M690 340v-44m-7 11 7-13 7 13" fill="none" stroke="#f2f5fb" stroke-width="2"/><text x="690" y="365" text-anchor="middle" class="muted">N</text>
<g class="muted"><circle cx="39" cy="625" r="7" fill="#09152b" stroke="#48dcef" stroke-width="2"/><text x="55" y="630" class="muted">Overnight base</text><circle cx="213" cy="625" r="4" fill="#f4f6fc"/><text x="228" y="630" class="muted">Visit / break</text><path d="M366 625h25" stroke="#c3adff" stroke-width="3" stroke-dasharray="5 5"/><text x="402" y="630" class="muted">Mountain outing</text><text x="721" y="630" text-anchor="end" class="muted">Not to scale</text></g>
<path d="M35 650H725" stroke="#425067"/>
{timings}
<text x="38" y="911" class="muted">Cyan: southbound · Apricot: main return · Green: optional extension</text>
<text x="38" y="934" class="muted">Approximate driving only · add sightseeing, traffic and baby breaks</text>
</svg>'''

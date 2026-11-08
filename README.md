# Canberra and Kosciuszko · five nights

Christmas road trip, 25–30 December 2026: six days and five nights, styled after the [New Zealand itinerary](https://vitorsei.github.io/nz-trip-itinerary-2026/).

- Canberra, 25–26 December: two nights; Christmas Day picnic break and pre-arranged arrival; Arboretum and lake on Boxing Day.
- 27 December: Mount Ainslie summit is a firm morning stop, then Cooma lunch and park break en route to Jindabyne.
- Jindabyne, 27–29 December: three nights in one base, with Thredbo/Kosciuszko lookout and Charlotte Pass on separate days.
- 30 December: drive home via Cooma, Canberra and Goulburn with substantial breaks.
- An optional sixth night in Canberra can split the long return; it is outside the five-night plan and budget.
- Three adults and an infant, travelling in a Mercedes EQB 250. Includes exact-date accommodation search prices checked 8 November 2026, shared-unit versus two-room comparisons, and EV charging options. Confirm bed layout, cot arrangements, final booking prices and live charger status.
- Route schematic, daily seasonal weather references, real photo galleries, source links and a browser-local checklist.

## Run and edit

No dependencies or framework are needed:

```sh
python3 -m http.server 8766 --bind 127.0.0.1
```

Open http://127.0.0.1:8766/.

`scripts/build.py` generates `index.html`, `assets/styles.css` and `assets/app.js`. `scripts/route_map.py` generates `assets/route-map.svg`. `scripts/destinations.json` retains destination research and photo references, including places no longer in the route.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build.py
python3 scripts/check.py
node --check assets/app.js
```

The generator preserves the reference theme before the `ACT itinerary additions` marker in the stylesheet. Photographs remain remotely hosted and credited; they need internet access and can depict other seasons.

## Publication

GitHub Pages publishes `main` from the repository root, with `.nojekyll` for the static site:
https://vitorsei.github.io/act-trip-itinerary-2026/

## Planning assumptions

Travelling with three adults and a one-year-old in a Mercedes EQB 250. Model year and preferred room layout remain unconfirmed. Accommodation figures are observed search prices, not reserved inventory or bookings. Charging locations need live app verification; no vehicle-specific battery simulation has been completed. Confirm private bathrooms, minimum stays, holiday hours and infant/carrier lift arrangements before booking. Weather notes are seasonal references, not forecasts. Driving times exclude traffic, sightseeing and baby breaks. Checklist ticks do not make reservations or sync between devices.

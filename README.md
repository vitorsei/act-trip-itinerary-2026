# Canberra and Kosciuszko · five nights

Christmas road trip, 24–29 December 2026: six days and five nights, styled after the [New Zealand itinerary](https://vitorsei.github.io/nz-trip-itinerary-2026/).

- Canberra, 24–25 December: two nights; Goulburn arrival break, city evening, Arboretum and lake.
- 26 December: Mount Ainslie summit is a firm morning stop, then Cooma lunch and park break en route to Jindabyne.
- Jindabyne, 26–28 December: three nights in one base, with Thredbo/Kosciuszko lookout and Charlotte Pass on separate days.
- 29 December: drive home via Cooma, Canberra and Goulburn with substantial breaks.
- An optional sixth night in Canberra can split the long return; it is outside the five-night plan and budget.
- Accommodation allowance: AUD $920–1,420, based on two adults and an infant, own car and private bathrooms. Prices and Christmas availability are unverified.
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

Travelling with a one-year-old; adult count and car ownership remain unconfirmed. Accommodation allowances are planning targets, not live quotes or bookings. Confirm private bathrooms, minimum stays, holiday hours and infant/carrier lift arrangements before booking. Weather notes are seasonal references, not forecasts. Driving times exclude traffic, sightseeing and baby breaks. Checklist ticks do not make reservations or sync between devices.

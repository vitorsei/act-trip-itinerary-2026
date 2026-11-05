# Canberra and Kosciuszko Christmas itinerary 2026

A photo-rich, responsive road-trip guide from Sydney, styled after [the New Zealand itinerary](https://vitorsei.github.io/nz-trip-itinerary-2026/).

- Main route: 24–31 December 2026, eight days and seven nights.
- Extended route: 24 December–2 January, ten days and nine nights, adding Tumut and Yarrangobilly.
- Includes Mount Ainslie, Questacon/Mini Q, Charlotte Pass, Rainbow Lake, Porcupine Rocks and Fitzroy Falls.
- Rainbow Lake and Porcupine Rocks are alternatives on the flexible mountain day; the guide explains the effort of combining them or adding another night.
- Route selection updates visible days, dates, overnight allocations and the shareable URL (`?route=extended`).
- Browser-local booking checklist, map/source links and print styling.

## View and edit

No dependencies or build framework are needed. Serve the repository with `python3 -m http.server 8000` and open `http://localhost:8000`.

`index.html`, `assets/styles.css` and `assets/app.js` are the published site. Destination photographs are remotely hosted, with source credits beside each gallery and in the footer. Photos need internet access and may show other seasons or older facilities.

The generator is `scripts/build.py`; destination research and photo references are in `scripts/destinations.json`. After changing the generator, run:

```sh
python3 scripts/build.py
python3 scripts/check.py
node --check assets/app.js
```

The reference theme lives in `assets/styles.css` before the `ACT itinerary additions` marker. The generator replaces only the additions after that marker.

## GitHub Pages

Publish from `main` and `/ (root)` under Settings → Pages → Deploy from a branch. `.nojekyll` keeps this a plain static site.

Expected address: https://vitorsei.github.io/act-trip-itinerary-2026/

Enabling Pages requires the appropriate repository permissions; contributor push access alone may not allow the settings change.

## Planning assumptions

Travelling with a one-year-old. Budget examples assume two adults and one infant using their own car; those adult/transport assumptions are not confirmed. Stays, tickets and prices are provisional, not booked. Confirm holiday hours, carrier/lift arrangements, cave suitability, access and alpine weather before travel. Checklist ticks are local to the browser and do not make reservations.

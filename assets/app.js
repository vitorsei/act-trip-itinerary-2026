
(()=>{
 const routeButtons=[...document.querySelectorAll('[data-route]')];
 function setRoute(route,changeUrl=true){
  const extended=route==='extended';
  document.querySelectorAll('[data-variant]').forEach(el=>el.hidden=el.dataset.variant!=='both'&&el.dataset.variant!==route);
  routeButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.route===route)));
  document.getElementById('trip-title').textContent=extended?'9 nights from Canberra to the high country':'7 nights from Canberra to the high country';
  document.getElementById('trip-dates').textContent=extended?'24 December 2026 – 2 January 2027 · Sydney return':'24–31 December 2026 · Sydney return';
  document.getElementById('route-description').textContent=extended?'Canberra · Jindabyne · Tumut and Yarrangobilly · Southern Highlands':'Canberra · Jindabyne and Kosciuszko · Southern Highlands';
  document.querySelector('[data-place="fitzroy"]').href=extended?'#ext-4':'#day-8';
  document.querySelector('.trip-index ol').style.gridTemplateRows='repeat('+(extended?5:4)+',auto)';
  document.getElementById('route-status').textContent=extended?'Extended route selected: 10 days, 9 nights. Tumut and Yarrangobilly replace the original return leg.':'Main route selected: 8 days, 7 nights. Add the extension to include Tumut and Yarrangobilly.';
  if(changeUrl){const url=new URL(location.href);if(extended)url.searchParams.set('route','extended');else url.searchParams.delete('route');history.replaceState(null,'',url)}
 }
 routeButtons.forEach(b=>b.addEventListener('click',()=>setRoute(b.dataset.route)));
 document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{const target=document.getElementById(a.hash.slice(1));if(target?.dataset.variant==='extended')setRoute('extended');else if(target?.dataset.variant==='base')setRoute('base')}));
 const initial=new URL(location.href).searchParams.get('route')==='extended'||location.hash.startsWith('#ext-')?'extended':'base';setRoute(initial,false);
 const boxes=[...document.querySelectorAll('[data-check]')],key='act-snowies-trip-2026-checklist-v1';
 function update(){document.getElementById('progress').textContent=boxes.filter(b=>b.checked).length+' of '+boxes.length+' items checked'}
 try{const saved=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(saved))boxes.forEach((b,i)=>b.checked=saved[i]===true)}catch{}
 boxes.forEach(b=>b.addEventListener('change',()=>{update();try{localStorage.setItem(key,JSON.stringify(boxes.map(b=>b.checked)))}catch{}}));update();
 document.getElementById('print-trip').addEventListener('click',()=>window.print());
 document.querySelectorAll('img').forEach(img=>img.addEventListener('error',()=>{img.classList.add('photo-unavailable');img.alt+=' — photo unavailable; use the source link';}));
})();


(()=>{
 const boxes=[...document.querySelectorAll('[data-check]')],key='act-snowies-trip-2026-five-nights-dec25-checklist-v1';
 function update(){document.getElementById('progress').textContent=boxes.filter(b=>b.checked).length+' of '+boxes.length+' items checked'}
 try{const saved=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(saved))boxes.forEach((b,i)=>b.checked=saved[i]===true)}catch{}
 boxes.forEach(b=>b.addEventListener('change',()=>{update();try{localStorage.setItem(key,JSON.stringify(boxes.map(b=>b.checked)))}catch{}}));update();
 document.getElementById('print-trip').addEventListener('click',()=>window.print());
 document.querySelectorAll('img').forEach(img=>img.addEventListener('error',()=>{img.classList.add('photo-unavailable');img.alt+=' — photo unavailable; use the source link';}));
})();

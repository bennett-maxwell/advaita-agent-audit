/* cc-fresh.js — honest freshness badges for FKI command centers.
 * Reads [data-asof] (ISO timestamp of the page/data's REAL last update) and renders
 * fresh / aging / stale. FAIL-CLOSED: a missing or unparseable timestamp renders
 * "age unknown" (grey) — it NEVER renders green or the word "LIVE". This is the
 * structural guarantee that no command-center page can label stale data as live.
 */
(function () {
  function injectStyles() {
    if (document.getElementById('cc-fresh-styles')) return;
    var s = document.createElement('style');
    s.id = 'cc-fresh-styles';
    s.textContent =
      '.cc-fresh-badge{font-weight:700;border-radius:6px;padding:1px 7px;font-size:.92em}' +
      '.cc-ok{color:#15803d;background:#dcfce7}' +
      '.cc-aging{color:#b45309;background:#fef3c7}' +
      '.cc-stale{color:#4b5563;background:#e5e7eb}';
    document.head.appendChild(s);
  }
  function ageDays(iso) {
    var t = Date.parse(iso);
    if (isNaN(t)) return null;
    return (Date.now() - t) / 86400000;
  }
  function fmt(d) { return d < 1 ? Math.max(0, Math.round(d * 24)) + 'h' : Math.round(d) + 'd'; }
  function render(el) {
    var badge = el.querySelector('.cc-fresh-badge');
    if (!badge) return;
    var d = ageDays(el.getAttribute('data-asof'));
    var txt, cls;
    if (d === null) { txt = 'age unknown'; cls = 'cc-stale'; }
    else if (d < 2) { txt = 'fresh (' + fmt(d) + ' old)'; cls = 'cc-ok'; }
    else if (d < 7) { txt = fmt(d) + ' old'; cls = 'cc-aging'; }
    else { txt = 'STALE — ' + fmt(d) + ' old'; cls = 'cc-stale'; }
    badge.textContent = txt;
    badge.className = 'cc-fresh-badge ' + cls;
  }
  function run() {
    injectStyles();
    var nodes = document.querySelectorAll('[data-asof]');
    for (var i = 0; i < nodes.length; i++) render(nodes[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
})();

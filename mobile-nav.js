/**
 * AGENTE STRATEGICO — Mobile Hamburger Menu v2
 * Funziona su .navbar (tutte le pagine) e .nav (risorse)
 * Aggiungere prima di </body> in ogni HTML:
 * <script src="/mobile-nav.js"></script>
 * (o ../mobile-nav.js per sottocartelle a 1 livello)
 * (o ../../mobile-nav.js per coach/nome/)
 */
(function () {
  'use strict';

  function initMobileNav() {

    // Assicura viewport meta
    if (!document.querySelector('meta[name="viewport"]')) {
      var meta = document.createElement('meta');
      meta.name = 'viewport';
      meta.content = 'width=device-width, initial-scale=1.0';
      document.head.insertBefore(meta, document.head.firstChild);
    }

    // Trova la navbar — supporta sia .navbar che .nav
    var nav = document.querySelector('.navbar, nav.nav');
    if (!nav) return;

    // Solo su mobile
    function isMobile() { return window.innerWidth <= 768; }

    // Raccoglie i link dalla navbar (esclude il logo)
    var navLinksEl = nav.querySelector('.nav-links, ul');
    var links = [];
    if (navLinksEl) {
      navLinksEl.querySelectorAll('a').forEach(function (a) {
        var text = a.textContent.trim();
        var href = a.getAttribute('href');
        if (text && href) {
          links.push({ text: text, href: href });
        }
      });
    }

    // Fallback: link hard-coded se la navbar non ha ul
    if (links.length === 0) {
      links = [
        { text: 'Community', href: '/community/' },
        { text: 'Eventi', href: '/eventi/' },
        { text: 'Risorse', href: '/risorse/' },
        { text: 'Chi Siamo', href: '/chi-siamo/' }
      ];
    }

    // Crea hamburger button
    var btn = document.createElement('button');
    btn.className = 'as-hamburger';
    btn.setAttribute('aria-label', 'Apri menu');
    btn.setAttribute('aria-expanded', 'false');
    btn.innerHTML = '<span></span><span></span><span></span>';
    nav.appendChild(btn);

    // Crea overlay
    var overlay = document.createElement('div');
    overlay.className = 'as-mobile-nav';
    overlay.setAttribute('aria-hidden', 'true');

    var html = '';
    links.forEach(function (l) {
      // Non duplicare il bottone candidatura se già presente
      if (!l.text.toLowerCase().includes('candidat')) {
        html += '<a href="' + l.href + '">' + l.text + '</a>';
      }
    });
    // CTA candidatura sempre in fondo
    html += '<a href="/candidatura/" class="as-mobile-cta">Candidati ora</a>';

    overlay.innerHTML = html;
    document.body.appendChild(overlay);

    // Toggle
    function openMenu() {
      overlay.classList.add('open');
      btn.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
      overlay.classList.remove('open');
      btn.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    btn.addEventListener('click', function () {
      overlay.classList.contains('open') ? closeMenu() : openMenu();
    });

    // Chiude su click link
    overlay.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });

    // Chiude su ESC
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });

    // Chiude su resize a desktop
    window.addEventListener('resize', function () {
      if (!isMobile()) closeMenu();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }
})();

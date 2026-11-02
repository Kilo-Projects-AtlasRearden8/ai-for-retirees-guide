// Free AI for Retirement - site interactivity
// Font size controls (large-print friendly), persisted in localStorage.

(function () {
  var root = document.documentElement;
  var sizeDisplay = document.getElementById('current-size');
  var btnSmaller = document.getElementById('btn-smaller');
  var btnLarger = document.getElementById('btn-larger');
  var btnReset = document.getElementById('btn-reset');

  var MIN = 16;
  var MAX = 30;
  var STEP = 2;

  var size = parseInt(localStorage.getItem('afr-font-size'), 10) || 19;
  if (size < MIN) size = MIN;
  if (size > MAX) size = MAX;

  function apply(sizePx) {
    root.style.setProperty('--base-font-size', sizePx + 'px');
    localStorage.setItem('afr-font-size', sizePx);
    if (sizeDisplay) sizeDisplay.textContent = sizePx + 'px';
  }

  if (btnSmaller) {
    btnSmaller.addEventListener('click', function () {
      size = Math.max(MIN, size - STEP);
      apply(size);
    });
  }
  if (btnLarger) {
    btnLarger.addEventListener('click', function () {
      size = Math.min(MAX, size + STEP);
      apply(size);
    });
  }
  if (btnReset) {
    btnReset.addEventListener('click', function () {
      size = 19;
      apply(size);
    });
  }

  apply(size);

  // Make print link open browser print dialog
  var printLink = document.getElementById('print-link');
  if (printLink) {
    printLink.addEventListener('click', function (e) {
      e.preventDefault();
      window.print();
    });
  }
})();

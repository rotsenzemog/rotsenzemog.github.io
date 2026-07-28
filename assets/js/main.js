document.addEventListener('DOMContentLoaded', function() {
  
  // --- Navegación Sticky ---
  const navBar = document.getElementById('sticky-nav');
  const headerTop = document.querySelector('.header-top');

  if (navBar) {
    window.addEventListener('scroll', function() {
      const triggerHeight = headerTop ? headerTop.offsetHeight : 50;

      if (window.scrollY > triggerHeight) {
        navBar.classList.add('is-sticky');
      } else {
        navBar.classList.remove('is-sticky');
      }
    });
  }

  // --- Carrusel de Citas / Fragmentos ---
  const slides = document.querySelectorAll('.quote-slide');
  const dots = document.querySelectorAll('.dot');
  const prevBtn = document.getElementById('prevQuote');
  const nextBtn = document.getElementById('nextQuote');

  if (slides.length > 0) {
    let currentSlide = 0;
    let autoSlideInterval;

    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.classList.remove('active');
        if (dots[i]) dots[i].classList.remove('active');
      });

      currentSlide = (index + slides.length) % slides.length;
      slides[currentSlide].classList.add('active');
      if (dots[currentSlide]) dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
      showSlide(currentSlide + 1);
    }

    function prevSlide() {
      showSlide(currentSlide - 1);
    }

    // Eventos en los botones
    if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetTimer(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetTimer(); });

    // Eventos en los puntos
    dots.forEach(dot => {
      dot.addEventListener('click', function() {
        const slideIndex = parseInt(this.getAttribute('data-slide'));
        showSlide(slideIndex);
        resetTimer();
      });
    });

    // Auto rotación cada 6 segundos
    function startTimer() {
      autoSlideInterval = setInterval(nextSlide, 6000);
    }

    function resetTimer() {
      clearInterval(autoSlideInterval);
      startTimer();
    }

    startTimer();
  }

});

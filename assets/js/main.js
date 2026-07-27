<script>
  document.addEventListener('DOMContentLoaded', function() {
    const navBar = document.getElementById('sticky-nav');
    const headerTop = document.querySelector('.header-top');

    window.addEventListener('scroll', function() {
      // Punto donde la franja superior desaparece de la pantalla
      const triggerHeight = headerTop ? headerTop.offsetHeight : 60;

      if (window.scrollY > triggerHeight) {
        navBar.classList.add('is-sticky');
      } else {
        navBar.classList.remove('is-sticky');
      }
    });
  });
</script>

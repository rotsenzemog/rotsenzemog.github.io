<script>
  document.addEventListener('DOMContentLoaded', function() {
    const navBar = document.getElementById('sticky-nav');
    const headerTop = document.querySelector('.header-top');

    window.addEventListener('scroll', function() {
      const triggerHeight = headerTop ? headerTop.offsetHeight : 50;

      if (window.scrollY > triggerHeight) {
        navBar.classList.add('is-sticky');
      } else {
        navBar.classList.remove('is-sticky');
      }
    });
  });
</script>

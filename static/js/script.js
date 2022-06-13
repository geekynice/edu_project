$(function () {
  $(document).scroll(function () {
      var $nav = $(".navbar-fixed-top");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});
AOS.init({
        offset: 120, 
        delay: 100, // values from 0 to 3000, with step 50ms
        duration: 400, // values from 0 to 3000, with step 50ms
        easing: 'ease', // default easing for AOS animations
        once: false,
     });

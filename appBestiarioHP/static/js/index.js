document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");
  const dots = document.querySelectorAll(".dot");
  let index = 0;

  function showSlide(i) {
    slides.forEach((s, n) => {
      s.classList.toggle("active", n === i);
      dots[n].classList.toggle("active", n === i);
    });
    index = i;
  }

  document.querySelector(".next").addEventListener("click", () => {
    showSlide((index + 1) % slides.length);
  });

  document.querySelector(".prev").addEventListener("click", () => {
    showSlide((index - 1 + slides.length) % slides.length);
  });

  dots.forEach((dot, i) => {
    dot.addEventListener("click", () => showSlide(i));
  });
});

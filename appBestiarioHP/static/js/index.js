document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");
  const dots = document.querySelectorAll(".dot");
  const carouselContainer = document.querySelector(".carousel-container");
  let index = 0;

  function showSlide(i) {
    slides.forEach((s, n) => {
      s.classList.toggle("active", n === i);
      dots[n].classList.toggle("active", n === i);
    });
    
    // Actualizar la imagen de fondo del contenedor
    carouselContainer.className = 'carousel-container';
    carouselContainer.classList.add(`slide${i + 1}-active`);
    
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

  // Inicializar con la primera imagen de fondo
  showSlide(0);

  // Carrusel de razas
  const razasContainer = document.querySelector(".razas-container");
  const razaPrev = document.querySelector(".raza-prev");
  const razaNext = document.querySelector(".raza-next");

  if (razasContainer && razaPrev && razaNext) {
    const razaCards = Array.from(document.querySelectorAll(".raza-card"));
    
    if (razaCards.length > 0) {
      let currentIndex = 0;

      function updateCarousel() {
        razaCards.forEach((card, index) => {
          // Limpiar estilos inline
          card.style.opacity = '';
          card.style.transform = '';
          
          // Remover todas las clases de posición
          card.classList.remove('center', 'left', 'right');
          
          // Calcular la posición relativa al índice actual
          const diff = (index - currentIndex + razaCards.length) % razaCards.length;
          
          if (diff === 0) {
            // Tarjeta central
            card.classList.add('center');
          } else if (diff === razaCards.length - 1) {
            // Tarjeta a la izquierda
            card.classList.add('left');
          } else if (diff === 1) {
            // Tarjeta a la derecha
            card.classList.add('right');
          }
          // Las demás tarjetas no tendrán clase y usarán el estilo por defecto (opacity: 0)
        });
      }

      razaNext.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % razaCards.length;
        updateCarousel();
      });

      razaPrev.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + razaCards.length) % razaCards.length;
        updateCarousel();
      });

      // Inicializar
      updateCarousel();
    }
  }
});

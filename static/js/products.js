document.addEventListener("scroll", function () {
    const cards = document.querySelector(".our-products-cards");
    const rect = cards.getBoundingClientRect();
  
    if (rect.top <= window.innerHeight - 100) {
      cards.classList.add("visible");
    }
  });
  
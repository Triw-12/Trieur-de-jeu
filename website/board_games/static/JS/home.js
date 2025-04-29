document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".scroll-container").forEach(carousel => {
        let scrollAmount = 0;
        let maxScroll = carousel.scrollWidth - carousel.clientWidth;

        function autoScroll() {
            if (carousel.scrollLeft >= maxScroll) {
                carousel.scrollLeft = 0; // Reviens au début
            } else {
                carousel.scrollBy({ left: carousel.clientWidth / 3, behavior: "smooth" }); // Fait défiler d'un tiers de la largeur
            }
        }

        let interval = setInterval(autoScroll, 10000); // Défile toutes les 10 secondes

        // Arrêter au survol et reprendre après
        carousel.addEventListener("mouseenter", () => clearInterval(interval));
        carousel.addEventListener("mouseleave", () => interval = setInterval(autoScroll, 10000));
    });
});

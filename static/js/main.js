(function () {
    "use strict";

    const body = document.body;
    const navbar = document.querySelector(".site-navbar");
    const themeToggle = document.getElementById("themeToggle");
    const savedTheme = localStorage.getItem("portfolio-theme");

    if (savedTheme === "light" || savedTheme === "dark") {
        body.dataset.theme = savedTheme;
    }

    window.addEventListener("load", () => {
        body.classList.add("loaded");
    });

    const syncNavbar = () => {
        if (navbar) {
            navbar.classList.toggle("nav-scrolled", window.scrollY > 8);
        }
    };

    syncNavbar();
    window.addEventListener("scroll", syncNavbar, { passive: true });

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            const nextTheme = body.dataset.theme === "dark" ? "light" : "dark";
            body.dataset.theme = nextTheme;
            localStorage.setItem("portfolio-theme", nextTheme);
        });
    }

    const revealItems = document.querySelectorAll(".reveal");
    const progressBars = document.querySelectorAll("[data-progress]");

    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12 }
    );

    revealItems.forEach((item) => revealObserver.observe(item));

    const progressObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const value = entry.target.dataset.progress || "0";
                    entry.target.style.width = `${value}%`;
                    progressObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.4 }
    );

    progressBars.forEach((bar) => progressObserver.observe(bar));

    const typingTarget = document.querySelector("[data-typing]");
    if (typingTarget && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        const phrases = typingTarget.dataset.typing.split(",").map((phrase) => phrase.trim()).filter(Boolean);
        let phraseIndex = 0;
        let charIndex = 0;
        let deleting = false;

        const type = () => {
            const phrase = phrases[phraseIndex] || "";
            typingTarget.textContent = phrase.slice(0, charIndex);

            if (!deleting && charIndex < phrase.length) {
                charIndex += 1;
                window.setTimeout(type, 70);
                return;
            }

            if (!deleting && charIndex === phrase.length) {
                deleting = true;
                window.setTimeout(type, 1200);
                return;
            }

            if (deleting && charIndex > 0) {
                charIndex -= 1;
                window.setTimeout(type, 36);
                return;
            }

            deleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            window.setTimeout(type, 180);
        };

        type();
    }
})();

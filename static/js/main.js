/* ============================================================
   Muhammad Haseeb - Portfolio JavaScript
   ============================================================ */

document.addEventListener("DOMContentLoaded", () => {
  console.log("Portfolio loaded ✅");

  // ============ TYPEWRITER EFFECT ============
  const typedElement = document.getElementById("typed-text");
  if (typedElement) {
    const roles = [
      "Network Engineer",
      "IT Specialist",
      "Developer",
      "Instructor"
    ];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function typeRole() {
      const currentRole = roles[roleIndex];
      if (isDeleting) {
        typedElement.textContent = currentRole.substring(0, charIndex - 1);
        charIndex--;
      } else {
        typedElement.textContent = currentRole.substring(0, charIndex + 1);
        charIndex++;
      }

      let typeSpeed = isDeleting ? 50 : 100;

      if (!isDeleting && charIndex === currentRole.length) {
        typeSpeed = 2000;
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        typeSpeed = 500;
      }

      setTimeout(typeRole, typeSpeed);
    }
    typeRole();
  }

  // ============ SKILL BAR ANIMATION ============
  const skillBars = document.querySelectorAll(".skill-progress");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const level = entry.target.getAttribute("data-level");
        entry.target.style.width = level + "%";
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  skillBars.forEach((bar) => observer.observe(bar));

  // ============ FADE IN ON SCROLL ============
  const fadeElements = document.querySelectorAll(".project-card, .fact-card, .skill-category, .contact-card, .experience-card");
  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in");
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  fadeElements.forEach((el) => fadeObserver.observe(el));

  // ============ NAVBAR SHADOW ON SCROLL ============
  const navbar = document.querySelector(".portfolio-navbar");
  if (navbar) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 20) {
        navbar.style.boxShadow = "0 10px 30px rgba(0, 0, 0, 0.3)";
      } else {
        navbar.style.boxShadow = "none";
      }
    });
  }

  // ============ SMOOTH SCROLL ============
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (href.length > 1) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      }
    });
  });
});
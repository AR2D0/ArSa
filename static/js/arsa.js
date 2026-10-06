/**
 * ArSa – Client-side utilities
 * Floating hearts, confetti helpers, map helpers
 */

(function () {
    'use strict';

    // ----- Floating hearts background -----
    function createHearts() {
        const container = document.getElementById('hearts-bg');
        if (!container) return;

        const hearts = ['❤️', '💕', '💗', '💖', '💘', '🩷'];
        const count = 18;

        for (let i = 0; i < count; i++) {
            const heart = document.createElement('span');
            heart.className = 'heart';
            heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.left = Math.random() * 100 + '%';
            heart.style.animationDuration = (8 + Math.random() * 10) + 's';
            heart.style.animationDelay = Math.random() * 12 + 's';
            heart.style.fontSize = (0.8 + Math.random() * 1.2) + 'rem';
            container.appendChild(heart);
        }
    }

    // ----- Confetti celebration -----
    window.arsaCelebrate = function () {
        if (typeof confetti !== 'function') return;

        const duration = 5 * 1000;
        const end = Date.now() + duration;
        const colors = ['#8E1EA2', '#C654C3', '#ED96D7', '#FFC0DE', '#ffffff'];

        (function frame() {
            confetti({
                particleCount: 4,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: colors
            });
            confetti({
                particleCount: 4,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: colors
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        })();

        // Big burst
        setTimeout(() => {
            confetti({
                particleCount: 120,
                spread: 100,
                origin: { y: 0.6 },
                colors: colors
            });
        }, 300);
    };

    // ----- Fireworks-like bursts -----
    window.arsaFireworks = function () {
        if (typeof confetti !== 'function') return;
        const colors = ['#8E1EA2', '#C654C3', '#ED96D7', '#FFC0DE'];

        function fire(x) {
            confetti({
                particleCount: 40,
                startVelocity: 35,
                spread: 360,
                ticks: 60,
                origin: { x: x, y: Math.random() * 0.4 + 0.1 },
                colors: colors,
                shapes: ['circle', 'square'],
                scalar: 1.1
            });
        }

        fire(0.2);
        setTimeout(() => fire(0.5), 200);
        setTimeout(() => fire(0.8), 400);
        setTimeout(() => fire(0.35), 600);
        setTimeout(() => fire(0.65), 800);
    };

    // Init on DOM ready
    document.addEventListener('DOMContentLoaded', function () {
        createHearts();
    });
})();

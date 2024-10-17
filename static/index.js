
if (window.location.pathname === '/') {
    window.addEventListener('scroll', function() {
        const header = document.querySelector('.header');
        if (window.scrollY > 100) {
            header.classList.add('bg-gray-900');
            header.classList.add('border-b-2');
            header.classList.add('border-main');
        } else {
            header.classList.remove('bg-gray-900');
            header.classList.remove('border-b-2');
            header.classList.remove('border-main');
        }
    });
}

class MobileMenu {
    constructor() {
        this.mobileMenu = document.getElementById('mobile-menu');
        this.openMenuBtn = document.getElementById('mobile-menu-btn');
        this.closeMenuBtn = document.getElementById('close-menu-btn');
        this.events();
    }

    events() {
        this.openMenuBtn.addEventListener('click', () => this.toggleMenu());
        this.closeMenuBtn.addEventListener('click', () => this.toggleMenu());
        this.mobileMenu.addEventListener('click', (e) => {
            if (e.target.tagName === 'A') {
                this.toggleMenu();
            }
        });
    }

    toggleMenu() {
        if (this.mobileMenu.classList.contains('hidden')) {
            this.mobileMenu.classList.remove('hidden');
            this.mobileMenu.classList.add('open');
        } else {
            this.mobileMenu.classList.remove('open');
            this.mobileMenu.classList.add('hidden');
        }
    }
}

document.addEventListener('DOMContentLoaded', function(){
    mobileMenu = new MobileMenu();
})
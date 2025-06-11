// script.js
document.addEventListener('DOMContentLoaded', () => {
    // Cursor elements
    const cursorMain = document.querySelector('.cursor-main');
    const cursorFollower = document.querySelector('.cursor-follower');
    const particlesContainer = document.querySelector('.particles-container');
    
    // Sound elements
    const clickSound = document.getElementById('clickSound');
    const hoverSound = document.getElementById('hoverSound');
    
    // Input state tracking
    const Input = {
        mouse: {
            x: 0,
            y: 0,
            left: false,
            middle: false,
            right: false,
            prevX: 0,
            prevY: 0,
            velocityX: 0,
            velocityY: 0
        },
        keys: {}
    };
    
    // Track mouse position
    document.addEventListener('mousemove', (e) => {
        Input.mouse.prevX = Input.mouse.x;
        Input.mouse.prevY = Input.mouse.y;
        Input.mouse.x = e.clientX;
        Input.mouse.y = e.clientY;
        
        // Calculate velocity
        Input.mouse.velocityX = Input.mouse.x - Input.mouse.prevX;
        Input.mouse.velocityY = Input.mouse.y - Input.mouse.prevY;
        
        // Update cursor positions
        cursorMain.style.left = `${Input.mouse.x}px`;
        cursorMain.style.top = `${Input.mouse.y}px`;
        
        // Follower cursor has a slight delay
        setTimeout(() => {
            cursorFollower.style.left = `${Input.mouse.x}px`;
            cursorFollower.style.top = `${Input.mouse.y}px`;
        }, 50);
        
        // Create subtle trail particles when moving fast
        if (Math.abs(Input.mouse.velocityX) + Math.abs(Input.mouse.velocityY) > 10) {
            createParticle(Input.mouse.x, Input.mouse.y);
        }
    });
    
    // Mouse down events
    document.addEventListener('mousedown', (e) => {
        if (e.button === 0) {
            Input.mouse.left = true;
            cursorMain.classList.add('click');
            cursorFollower.classList.add('click');
            clickSound.currentTime = 0;
            clickSound.play();
            
            // Create click effect particles
            for (let i = 0; i < 5; i++) {
                createParticle(Input.mouse.x, Input.mouse.y, true);
            }
        }
        if (e.button === 1) Input.mouse.middle = true;
        if (e.button === 2) Input.mouse.right = true;
    });
    
    // Mouse up events
    document.addEventListener('mouseup', (e) => {
        if (e.button === 0) {
            Input.mouse.left = false;
            cursorMain.classList.remove('click');
            cursorFollower.classList.remove('click');
        }
        if (e.button === 1) Input.mouse.middle = false;
        if (e.button === 2) Input.mouse.right = false;
    });
    
    // Hover effects for interactive elements
    const interactiveElements = document.querySelectorAll('.interactive-btn, .interactive-link, a, button');
    
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursorMain.classList.add('active');
            cursorFollower.classList.add('active');
            hoverSound.currentTime = 0;
            hoverSound.play();
            
            // Create hover effect particles
            const rect = el.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            
            for (let i = 0; i < 8; i++) {
                setTimeout(() => {
                    createParticle(
                        centerX + (Math.random() - 0.5) * rect.width,
                        centerY + (Math.random() - 0.5) * rect.height,
                        false,
                        true
                    );
                }, i * 100);
            }
        });
        
        el.addEventListener('mouseleave', () => {
            cursorMain.classList.remove('active');
            cursorFollower.classList.remove('active');
        });
    });
    
    // Particle creation function
    function createParticle(x, y, isClick = false, isHover = false) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        particlesContainer.appendChild(particle);
        
        // Set initial position
        particle.style.left = `${x}px`;
        particle.style.top = `${y}px`;
        
        // Different styles based on interaction type
        if (isClick) {
            particle.style.backgroundColor = '#bc6c25';
            particle.style.width = '6px';
            particle.style.height = '6px';
        } else if (isHover) {
            particle.style.backgroundColor = '#588157';
            particle.style.width = '10px';
            particle.style.height = '10px';
        }
        
        // Randomize animation
        const size = Math.random() * 5 + 3;
        const duration = Math.random() * 2 + 1;
        
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        
        // Animate particle
        const animation = particle.animate([
            { 
                transform: 'translate(0, 0) scale(1)',
                opacity: 1 
            },
            { 
                transform: `translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px) scale(0)`,
                opacity: 0 
            }
        ], {
            duration: duration * 1000,
            easing: 'cubic-bezier(0.4, 0, 0.2, 1)'
        });
        
        animation.onfinish = () => {
            particle.remove();
        };
    }
    
    // Handle keyboard events
    document.addEventListener('keydown', (e) => {
        Input.keys[e.key] = true;
    });
    
    document.addEventListener('keyup', (e) => {
        Input.keys[e.key] = false;
    });
    
    // Prevent context menu on right click
    document.addEventListener('contextmenu', (e) => {
        e.preventDefault();
    });
    
    // Initialize cursor position
    cursorMain.style.left = `${window.innerWidth / 2}px`;
    cursorMain.style.top = `${window.innerHeight / 2}px`;
    cursorFollower.style.left = `${window.innerWidth / 2}px`;
    cursorFollower.style.top = `${window.innerHeight / 2}px`;
});
// Add this to the script.js for tongue-flick effect
setInterval(() => {
    if (Math.random() > 0.98) {
        const tongue = document.createElement('div');
        tongue.classList.add('tongue');
        document.body.appendChild(tongue);
        
        tongue.style.left = `${Input.mouse.x}px`;
        tongue.style.top = `${Input.mouse.y}px`;
        
        setTimeout(() => {
            tongue.remove();
        }, 500);
    }
}, 1000);
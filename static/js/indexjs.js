/*!
* Start Bootstrap - Grayscale v7.0.6 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});
function printSet() {
    const cookies = document.cookie.split(';');
    let myCookieValue = null;
    let myCookieValue2 = null;
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('user=')|| cookie.startsWith('session=')) {
            myCookieValue = cookie.substring('user='.length, cookie.length);
            myCookieValue2 = cookie.substring('session='.length, cookie.length);
            break;
        }
    }
  
    // Print the Set to the DOM
    const container = document.getElementById('myCookSetContainer');
    container.innerHTML = '';
    const item = document.createElement('div');
    item.textContent = "user_cookie:"+myCookieValue+'\n\n'+"session_cookie:"+myCookieValue2;
    alert(item.textContent);
    //container.appendChild(item);
  }

  function printSet2() {
    
    const cookies = document.cookie.split(';');
    let myCookieValue = null;
    let myCookieValue2 = null;
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('user=')|| cookie.startsWith('session=')) {
            myCookieValue = cookie.substring('user='.length, cookie.length);
            myCookieValue2 = cookie.substring('session='.length, cookie.length);
            break;
        }
    }

    // Print the Set to the DOM
    const item = document.createElement('div');
    item.textContent = "user_cookie:"+myCookieValue+'\n\n'+"session_cookie:"+myCookieValue2;

    alert(item.textContent);
  }
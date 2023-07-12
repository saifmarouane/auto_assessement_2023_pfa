function printSet() {
    const cookies = document.cookie.split(';');
    let myCookieValue = null;
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('user=')) {
            myCookieValue = cookie.substring('user='.length, cookie.length);
            break;
        }
    }
  
    // Print the Set to the DOM
    const container = document.getElementById('myCookSetContainer');
    container.innerHTML = '';
    const item = document.createElement('div');
    item.textContent = myCookieValue;
    container.appendChild(item);
  }
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
   
    alert("hi");
    //container.appendChild(item);
  }
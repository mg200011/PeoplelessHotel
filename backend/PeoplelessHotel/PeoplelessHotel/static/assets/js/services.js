'use strict';

class Services {


    async gget(url) {
        
        try { 
            showSpinner();

            let response = await fetch(url);
            
            if(response.ok) {
                hideSpinner();
                return await response.json();
            }

        } catch(ex) {
            console.log(ex);
        }
        hideSpinner();

        return new Error("failed to run query");
    }

    async gdelete(url) {
        try { 
            showSpinner();

            let response = await fetch(url, { method: "DELETE" } );
            
            if(response.ok) {
                hideSpinner();
                return await response.json();
            }

        } catch(ex) {
            console.log(ex);
        }
        hideSpinner();

        return new Error("failed to run delete");
    }

    async gpost(url, data = {}) {
        try { 
            showSpinner();

            const response = await fetch(url, {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json; charset=UTF-8'
                },
                redirect: 'follow', // manual, *follow, error
                referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(data) // body data type must match "Content-Type" header
            });
      
            
            if(response.ok) {
                hideSpinner();
                return await response.json();
            }

        } catch(ex) {
            console.log(ex);
        }
        hideSpinner();

        return new Error("failed to run post");
    }


    async gput(url, data = {}) {
        try { 
            showSpinner();

            const response = await fetch(url, {
                method: 'PUT', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
                cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json; charset=UTF-8'
                },
                redirect: 'follow', // manual, *follow, error
                referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(data) // body data type must match "Content-Type" header
            });
      
            
            if(response.ok) {
                hideSpinner();
                return await response.json();
            }

        } catch(ex) {
            console.log(ex);
        }
        hideSpinner();

        return new Error("failed to run put");
    }

}

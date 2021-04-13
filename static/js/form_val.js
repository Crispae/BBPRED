
var e = document.getElementById("post-form").addEventListener("submit", form_submit);
function form_submit(e) 

{
    e.preventDefault();
    console.log("default prevent")
    var smiles = document.getElementById("smiles").value;
    var algo = document.getElementById("algo").value;
    console.log("data-collected");
    data = JSON.stringify({ smiles: smiles, algo: algo });
    console.log("data-jsonfied");
    console.log(data);
    
    //xhr
    var xhr = new XMLHttpRequest();
    console.log("xmlhttp formed")

    // open
    xhr.open("POST", `${window.origin}/predict`, true);
    xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded")

    console.log("object formed")

    = function () {
        console.log(this.readyState);

        if (this.status == 200 && this.readyState == 4) {
            var res = JSON.parse(this.responseText);

            if (res["result"] == 1) 
            {
                document.getElementById("response").innerHTML = `
                <div id="errorAlert" class="alert alert-danger" role="alert">
                <h4 class="alert-heading">Well done!</h4>
                <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
                <hr>
                <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
              </div>`
            }

            else 
            {

                document.getElementById("response").innerHTML = `

                <div  id="successAlert" class="alert alert-success" role="alert">
                <h4 class="alert-heading">Well done!</h4>
                <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
                <hr>
                <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
              </div>
                
                
                `
            }

        }

    

    xhr.onerror = function() 
    {

        document.getElementById("response").innerHTML = `

            <div  id="successAlert" class="alert alert-success" role="alert">
                <h4 class="alert-heading">Well done!</h4>
                <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
                <hr>
                <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
              </div>
                
              `;

    }

 xhr.send(data);

}

console.log("loaded");


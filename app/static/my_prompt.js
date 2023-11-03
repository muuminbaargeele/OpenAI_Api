
// if the Code works do not touch
var respond_container = document.getElementById('respond-container')

// ===================My code starts here======================
function save_topic(){

    
    var s_b_2 = document.getElementById('s_b_2')
    s_b_2.style.display = 'block'
    var s_b_1 = document.getElementById('s_b_1')
    s_b_1.style.display = 'none'


 
    // s_b_2.style.opacity = '1'

    var my_topic = document.getElementById('my_topic')
    
    var data = {
        'topic': my_topic.value
    }
    console.log(data)
    // now call python funct to prounce

        fetch(`/respond`,
        {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })

        })// Then do something other withe respond...
        .then(function (response) {
            if (response.status != 200) {
                console.log(`Response status were not 200: ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                console.log(data)
                respond_container.innerHTML = data['message']
                // s_b_2.style.opacity = '0'
                // s_b_1.style.display = 'block'
                s_b_2.style.display = 'none'
                s_b_1.style.display = 'block'


            })
        })// End of then
    
}

// Wainting spineers
function please_wait(hidde_btn, show_btn) {

    console.log('Please wait...')
    var hidde_btn = document.getElementById(hidde_btn)
    var show_btn = document.getElementById(show_btn)

    hidde_btn.style.display = 'none'
    show_btn.style.display = 'inline-block'

}

function please_wait2(hidde_btn, show_btn) {

    console.log('Please wait...')
    var hidde_btn = document.getElementById(hidde_btn)
    var show_btn = document.getElementById(show_btn)

    hidde_btn.style.display = 'none'
    show_btn.style.display = 'inline-block'

}


// ===================My code starts here======================
function speak(topic, b1, b2, b3){

    console.log('Please wait...')
    var hidde_btn = document.getElementById(b1)
    var show_btn = document.getElementById(b2)
    var show_btn1 = document.getElementById(b3)

    hidde_btn.style.display = 'none'
    show_btn.style.display = 'inline-block'
    show_btn1.style.display = 'inline-block'
    var my_topic = document.getElementById(topic)


    var data = {
        'topic': my_topic.innerText
    }
    console.log(data)
    // now call python funct to prounce

        fetch(`/speak`,
        {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })

        })// Then do something other withe respond...
        .then(function (response) {
            if (response.status != 200) {
                console.log(`Response status were not 200: ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                console.log(data)
                // respond_container.innerHTML = data['message']
                hidde_btn.style.display = 'inline-block'
                show_btn.style.display = 'none'
                show_btn1.style.display = 'none'


            })
        })// End of then
    
}


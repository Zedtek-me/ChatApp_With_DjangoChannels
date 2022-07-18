// getting the room name from the url 
var roomUrl= window.location.pathname

// dynamically creating an endpoint
const host= window.location.host

// to get the appropriate scheme of the protocol--> secure or not
let endPoint;
if (window.location.href.split(':')[0]==='https'){
    endPoint= `wss://${String(host)}/chat/`
}
else{
    endPoint= `ws://${String(host)}/chat/`
}

// instatiation and events emition
const socket= new WebSocket(endPoint)

// get the connected user and display at the frontend 
let allUsersCont= document.querySelectorAll('.list')//container that lists the users connected.
socket.onopen= function(e){
    let data= JSON.parse(e.data)
    var currentUser= data.current_user
    // get the container for all connected users and add the current user to the connected users, below.
    allUsersCont.textContent += `${currentUser}, `
}
// remove users from users list when disconnected.
socket.onclose= function(e){
    allUsersCont.textContent.replace(`${currentUser},`, '')
}
// inserting the data from the server into the chatbox
socket.onmessage= function(event){
    let data= JSON.parse(event.data)
    // checking if a message is contained in the sent data
    if (data.message){
        var chatContainer= document.querySelector(".chat-cont")
        var paragAndImg= document.createElement('DIV')
        paragAndImg.setAttribute('class', 'img-msg')
        var img= document.createElement('IMG')
        img.setAttribute('src', '')
        img.setAttribute('id', 'chat-pic')
        img.src=  data.image
        var paragraph= document.createElement("P")
        paragraph.setAttribute('id', 'response')
        paragraph.setAttribute('onopen', '')
        paragraph.innerHTML="<b class='u-name'>" + data.user + "</b>" + ': ' + data.message
        paragAndImg.appendChild(img)
        paragAndImg.appendChild(paragraph)

        // checking whether the message has been seen or not.
        if(paragraph.textContent && !paragraph.onopen){
            msg=document.createElement('P')
            msg.textContent= "Some messages unread."
            chatContainer.appendChild(msg)
            chatContainer.appendChild(paragAndImg)

            setTimeout(()=> chatContainer.removeChild(msg), 2*1000)
        }else {
            setTimeout(()=> chatContainer.removeChild(msg), 2*1000)
        }
    }
}

// send text data to the server
function sendText(){
    let text= document.getElementsByClassName("msg-box")[0]
    if (text.value && text.value != '0'){
        socket.send(JSON.stringify({message: text.value}))
        text.value=""
    }
}
// keyboard enter key
function keyEvent(event){
    if (event.keyCode === 13){
    let text= document.getElementsByClassName("msg-box")[0]
    socket.send(text.value)
    text.value=""
    }
}

// Initial check typing code

// const checkTyping= (eve)=>{
//     let topBar= document.querySelector('.connected-ones')
//     let typeBox= document.createElement('H6')
//     typeBox.setAttribute('id', 'typing')
//     typeBox.innerHTML= 'someone is typing...'
//     topBar.appendChild(typeBox)
//     typeBox.setAttribute('id', 'typing')
//     setTimeout(()=>{
//         topBar.removeChild(typeBox)}, 1000
//     )
//     }

// checking if someone is typing something
function checkTyping(event){
    let typing= document.querySelector('.typing')
    let parent= document.querySelector('.connected-ones')
    if(typing.style.display === 'flex'){
        typing.style.display='none';
    }else {
        typing.style.display='flex'
    }
}
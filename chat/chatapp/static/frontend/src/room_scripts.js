// getting the room name from the url 
var roomUrl= window.location.pathname
console.log(roomUrl)

// dynamically creating an endpoint
const host= window.location.host
const endPoint= `ws://${String(host)}/chat/`

// instatiation and events emition
const socket= new WebSocket(endPoint)

// inserting the data from the server into the chatbox
socket.onmessage= function(event){
    console.log(event)
    var chatContainer= document.querySelector(".chat-cont")
    var paragraph= document.createElement("P")
    paragraph.setAttribute('id', 'response')
    paragraph.setAttribute('onopen', '')
    paragraph.textContent=event.data

    // checking whether the message has been seen or not.
    if(paragraph.textContent && !paragraph.onopen){
        msg=document.createElement('P')
        msg.textContent= "Some messages unread."
        chatContainer.appendChild(msg)
        chatContainer.appendChild(paragraph)
        setTimeout(()=> chatContainer.removeChild(msg), 2*1000)
    }else {
        setTimeout(()=> chatContainer.removeChild(msg), 2*1000)
    }
    console.log(chatContainer)
}

// send text data to the server
function sendText(){
    let text= document.getElementsByClassName("msg-box")[0]
    socket.send(text.value)
    text.value=""
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
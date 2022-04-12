
// for mobile display
function toggle(){
    const linksCont= document.querySelector(".m-nav").classList.toggle('mobile-nav')
    
}
    

// scripts for posting user contents on their timelines and on trends

// const postUpdates = ()=>{
//     let postContaineritems= document.querySelector('.post-widget')
//     let image= document.querySelector('.upload')
//     let viewImg= document.querySelector('.posted-img')
//     let viewTxtCont= document.querySelector('.writeup')
//     if (postContaineritems){
//         if(image){
//             viewImg.src= URL.createObjectURL(image)
//             viewTxtCont.textContent= postContaineritems.value
//             postContaineritems.value= ''
//         }
//         else{
//             viewTxtCont.textContent= postContaineritems.value
//             postContaineritems.value= ''
//         }
//     }
// }

//
 // creates a dialogue box for file upload.
 function getFile(){
    let upload= document.getElementsByClassName("upload")[0].click()
}
// function to click the submit button when the post button is clicked, as arranged on the profile page
function postSubmit(){
    let submit=document.querySelector('.hidden-btn').click()
}
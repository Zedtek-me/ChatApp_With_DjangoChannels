
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

// the toggles for editing each post.
const toggleEdit= ()=>{
    let toggleArrows= document.querySelectorAll('.prod-tog')
    let editDivs= document.querySelectorAll('.edits')
    for(let count= 0; count < toggleArrows.length; count++){
        toggleArrows[count].addEventListener('click', (e)=>{
            editDivs[count].classList.toggle('edit-options');
            toggleArrows[count].classList.toggle('fa-angle-up')
            toggleArrows[count].classList.toggle('fa-angle-down')
        })
    }
}
toggleEdit()

// form submission event for product removal
let removeBtns= document.querySelectorAll('.remove-post')
let formBtns= document.querySelectorAll('#removePost')
for(let i= 0; i < removeBtns.length; i++){
    removeBtns[i].addEventListener('click', (e)=>{
       formBtns[i].click()
    })
}

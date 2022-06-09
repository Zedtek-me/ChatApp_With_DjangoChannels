
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
    let toggleArrows= document.querySelectorAll('.post-tog')
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
function postEdit(){
    let removeBtns= document.querySelectorAll('#delete-quest')
    let formBtns= document.querySelectorAll('#removePost')
    let confirmCont= document.querySelectorAll('.confirm-del')
    let yesCont= document.querySelectorAll("[name='yesBtn']")
    let noCont= document.querySelectorAll("[name='noBtn']")
    for(let i= 0; i < removeBtns.length; i++){
        removeBtns[i].addEventListener('click', (e)=>{
            confirmCont[i].style.display= 'flex'//displays the confirmation box

            yesCont[i].addEventListener('click', (e)=>{//checks whether yes is clicked
                formBtns[i].click()// submit post for deletion if yes
            })

            noCont[i].addEventListener('click', (e)=>{//in case no is chosen
                confirmCont[i].style.display= 'none'
            })
        })
    }

}

postEdit()
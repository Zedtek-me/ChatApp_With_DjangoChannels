const API_KEY=  'pub_3010c2abf31e8a1aff7da956efcfef4bdf12'
var endPoint= 'https://newsdata.io/api/1/news?apikey=' + API_KEY + '&country=us,au';

var request= new Request(endPoint);

fetch(request)
.then((response)=>{
    return response.json()})
.then((data)=>{
        let newInfo = data.results;
        newInfo.forEach((news)=>{
            let trendContainer= document.querySelector(".all-trends")
            let subContainer= document.createElement("DIV")
            let innerItems= ['H1', 'IMG', 'P', 'A']
            // for h1
            let h1= document.createElement(innerItems[0])
            h1.setAttribute('id', 'title')
            h1.innerHTML=news.title
            subContainer.appendChild(h1)
            // for image
            let img= document.createElement(innerItems[1])
            img.setAttribute('src', news.image_url)
            img.setAttribute('alt', 'No Image Available')
            img.setAttribute('id', 'trend-img')
            subContainer.appendChild(img)
            // for paragraph
            let p= document.createElement(innerItems[2])
            p.setAttribute('class', 'description')
            p.innerHTML= news.description
            subContainer.appendChild(p)
            // for link
            let a= document.createElement(innerItems[3])
            a.setAttribute('href', news.link)
            a.setAttribute('id', 'read-more')
            a.innerHTML='Read More...'
            subContainer.appendChild(a)
            trendContainer.appendChild(subContainer)
        })   
    })



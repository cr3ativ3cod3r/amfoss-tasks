var city=document.querySelector('#city-in')
var submitButton = document.querySelector('#sub')
var temp=document.querySelector('#temperature')
var climate=document.querySelector('#climate')



apik = "89903746d62e6d60bf2ca2b1676ec92c"
    
    submitButton.addEventListener('click',function(e)
    {
    fetch('https://api.openweathermap.org/data/2.5/weather?q='+city.value+'&appid='+apik)
    .then(response => response.json())
    
    .then(data =>
        {
            console.log(data)
            var citydata=city
            var climatedata=data['weather']['0']['main']
            var tempdata=(data['main']['temp']-273).toFixed(2)
            city.innerHTML=citydata
            climate.innerHTML=climatedata
            temp.innerHTML=tempdata
        })

    .catch(error => 
    {
        console.error('Error fetching', error);
    })
   })

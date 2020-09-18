document.addEventListener('DOMContentLoaded', function() {

getData()

});
////////Below Function Loads the entire India map after getting data from getData() function///////////////
function loadmap(data){
if (window.innerWidth <= 800)
{
var scl = 650
var lat = 109.9629
var long = 23.5937
}
else
{
var scl = 1000
var lat = 93.9629
var long = 24.5937
}
var map = new Datamap({
            element: document.getElementById('india'),
            scope: 'india',
            responsive: false,
            fills: {
                'MAJOR': '#660000',
                'MEDIUM': '#e60000',
                'MINOR': '#ff6666',
                defaultFill: '#ffcccc'
            },
            data: data,
            geographyConfig: {
                popupOnHover: true,
                highlightOnHover: true,
                borderColor: '#000000',
                borderWidth: 1,
                dataUrl: 'https://rawgit.com/Anujarya300/bubble_maps/master/data/geography-data/india.topo.json',
                popupTemplate: function(geo, data) {
                return ['<div class="hoverinfo"><strong>',
                        'ACTIVE cases ' + geo.properties.name,
                        ': ' + data.numberOfThings,
                        '</strong></div>'].join('');}
            },
            setProjection: function (element) {
                var projection = d3.geo.mercator()
                    .center([lat, long]) // always in [East Latitude, North Longitude]
                    .scale(scl);
                var path = d3.geo.path().projection(projection);
                return { path: path, projection: projection };

            }

});
window.addEventListener('resize', function() {
        map.resize();
    });
}
///////////////Loadmap function ends here////////////////////////////
///////////////////////daily trend function//////////////////////////////
function dailytrend(data,numbr){
var corona_data = data
var options = {
          series: [{
            name: "Daily New Cases",
            data: corona_data[0]
        },
	{
            name: "Daily Recovered",
            data: corona_data[1]
          },
         {
            name: "Daily Deaths",
            data: corona_data[2]
          } ],
          chart: {
          height: 350,
          type: 'line',
          zoom: {
            enabled: true
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Daily trends',
          align: 'left'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
          },
        },
        xaxis: {
          categories: corona_data[3],
        }
        };
        if(numbr===undefined){//when numbr is undefined the apex chart loads the chart fr the whole country
        var chart = new ApexCharts(document.querySelector("#chart"), options);
        }
        else
        {
        document.querySelector(".statewisedata").innerHTML="";
        var chart = new ApexCharts(document.querySelector(".statewisedata"), options);
        }
        chart.render();

}
/////////////////////////daily trend function ends here/////////////////////
///////////////function to populate data in the table starts her///////////////
function datatable(data)
{
		var table = document.getElementById('myTable')

		for (var i = 0; i < data.length; i++){
			var row = `<tr>
							<td><a href="#statewise-daily-trend" id="${data[i].id}" onclick="stategraph(this);">${data[i].state_name}</a></td>
							<td>${data[i].confirmed_corona_cases}</td>
							<td>${data[i].recovered_corona_cases}</td>
							<td>${data[i].confirmed_corona_cases - data[i].recovered_corona_cases - data[i].deaths_corona_cases}</td>
							<td>${data[i].deaths_corona_cases}</td>
							</tr>`
			table.innerHTML += row


		}

}
////////////////function to populate data in the table ends here/////////////////////

function getData(){
//////////////This api loads the Datamap's data//////////////////////
fetch("indiamap")
.then(response => response.json())
.then(data => {
loadmap(data)
})
////////////data map api ends here///////////////////////////

///////////below api loads the daily trend map///////////////////
fetch("dailytrend/country")
.then(response => response.json())
.then(data => {
dailytrend(data)
})
///////////daily trend map ends here//////////////////////////////

//////////datatable api starts here///////////////////////
fetch("datatable")
.then(response => response.json())
.then(data => {
datatable(data)

})
/////////////datatable api ends here
}
/////////////stategraph starts here///////////////////
function stategraph(name){
var numbr = name.id;
var state = name.innerHTML
document.querySelector("#clicked-state").innerHTML="Below chart shows the Daily Trends of "+`${state}`;
fetch(`dailytrend/${state}`)
.then(response => response.json())
.then(data => {
dailytrend(data,numbr);//here I call the daily trend function and i pass the state number and data of that particular state in it
})
}
/////////////stategraph ends here///////////////////
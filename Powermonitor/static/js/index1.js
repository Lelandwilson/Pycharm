var watts_amps_bool = true;
var watts_amps_bool2 = true;
var watts_amps_bool3 = true;
var watts_amps_bool4 = true;
var watts_amps_bool5 = true;
var lineChart1;
var pieChart1;
 //------------------- <!--Load HOUR Charts--> ------------------- //
function updateChart(){
    try{
        if (watts_amps_bool == false){          // Display Amps //
            // console.log("Update: Amps");
            var updatedData = $.get('/hour_data');

            updatedData.done(function(hour_results){
                var data= {
                labels: hour_results.Xlabels,
                series: hour_results.data
                };

                var options = {
                    <!--height : 400,-->
                    high: 100,
                    low: 0,
                    fullwidth: true,
                    //showPoint: false,
                    plugins: [
                        Chartist.plugins.legend({
                        legendNames: hour_results.names,
                        position: legendDiv
                        })
                    ]
                };

                var pie_data = {
                    labels: hour_results.pieLables,
                    series: hour_results.pieData
                };

            $( "#legendDiv" ).empty();
            lineChart1 = new Chartist.Line('.hour_line_chart', data, options);
            pieChart1 = new Chartist.Pie('.pie_chart', pie_data);

            });
        } 
        else{                      // Display Watts //
            // console.log("Update: Watts");
            var updatedData = $.get('/hour_data');
            updatedData.done(function(hour_results){
                var input = [];
                var output = [];
//                labels = hour_results.Xlabels;
                input = hour_results.data;

                if(input[0].length > 1){
                    for (var x=0; x < input.length; x++){
                        output[x] = new Array(0);
                        for(var y =0; y < input[x].length; y++){
                            var number = input[x][y];
                            number = number * 240;
                            number = number.toFixed(2);
                            output[x].push(number);
                        }
                    }
                }

                else{
                    for (var i=0; i < input.length; i++){
                        var number = input[i]*240;
                        number = number.toFixed(2);
                        output[i] = new Array(0);
                        output[i].push(number);
                    }
                }
                var data= {
                labels: hour_results.Xlabels,
                series: output
                };

                var options = {
                    low: 0,
                    fullwidth: true,
                    //showPoint: false,
                    plugins: [
                        Chartist.plugins.legend({
                        legendNames: hour_results.names,
                        position: legendDiv
                        })
                    ]
                };

                var pie_data = {
                    labels: hour_results.pieLables,
                    series: hour_results.pieData
                };

            $( "#legendDiv" ).empty();
            lineChart1 = new Chartist.Line('.hour_line_chart', data, options);
            pieChart1 = new Chartist.Pie('.pie_chart', pie_data);

            });
        }
    }
    catch(err){
        console.log(err)
    }

}

//-------------------  <!--Load Day Charts--> -------------------//
function Day_updateChart(){
    if (watts_amps_bool2 == false){          // Display Amps //
        // var input = [];
        // var output = [];
        var lineChart2;
        var getData2 = $.get('/day_data');

        getData2.done(function(day_results) {
            var data2= {
            labels: day_results.Day_Xlabels,
            series: day_results.Day_data
            };

            var day_options = {
                <!--height : 400,-->
                high: 100,
                low: 0,
                fullwidth: true,
                //showPoint: false,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: day_results.Day_names,
                    position: day_legendDiv
                    })
                ]
            };

            var day_pie_data = {
                labels: day_results.Day_pieLables,
                series: day_results.Day_pieData

            };
            //console.log(day_results.Day_data)
            $( "#day_legendDiv" ).empty();
            lineChart2 = new Chartist.Line('.day_line_chart', data2, day_options);
            pieChart2 = new Chartist.Pie('.day_pie_chart', day_pie_data);

        });
    }
    else{       // Display Watts //
        // console.log("Update: Watts");
        var updatedData = $.get('/day_data');
        updatedData.done(function(day_results){
            var input = [];
            var output = [];
            //labels = day_results.Day_Xlabels;
            input = day_results.Day_data;

            if(input[0].length > 1){
                for (var x=0; x < input.length; x++){
                    output[x] = new Array(0);
                    for(var y =0; y < input[x].length; y++){
                        var number = input[x][y];
                        number = number * 240;
                        number = number.toFixed(2);
                        output[x].push(number);
                    }
                }
            }

            else{
                for (var i=0; i < input.length; i++){
                    var number = input[i]*240;
                    number = number.toFixed(2);
                    output[i] = new Array(0);
                    output[i].push(number);
                    }
            }
            var data2= {
                labels: day_results.Day_Xlabels,
                series: output
            };

            var day_options = {
                low: 0,
                fullwidth: true,
                //showPoint: false,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: day_results.Day_names,
                    position: day_legendDiv
                    })
                ]
            };

            var day_pie_data = {
                labels: day_results.Day_pieLables,
                series: day_results.Day_pieData
            };

            // console.log(day_pie_data)
            $( "#day_legendDiv" ).empty();
            lineChart2 = new Chartist.Line('.day_line_chart', data2, day_options);
            pieChart2 = new Chartist.Pie('.day_pie_chart', day_pie_data);
        });
    }
}


// <!--------------------- Load Week Charts -------------------> //
function Week_updateChart(){        // Display Amps //
    if (watts_amps_bool3 == false){
        // var input = [];
        // var output = [];
        var lineChart3;
        var getData3 = $.get('/week_data');

        getData3.done(function(week_results) {
            var data3= {
                labels: week_results.Week_Xlabels,
                series: week_results.Week_data
                };

            var week_options = {
                //<!--height : 400,-->
                high: 1000,
                low: 0,
                fullwidth: true,
                //showPoint: false,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: week_results.Week_names,
                    position: week_legendDiv
                    })
                ]
            };


            var week_pie_data = {
                labels: week_results.Week_pieLables,
                series: week_results.Week_pieData

            };
            //console.log(week_results.Week_data)
            $( "#week_legendDiv" ).empty();
            lineChart3 = new Chartist.Line('.week_line_chart', data3, week_options);
            pieChart3 = new Chartist.Pie('.week_pie_chart', week_pie_data);

        });
    }
    else{          // Display Watts //
            // console.log("Update: Watts");
            var updatedData = $.get('/week_data');
            updatedData.done(function(week_results){
                var input = [];
                var output = [];
                // labels = week_results.Week_Xlabels;
                input = week_results.Week_data;

            if(input[0].length > 1){
                for (var x=0; x < input.length; x++){
                    output[x] = new Array(0);
                    for(var y =0; y < input[x].length; y++){
                        var number = input[x][y];
                        number = number * 240;
                        number = number.toFixed(2);
                        output[x].push(number);
                    }
                }
            }

            else{
                for (var i=0; i < input.length; i++){
                    var number = input[i]*240;
                    number = number.toFixed(2);
                    output[i] = new Array(0);
                    output[i].push(number);
                    }
            }
            var data3= {
                labels: week_results.Week_Xlabels,
                series: output
            };

            var week_options = {
                //high: 1000,
                low: 0,
                fullwidth: true,
                //showPoint: false,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: week_results.Week_names,
                    position: week_legendDiv
                    })
                ]
            };


            var week_pie_data = {
                labels: week_results.Week_pieLables,
                series: week_results.Week_pieData

            };
            //console.log(week_results.Week_data)
            $( "#week_legendDiv" ).empty();
            lineChart3 = new Chartist.Line('.week_line_chart', data3, week_options);
            pieChart3 = new Chartist.Pie('.week_pie_chart', week_pie_data);

        });
    }
}


// <!-----------------Load Month Charts--------------------->
function Month_updateChart(){
    if (watts_amps_bool4 == false){  
        var lineChart4;
        var getData4 = $.get('/month_data');

        getData4.done(function(month_results) {
            var data4= {
                labels: month_results.Month_Xlabels,
                series: month_results.Month_data
                };


            var month_options = {
                high: 1000,
                low: 0,
                fullwidth: true,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: month_results.Month_names,
                    position: month_legendDiv
                    })
                ]
            };


            var month_pie_data = {
                labels: month_results.Month_pieLables,
                series: month_results.Month_pieData

            };
            //console.log(month_results.Month_data)
            $( "#month_legendDiv" ).empty();
            pieChart4 = new Chartist.Pie('.month_pie_chart', month_pie_data);
            lineChart4 = new Chartist.Line('.month_line_chart', data4, month_options);

        });
    }
    else{       // Display Watts //
            // console.log("Update: Watts");
            var updatedData = $.get('/month_data');
            updatedData.done(function(month_results){
                var input = [];
                var output = [];
                //labels = month_results.Month_Xlabels;
                input = month_results.Month_data;

                if(input[0].length > 1){
                    for (var x=0; x < input.length; x++){
                        output[x] = new Array(0);
                        for(var y =0; y < input[x].length; y++){
                            var number = input[x][y];
                            number = number * 240;
                            number = number.toFixed(2);
                            output[x].push(number);
                        }
                    }
                }

                else{
                    for (var i=0; i < input.length; i++){
                        var number = input[i]*240;
                        number = number.toFixed(2);
                        output[i] = new Array(0);
                        output[i].push(number);
                        }
                }
                var data4= {
                    labels: month_results.Month_Xlabels,
                    series: output
                };

                var month_options = {
                    low: 0,
                    fullwidth: true,
                    //showPoint: false,
                    plugins: [
                        Chartist.plugins.legend({
                        legendNames: month_results.Month_names,
                        position: month_legendDiv
                        })
                    ]
                };

                var month_pie_data = {
                    labels: month_results.Month_pieLables,
                    series: month_results.Month_pieData
                };

                // console.log(month_pie_data)
                $( "#month_legendDiv" ).empty();
                lineChart4 = new Chartist.Line('.month_line_chart', data4, month_options);
                pieChart4 = new Chartist.Pie('.month_pie_chart', month_pie_data);
            });
        }
    }

// <!--Load Year Charts-->
function Year_updateChart(){
    if (watts_amps_bool5 == false){          // Display Amps //
        var lineChart5;
        var getData5 = $.get('/year_data');

        getData5.done(function(year_results) {
            var data5= {
                labels: year_results.Year_Xlabels,
                series: year_results.Year_data
                };


            var year_options = {
                high: 1000,
                low: 0,
                fullwidth: true,
                //fullwidth: true,
                //showPoint: false,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: year_results.Year_names,
                    position: year_legendDiv
                    })
                ]
            };


            var year_pie_data = {
                labels: year_results.Year_pieLables,
                series: year_results.Year_pieData

            };
            //console.log(year_results.Year_data)
            $( "#year_legendDiv" ).empty();
            lineChart5 = new Chartist.Line('.year_line_chart', data5, year_options);
            pieChart5 = new Chartist.Pie('.year_pie_chart', year_pie_data);

        });
    }
    else{       // Display Watts //
        // console.log("Update: Watts");
        var updatedData = $.get('/year_data');
        updatedData.done(function(year_results){
            var input = [];
            var output = [];
            //labels = year_results.Year_Xlabels;
            input = year_results.Year_data;

            if(input[0].length > 1){
                for (var x=0; x < input.length; x++){
                    output[x] = new Array(0);
                    for(var y =0; y < input[x].length; y++){
                        var number = input[x][y];
                        number = number * 240;
                        number = number.toFixed(2);
                        output[x].push(number);
                    }
                }
            }

            else{
                for (var i=0; i < input.length; i++){
                    var number = input[i]*240;
                    number = number.toFixed(2);
                    output[i] = new Array(0);
                    output[i].push(number);
                    }
            }
            var data5= {
                labels: year_results.Year_Xlabels,
                series: output
            };

            var year_options = {
                low: 0,
                fullwidth: true,
                //showPoint: false,
                plugins: [
                    Chartist.plugins.legend({
                    legendNames: year_results.Year_names,
                    position: year_legendDiv
                    })
                ]
            };

            var year_pie_data = {
                labels: year_results.Year_pieLables,
                series: year_results.Year_pieData
            };

            // console.log(year_pie_data)
            $( "#year_legendDiv" ).empty();
            lineChart5 = new Chartist.Line('.year_line_chart', data5, year_options);
            pieChart5 = new Chartist.Pie('.year_pie_chart', year_pie_data);
        });
    }
}


// <!--change HOUR chart from amps to watts-->
document.getElementById("watt_amps_toggle").onchange = function () {
    if ($(this).is(':checked')) {
        switchStatus = $(this).is(':checked');
        watts_amps_bool = true;

    }
    else {
       switchStatus = $(this).is(':checked');
        watts_amps_bool = false;

    }
    $( "#legendDiv" ).empty();

    updateChart();

    
};
// <!--change DAY chart from amps to watts-->
document.getElementById("watt_amps_toggle2").onchange = function () {
    if ($(this).is(':checked')) {
        switchStatus = $(this).is(':checked');
        watts_amps_bool2 = true;


    }
    else {
       switchStatus = $(this).is(':checked');
        watts_amps_bool2 = false;
    }
    $( "#day_legendDiv" ).empty();
    Day_updateChart();  
};

// <!--change WEEK chart from amps to watts-->
document.getElementById("watt_amps_toggle3").onchange = function () {
    if ($(this).is(':checked')) {
        switchStatus = $(this).is(':checked');
        watts_amps_bool3 = true;


    }
    else {
       switchStatus = $(this).is(':checked');
        watts_amps_bool3 = false;
    }
    $( "#week_legendDiv" ).empty();
    Week_updateChart();
};



// <!--change MONTH chart from amps to watts-->
document.getElementById("watt_amps_toggle4").onchange = function () {
    if ($(this).is(':checked')) {
        switchStatus = $(this).is(':checked');
        watts_amps_bool4 = true;


    }
    else {
       switchStatus = $(this).is(':checked');
        watts_amps_bool4 = false;
    }
    $( "#month_legendDiv" ).empty();
    Month_updateChart();
};


// <!--change YEAR chart from amps to watts-->
document.getElementById("watt_amps_toggle5").onchange = function () {
    if ($(this).is(':checked')) {
        switchStatus = $(this).is(':checked');
        watts_amps_bool5 = true;


    }
    else {
       switchStatus = $(this).is(':checked');
        watts_amps_bool5 = false;
    }
    $( "#year_legendDiv" ).empty();
    Year_updateChart();
};



// <!--Settings button link-->
document.getElementById("Settings").onclick = function () {
    location.href = "/settings";
};


// <!--Tabs-->
function open_tab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
  // <!--console.log(tabName);-->
  if(tabName == 'Past_hour'){updateChart();}
  if(tabName == 'Past_day'){Day_updateChart();}
  if(tabName == 'Past_week'){Week_updateChart();}
  if(tabName == 'Past_month'){Month_updateChart();}
  if(tabName == 'Past_year'){Year_updateChart();}

}
// <!--Set Phr Tab as default open tab-->
document.getElementById("PHr_btn").click();


// <!--Reload chart after x time-->
  // for (i = 0; i < 150; i++) {
  //   var timeout1 = setInterval(updateChart, 30000);
  //   var timeout2 = setInterval(Day_updateChart, 30000);
  // }

var timeout1 = setInterval(updateChart, 30000);
var timeout2 = setInterval(Day_updateChart, 30000);







$(function() {
    var tempF = {
        name: 'Temperature (F)',
        data: [],
    } 

    $.getJSON("/temperature_json", function(data) { 
        $.each(data, function(key, value) {
            $.each(value, function(k, v) {
                if(key == 'timestamp') {
                    tempF.data.push([(v * 1000)]);
                }
                else {
                    tempF.data[k].push(parseFloat(v));
                }
            });
        });
        $('#temperature').highcharts({
            chart: {
                title: 'Temperature Over Time',
                type: 'line',
            },
            xAxis: {
                type: 'datetime',
            },
            series: [{
                name: tempF.name,
                data: tempF.data,
            }],
        });
    });
});

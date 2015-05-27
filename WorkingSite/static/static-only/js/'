$(document).ready(function() {
    var tempFOptions = {
        chart: {
            renderTo: 'temperature',
            type: 'line',
        },
        legend: {enabled: false},
        title: {text: 'Temperature Over Time'},
        subtitle: {text: ''},
        xAxis: {title: {text: ''}, labels: {rotation: -45}},
        yAxis: {title: {text: ''}},
        series: [{}],
    }

    var chartDataUrl = "{% url 'chart_data_json' %}";
    $.getJSON(chartDataUrl,
        function(data) {
            console.log(data);
            tempFOptions.xAxis.categories = data['chart_data']['dates'];
            tempFOptions.series[0].name = 'Temperatures';
            tempFOptions.series[0].data = data['chart_data']['values'];
            var chart = new Highcharts.Chart(tempFOptions);
        });
});

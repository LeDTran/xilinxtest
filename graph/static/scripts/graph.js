var t1=[], t2=[], t3=[], t4=[];

t1=JSON.parse("{{test1|safe}}");
t2=JSON.parse("{{test2|safe}}");
t3=JSON.parse("{{test3|safe}}");
t4=JSON.parse("{{final|safe}}");


var trace1 = {
    y: t1, 
    name: 'Test 1',
    type: 'box',
    boxmean: 'sd',
    boxpoints: 'suspectedoutliers'
};

var trace2 = {
    y: t2,
    name: 'Test 2',
    type: 'box',
    boxmean: 'sd',
    boxpoints: 'suspectedoutliers'
};

var trace3 = {
    y: t3,
    name: 'Test 3',
    type: 'box',
    boxmean: 'sd',
    boxpoints: 'suspectedoutliers'
}

var trace4 = {
    y: t4,
    name: 'Final',
    type: 'box',
    boxmean: 'sd',
    boxpoints: 'suspectedoutliers'
}

var data = [trace1, trace2, trace3, trace4];

var layout = {
    title: '2017 Test Scores',
    boxgap: 0.75, 
};

Plotly.newPlot('graphDiv', data, layout);   
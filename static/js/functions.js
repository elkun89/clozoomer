<script>

$(document).ready(function(){

	// $(#html).click(function(){
	// 	alert("Value: " + $("#test").html());
	// });	

	$("#showHtml").click(function(){
    	alert("Text: " + $("#test").html());
  	});

	$("#clear").click(function(){
		var clear = '';
		$("#apparel").html(clear);
		$("#categories").html(clear);
		$("#profile").html(clear);
	});
	// $("button").click(function(){
 //    	alert("Value: " + $("#test").val());
 //  	});


// function request() {
// 	$.getJSON('http://130.215.126.187:8000/rest/brands/?format=json', function(data) {
// 		var item = '';

// 		window.alert('hello');

// 		for(i = 0; i < data.length; i++){
// 			if(jQuery.inArray(data[i].id, itemIDs) == -1 && data[i].title != null){
// 				item = '<a target="_blank" href="'+ data[i].link +'"><div id="item"><p id="source">' + data[i].source + '</p><p id="title">' +data[i].title + '</p><p id="date">' + data[i].date + '</p></p><hr/></a>';
// 				itemIDs.push(data[i].id);


// 				$(item).insertAfter("#top").hide().fadeIn("slow");
// 			}
// 		}
// 	});

// 	if(query != 'new'){ $('p').highlight(query); }
// }

// function query_get(){    
// 	var querystr = window.location.href.split("?q=");   
// 	return querystr[1];   
// }
});

function getTypeName(id){	
	var insert = "";
	var apparelName;
	$.ajax({
		type: 'GET',
		url: 'getApparelType/' + id + '/',
		async : false,
		contentType: "application/json",
		success: function(data) {
			apparelName = data.name;
			// insert = insert + "Name: " + apparelName + "<br>";
			// $("#apparelType").append(insert);
		},
		error: function(e) {
			alert('error!');
		}
	});
	return apparelName;
};

function getLocationName(id){	
	var insert = "";
	var locationName;
	$.ajax({
		type: 'GET',
		url: 'rest/locations/' + id + '/',
		async : false,
		contentType: "application/json",
		success: function(data) {
			locationName = data.address;
		},
		error: function(e) {
			alert('error!');
		}
	});
	return locationName;
};

function apparel_request(){
	$.ajax({
		type: 'GET',
		url: 'apparel',
		contentType: "application/json",
		success: function(data) {
			var apparelName;
			var locationName;
			var insert = "List of User's Apparel: <br>";
			for (var i = 0; i < data.length; i++) {
				apparelName = getTypeName(data[i].type);
				locationName = getLocationName(data[i].locationOfPurchase);	
				insert = insert + "Name: " + apparelName + "<br>";
			    insert = insert + "Purchase Time: " + data[i].timeOfCreation + "<br>";
			    insert = insert + "Location: " + locationName + "<br>";

			    // $("#apparel").append($("apparelType"), $(apparelInstance));
			    // $("#apparelType").clear;
			    // $("#apparelInstance").clear;
			}
			$("#apparel").html(insert);
		},
		error: function(e) {
			alert('error!');
		}
	});
};

function category_request(){
	$.ajax({
		type: 'GET',
		url: 'http://localhost:8000/categories',
		contentType: "application/json",
		success: function(data) {
			var insert = '';
			for (var i = 0; i < data.length; i++) {
			    insert = insert + data[i].name + "<br>";
			}
			$("#categories").html(insert);
		},
		error: function(e) {
			alert('error!');
		}
	});
};

function profile_request(){
	$.ajax({
		type: 'GET',
		url: 'http://localhost:8000/userProfile',
		contentType: "application/json",
		success: function(data) {
			var insert = 'Profile: <br>';
			for (var i = 0; i < data.length; i++) {
			    insert = insert + "Username: " + data[i].username + "<br>";
			    insert = insert + "Email: " + data[i].email + "<br>";
			}
			$("#profile").html(insert);
		},
		error: function(e) {
			alert('error!');
		}
	});
};


// function request_html(){
//  	alert("Value: " + $("p").html());
// };

function add_category(){
		var form = '';
		form = form + '<form id = "add_category" method = "POST" action = "addCategory">';
};
</script>

function clean(){
  $("#main_board").html("");
  $("#add_apparel_bar").html("");
  $("#post_bar").html("");
};

function show_livefeed(){
    clean();
    $.ajax({
    type: 'GET',
    url: '/getPosts',
    success: function(data) {
      $("#main_board").html(data);
    },
    error: function(e) {
      alert('error!');
    }
  });
  var hashVal = 'show_livefeed';
  window.location.hash = '#' + hashVal;
};

function getTypeData(id){
  var insert = "";
  var apparelData;
  $.ajax({
    type: 'GET',
    url: '/getApparelType/' + id + '/',
    async : false,
    contentType: "application/json",
    success: function(data) {
      apparelData = data;
      // insert = insert + "Name: " + apparelName + "<br>";
      // $("#apparelType").append(insert);
    },
    error: function(e) {
      alert('error!');
    }
  });
  return apparelData;
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
    }
  });
  return locationName;
};

function category_request(){
  $.ajax({
    type: 'GET',
    url: '/categories',
    contentType: "application/json",
    success: function(data) {
      var insert = '';
      for (var i = 0; i < data.length; i++) {
          insert = insert + data[i].name + "<br>";
      }
      $("#categories").html(insert);
    },
    error: function(e) {
    }
  });
};

function friends_request(){
  clean();
  var clear = '';
  $("#main_board").html(clear);
  $.ajax({
    type: 'GET',
    url: '/getFriends',
    contentType: "application/json",
    success: function(data) {
      var insert = 'Friends: <br>';
      for (var i = 0; i < data.length; i++) {
          insert = insert + "Name: " + data[i].first_name + " " + data[i].last_name + "<br>";
          insert = insert + "Email: " + data[i].email + "<br>";
      }
      $("#main_board").html(insert);
    },
    error: function(e) {
      alert('error!');
    }
  });
  var hashVal = 'friends_request';
  window.location.hash = '#' + hashVal;
};

function profile_request(){
  $.ajax({
    type: 'GET',
    url: '/userProfile',
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
    }
  });
}

function apparel_nojson_request(){
  clean();
  $.ajax({
    type: 'GET',
    url: 'listApparelInstance',
    success: function(data) {
      $("#main_board").html(data);
    },
    error: function(e) {
      alert(e);
    }
  });
  var hashVal = 'apparel_nojson_request';
  window.location.hash = '#' + hashVal;
}

function show_profilepic(){
  var clear = '';
  $("#profilepic_photo").html(clear);

  $.ajax({
    type: 'GET',
    url: 'getFriends',
    contentType: "application/json",
    success: function(data) {
      alert(data[0].email);
      var insert = '';
      insert = insert + '<img src = "../static/images/';
      insert = insert + data[0].profilePictureLink;
      insert = insert + '" HEIGHT="200" WIDTH="138" BORDER="1">';
      $("#profilepic_photo").html(insert);
    },
    error: function(e) {
      alert(e);
    }
  });
}

function create_post(){
  clean();
  $.ajax({
    type: 'GET',
    url: '/newPost',
    success: function(data) {
      $("#post_bar").html(data);
    },
    error: function(e) {
      alert('error!');
    }
  });
  show_livefeed();
  var hashVal = 'create_post';
  window.location.hash = '#' + hashVal;
};

function add_apparel(){
  clean();
  $.ajax({
    type: 'GET',
    url: '/addApparelInstance',
    success: function(data) {
      $("#add_apparel_bar").html(data);
    },
    error: function(e) {
      alert('error!');
    }
  });
  apparel_nojson_request();
  var hashVal = 'add_apparel';
  window.location.hash = '#' + hashVal;
};

function show_friend_request(){
  clean();
  $.ajax({
    type: 'GET',
    url: '/showFriendRequest',
    success: function(data) {
      $("#main_board").html(data);
    },
    error: function(e) {
      alert('error!');
    }
  });
  var hashVal = 'show_friend_request';
  window.location.hash = '#' + hashVal;
}

function request_friend(){
  clean();
  $.ajax({
    type: 'GET',
    url: '/requestFriend',
    success: function(data) {
      $("#main_board").html(data);
    },
    error: function(e) {
      alert('error!');
    }
  });
  var hashVal = 'request_friend';
  window.location.hash = '#' + hashVal;
}

function request_friend_success(){
  clean();
  $("#main_board").html("message sent");
  var hashVal = 'request_friend_success';
  window.location.hash = '#' + hashVal;
}

function edit_profile(){
  clean();
  $.ajax({
    type: 'GET',
    url: '/editProfile',
    success: function(data) {
      $("#main_board").html(data);
    },
    error: function(e) {
      alert('error!');
    }
  });
  var hashVal = 'edit_profile';
  window.location.hash = '#' + hashVal;
}


$(document).ready(function(){
  // using jQuery
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      crossDomain: false, // obviates need for sameOrigin test
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type)) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  //hanles conditions with no specific hashed url
  var hash = window.location.hash.substr(1);
  if(hash){
    var func = window[hash];
    try{
      func();
    }
    catch(err){
      show_livefeed();
    }
  }
  else{
    show_livefeed();
  }

  //registers call back functions to the events
  $('#stream').click(show_livefeed);
  $('#new_post').click(create_post);
  $('#closet').click(apparel_nojson_request);
  $('#new_apparel').click(add_apparel);
  $('#followers').click(friends_request);
  $('#show_requests').click(show_friend_request);
  $('#add_followers').click(request_friend);
  $('#top_bar').click(show_livefeed);
  $('#edit_profile_id').click(edit_profile);

  /* attach a submit handler to the form */
  $("#search_form").submit(function(event) {
    console.log('Trigger');
    /* stop form from submitting normally */
    event.preventDefault();
   
    /* get some values from elements on the page: */
    var form = $("#search_form");

    var form_url = '/search/';
   
    $.ajax({
      type:'POST',
      url:form_url,
      data:form.serialize(),
      success:function(data){
        $("#main_board").html(data);
        console.log(data);
      },
      error: function(data){
        $("#main_board").html('ajax request error');
      }
    });
  });
});

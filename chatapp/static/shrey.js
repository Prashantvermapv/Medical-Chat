$('#chat-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/post/',
        type : 'POST',
        data : { msgbox : $('#chat-msg').val() },

        success : function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="text-left query list-group-item">' + json.query + '</li>')
            $('#msg-list').append('<li class="text-left response list-group-item">' + json.response + '</li>')
            $('#msg-list').append('<li class="text-left suggestions list-group-item">' + json.sug1 + '</li>')
            $('#msg-list').append('<li class="text-left suggestions list-group-item">' + json.sug2 + '</li>')
            $('#msg-list').append('<li class="text-left suggestions list-group-item">' + json.sug3 + '</li>')
            $('#msg-list').append('<li class="text-left suggestions list-group-item">' + json.sug4 + '</li>');
            var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        }
    });
});

var scrolling = false;
$(function(){
    $('#msg-list-div').on('scroll', function(){
        scrolling = true;
    });
    refreshTimer = setInterval(getMessages, 500);
});

$(document).ready(function() {
     $('#send').attr('disabled','disabled');
     $('#chat-msg').keyup(function() {
        if($(this).val() != '') {
           $('#send').removeAttr('disabled');
        }
        else {
        $('#send').attr('disabled','disabled');
        }
     });
 });

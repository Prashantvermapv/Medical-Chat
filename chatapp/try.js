$('#chat-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/post/',
        type : 'POST',
        data : { msgbox : $('#chat-msg').val() },

        success : function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<div class="text-left query">' + json.query + '</div>')
            $('#msg-list').append('<div class="text-right response">' + json.response + '</div>')
            $('#msg-list').append('<div class="text-left suggestions">' + json.sug1 + '</div>')
            $('#msg-list').append('<div class="text-left suggestions">' + json.sug2 + '</div>')
            $('#msg-list').append('<div class="text-left suggestions">' + json.sug3 + '</div>')
            $('#msg-list').append('<div class="text-left suggestions">' + json.sug4 + '</div>');
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

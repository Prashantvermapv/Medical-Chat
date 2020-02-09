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
            $('#sugg1').replaceWith('<div class="col-sm-3" style="background-color:white;"><button type="button" class="btn btn-default" id="sugg1">'+ json.sug1 +'</button></div>')
            $('#sugg2').replaceWith('<div class="col-sm-3" style="background-color:white;"><button type="button" class="btn btn-default" id="sugg2">'+ json.sug2 +'</button></div>')
            $('#sugg3').replaceWith('<div class="col-sm-3" style="background-color:white;"><button type="button" class="btn btn-default" id="sugg3">'+ json.sug3 +'</button></div>')
            $('#sugg4').replaceWith('<div class="col-sm-3" style="background-color:white;"><button type="button" class="btn btn-default" id="sugg4">'+ json.sug4 +'</button></div>');
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
     $("#sugg1").click(function(){
        var value = $(this).html();
        var input = $('#chat-msg');
        input.val(value);
    });
 });

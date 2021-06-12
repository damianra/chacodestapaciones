var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}



$('#send').click(function(){
    var nombre = $('#id_nombre').val()
    var email= $('#id_email').val()
    var telefono = $('#id_telefono').val()
    var mensaje = $('#id_mensaje').val()
    sendData(nombre, email, telefono, mensaje);
});

function sendData(nombre, email, telefono, mensaje){
    $.ajax({  
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},

        url : "/contacto/",
        data: {'nombre': nombre, 'email': email, 'telefono': telefono, 'mensaje': mensaje},
		type : "POST",
        success: function(json){
            if(json.response == 'success'){
                var nombre = document.getElementById('id_nombre');
                nombre.value = '';
                var email = document.getElementById('id_email');
                email.value = '';
                var telefono = document.getElementById('id_telefono');
                telefono.value = '';
                var mensaje = document.getElementById('id_mensaje');
                mensaje.value = '';
                var modaltext = '<p>Mensaje enviado. En breve estaremos respondiendo. Gracias.</p>'
                $('#modalBody').html(modaltext);
            }else{
                var modaltext = '<p style="color: red;">Revise los datos ingresados, uno o mas campos son incorrectos</p>'
                $('#modalBody').html(modaltext);
            }
        },
        error : function(xhr, errmsg, err){
            var modaltext = '<p style="color: red;">Revise los datos ingresados, uno o mas campos son incorrectos</p>'
            $('#modalBody').html(modaltext);
		},

    });
}
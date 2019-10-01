export function Send(){
    $("#AjaxSend").on('click',function(){
        $.ajax({
            url:'./api/first',
            type:'POST',
            dataType: 'html',
            data:{

            }
        })
        .done( (data) => {
            $('body').html(data);
        })
    })
}
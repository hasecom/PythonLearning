
$(function(){
    dom();
});

function dom(){
    $(".firstView").css({
        width:$(window).width() + "px",
        height:$(window).height() + "px",
    });
}
let ajaxParam;
export function ParamSet(val){
    ajaxParam = val;
}
$(document).on('click','.AjaxSend',function(){
    $.ajax({
        url:'./api/first',
        type:'POST',
        dataType: 'html',
        data:{
            param:ajaxParam
        }
    })
    .done( (data) => {
        $('body').html(data);
        dom();
    })
})


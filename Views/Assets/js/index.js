
$(function(){
    dom();
});

function dom(){

}
let ajaxParam;
let aaa = "";
export function ParamSet(val){
    ajaxParam = val;
}
$(document).on('click','.AjaxSend',function(event){
    event.preventDefault();
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
        aaa = "aa";
    })
})
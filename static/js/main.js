$('#show-menu').bind('click',function(){
$('.menu-hidden').show();
$('#show-menu').hide();
$('#close').show();

})
$('#close').bind('click',function(){
$('.menu-hidden').hide();
$('#close').hide();
$('#show-menu').show();
});
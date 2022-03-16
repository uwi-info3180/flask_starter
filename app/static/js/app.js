/* Add your Application JavaScript */
// var activeNavItem = ('.nav-item');

// activeNavItem.click(function(){
//     oldObjChild=$('.active > a'); //gets active nav-item child nav-link
//     oldObj = $('.active'); //gets the active nav-item
//     oldObj.removeClass('active'); //removes active class from active nav-item
//     activeNavItem.removeClass('active');
//     $(this).parent().addClass('active');
    


$(function(){
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault()
        oldObjChild=$('.active > a'); //gets active nav-item child nav-link
        oldObj = $('.active'); //gets the active nav-item
        oldObj.removeClass('active'); //removes active class from active nav-item
        activeNavItem.removeClass('active');
        $(this).parent().addClass('active');
    });
});
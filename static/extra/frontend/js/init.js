$(document).ready(function(){

/**
 * This object controls the nav bar. Implement the add and remove
 * action over the elements of the nav bar that we want to change.
 *
 * @type {{flagAdd: boolean, elements: string[], add: Function, remove: Function}}
 */
var myNavBar = {

    flagAdd: true,

    elements: [],

    init: function (elements) {
        this.elements = elements;
    },

    add : function() {
        if(this.flagAdd) {
            for(var i=0; i < this.elements.length; i++) {
                document.getElementById(this.elements[i]).className += " fixed-theme";
            }
            this.flagAdd = false;
        }
    },

    remove: function() {
        for(var i=0; i < this.elements.length; i++) {
            document.getElementById(this.elements[i]).className =
                    document.getElementById(this.elements[i]).className.replace( /(?:^|\s)fixed-theme(?!\S)/g , '' );
        }
        this.flagAdd = true;
    }

};

/**
 * Init the object. Pass the object the array of elements
 * that we want to change when the scroll goes down
 */
myNavBar.init(  [
    "header",
    "header-container",
    "brand"
]);

/**
 * Function that manage the direction
 * of the scroll
 */
function offSetManager(){

    var yOffset = 0;
    var currYOffSet = window.pageYOffset;

    if(yOffset < currYOffSet) {
        myNavBar.add();
    }
    else if(currYOffSet == yOffset){
        myNavBar.remove();
    }

}

/**
 * bind to the document scroll detection
 */
window.onscroll = function(e) {
    offSetManager();
}

/**
 * We have to do a first detectation of offset because the page
 * could be load with scroll down set.
 */
offSetManager();



/**Owl home-page-slider**/
$('#home-slider').owlCarousel({
    loop:true,
      nav : false, // Show next and prev buttons
      dots : false,
      autoplay : true,
      slideSpeed : 300,
      paginationSpeed : 400,
      items : 1, 
      singleItem:true,
      animateOut: 'fadeOut', 
 
      // "singleItem:true" is a shortcut for:
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
});
/**Owl ots-slider**/
$('#ots-slider').owlCarousel({
      loop:true,
      nav : false, // Show next and prev buttons
      dots : true,
      autoplay : true,
      slideSpeed : 300,
      paginationSpeed : 400,
      items : 1, 
      singleItem:true,
      animateOut: 'fadeOut', 
 
      // "singleItem:true" is a shortcut for:
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
});


/**Owl ole-slider**/
$('#ole-slider').owlCarousel({

      loop:true,
      nav : false, // Show next and prev buttons
      dots : true,
      autoplay : true,
      slideSpeed : 300,
      paginationSpeed : 400,
      items : 1, 
      singleItem:true,
      animateOut: 'slideInDown', 
 
      // "singleItem:true" is a shortcut for:
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
});
/**Owl gallery-slider**/
$('#gallery-slider').owlCarousel({
    loop:true,
      nav : false, // Show next and prev buttons
      dots : true,
      autoplay : true,
      slideSpeed : 300,
      paginationSpeed : 400,  
      animateOut: 'fadeOut', 
      responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
      // "singleItem:true" is a shortcut for:
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
});

/**Owl lupdate-slider**/
$('#lupdate-slider').owlCarousel({
  loop:true,
      nav : false, // Show next and prev buttons
      dots : true,
      autoplay : true,
      slideSpeed : 300,
      paginationSpeed : 400,
      items : 1, 
      singleItem:true,
      animateOut: 'fadeOut', 
 
      // "singleItem:true" is a shortcut for:
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
});

// THE SCRIPT INITIALISATION -->
  //LOOK THE DOCUMENTATION FOR MORE INFORMATIONS --> 

    var revapi;

    jQuery(document).ready(function() {

         revapi = jQuery('.tp-banner').revolution(
        {
          delay:9000,
          startwidth:1170,
          startheight:500,
          hideThumbs:10,
          fullWidth:"on",
          forceFullWidth:"on"
        });

    }); //ready
 

  //END REVOLUTION SLIDER -->



/**Initialization for functions**/
    //Form Input
    function init_input_check(){
    $( ".focus-text" ).each(function() {
    if (($(this).val() != "")) { $(this).closest('div').addClass('focus-t'); }
    });
    }
/**Initialization for functions end**/
/**Input box styling like material design**/
init_input_check();

 
    $('.focus-text').focus(function(){
    $(this).closest('div').addClass('focus-t');
    });

 $('.focus-text').focusout(function(){
     if (($(this).val() == "")) { $(this).closest('div').removeClass('focus-t'); }
   
    });
/**Input box styling like material design end**/

/**dropdown hover**/ 
$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(500);
});
/**dropdown hover end**/ 


}); //redy function end
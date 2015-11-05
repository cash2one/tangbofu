window.jQuery = window.jQuery || {};
(function($){
    function testB() {
        console.log("hello, im A");
    }

    $.testB = testB;
})(jQuery)
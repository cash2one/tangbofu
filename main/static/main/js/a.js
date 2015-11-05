window.jQuery = window.jQuery || {};
(function($){
    function testA() {
        console.log("hello, im A");
    }

    $.testA = testA;
})(jQuery)
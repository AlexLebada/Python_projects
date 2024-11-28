/** code runs after page is ready */
$(document).ready(function(){
    console.log("loaded"); /** this displays in browser console */
    $.material.init();
    /** In case event of form submit is done, execute following */
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log("form submitted");
        var form = $('#register-form').serialize(); /** converts as a query string */
        /** using ajax method(async) we get data/form and send to server without refreshing the page */
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
                print(response)
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();
        console.log("form submitted");
        var form = $('#login-form').serialize(); /** converts as a query string */
        /** using ajax method(async) we get data/form and send to server without refreshing the page */
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(response){
                if(response=="error"){
                    alert("Could not log in."); /** pop-up message */
                }else{
                    console.log("Logged in as", response);
                    /** When logged in, user is redirected to home page*/
                    window.location.href="/";
                }
            }
        })
    });

    $(document).on("click", "#logout-link", function(e){
        e.preventDefault();
        console.log("logout click");
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(response){
                if(response == 'success'){
                    window.location.href="/login";
                    console.log("Logged out");
                }else{
                    alert("Something went wrong");
                }
            }
        });
    });

});
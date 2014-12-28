$(document).ready(function() {
    var height = $(window).height();
    var header_h = $(".header").height();
    var l_pane_h = height - header_h - 35;
    $(".left-pane").css("height", l_pane_h);

    $("#search").on("keyup", function() {

            $('#search').autocomplete({
              minLength: 1,
                dataType: 'json',
              source: "/search?text=" + $("#search").val(),
              focus: function( event, ui ) {
                //$( "#search" ).val( ui.item.code );
                return false;
              },
              select: function( event, ui ) {
                $( "#search" ).val( ui.item.code );
                return false;
              }
            })
            .autocomplete( "instance" )._renderItem = function( ul, item ) {
              return $( "<li>" )
                .append( "<a href='/lecture/" + item.slug + "'>" + item.code + "<br /><span class='search-list-name'>" + item.name + "</span></a>" )
                .appendTo( ul );
            };

    });

$('.dropdown-toggle').dropdown()

    $(".translate").on("click", function () {
        var id = $(this).attr("data-id");
        var url = $(this).attr("data-href");
        var loading = $("#loading-"+id);
        loading.removeClass("hidden");
        console.log(url);
        $.getJSON(url+"&id="+id, function(data) {
            console.log(data.text[0]);
            translate(id, data.text[0]);
            loading.addClass("hidden");
        })

    });



});

var translate = function(id, text) {
    var post = $("#post-"+id);
    console.log(id);
    console.log(text);
    console.log(post);
    post.find(".post-content").addClass("text-muted");
    post.find(".post-content-translated").html(text);
}

















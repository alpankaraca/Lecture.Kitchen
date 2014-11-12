$(document).ready(function() {
    var height = $(window).height();
    var header_h = $(".header").height();
    var l_pane_h = height - header_h - 35;
    $(".left-pane").css("height", l_pane_h);

    $("#search").on("keyup", function() {
        console.log($("#search").val())
        $.getJSON("/search?text=" + $("#search").val(), function(data) {
            console.log(data);
            var datam = ["asd", "das", "dsds"]
            $('#search').autocomplete({
              minLength: 0,
              source: data,
              focus: function( event, ui ) {
                $( "#search" ).val( ui.item.name );
                return false;
              },
              select: function( event, ui ) {
                $( "#search" ).val( ui.item.name );
                return false;
              }
            })
            .autocomplete( "instance" )._renderItem = function( ul, item ) {
                console.log(ul);
                console.log(item.name);
              return $( "<li>" )
                .append( "<a>" + item.name + "</a>" )
                .appendTo( ul );
            };
            //$(".lec-list-container").show();
        });

    });




});


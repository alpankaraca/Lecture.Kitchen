/**
 * Created by alpan on 20.08.2014.
 */
$(document).ready(function() {
    $(".addtocart").click(function() {
       console.log("addtocart");
       var id = $(this).attr("data-id");
        $.post("/cart?addtocart="+id,function(data){
            window.location.reload();
        })
        return false;
    });
    $(".addtocartwithq").click(function() {
       var qu = $(".itemquantity").val();
       var id = $(this).attr("data-id");
        $.post("/cart?addtocart="+id+"&quantity="+qu,function(data){
            window.location.reload();
        })
    });
    $(".del-product").click(function() {
       console.log("addtocart");
       var id = $(this).attr("data-id");
        $.post("/cart?delfromcart="+id,function(data){
            window.location.reload();
        })
    });

});
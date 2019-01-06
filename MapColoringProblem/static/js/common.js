/*
* @Author: Peter
* @Date:   2019-01-04 01:58:39
* @Last Modified by:   Peter
* @Last Modified time: 2019-01-04 02:25:45
*/
function dye() {
    $.ajax({
        type: "get",
        url: "dyemap",
        success: function (response) {
            $("#map").html(response);
        },
        error:function(response){
            
        }
    });
}

function restore() {
    $.ajax({
        type: "get",
        url: "restore",
        success: function (response) {
            $("#map").html(response);
        },
        error:function(response){
            
        }
    });
}
/**
 * Created by Keshav on 11/19/2016.
 */
function addToGroup(username, groupID) {
    $.ajax({
       url : '127.0.0.1:8000/addmember',
       type : 'POST',
       data : { 'username' : username, 'groupID' : groupID },
       success : function (response){},
       error : function () {
           alert('Could not make post request')
       }
    });
}

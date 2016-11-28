/**
 * Created by Keshav on 11/19/2016.
 */
function addToGroup(username, groupID) {
    $.ajax({
       url : 'http://127.0.0.1:8000/addmember/',
       type : 'POST',
       data : { 'username' : username.innerHTML, 'groupID' : groupID },
       success : function (data){
           console.log(data.g_id);
       },
       error : function () {
           alert('Could not make post request')
       }
    });
}
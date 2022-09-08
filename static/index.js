$(document).on('submit','#sendMsg',function(e) {
  console.log('hello');
  e.preventDefault();
  $.ajax({
    type:'POST',
    url:'/',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({data:$("#chatBox").val()}),
    success:function()
    {
      var chatBubble = document.createElement('div');
      chatBubble.innerHTML = this.data;
      chatBubble.style.cssText = 'background-color: #66a4ad; margin: 5px; position: absolute; right: 10px; border-radius: 10px; display: block; padding: 5px;';
      document.getElementById('chats').append(chatBubble);
      // alert('saved' + this.data);
    }
  });
});
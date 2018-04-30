layui.config({
	base : "js/"
}).use(['form','layer','jquery','layedit','laydate'],function(){
	var form = layui.form(),
		layer = parent.layer === undefined ? layui.layer : parent.layer,
		laypage = layui.laypage,
		layedit = layui.layedit,
		laydate = layui.laydate,
		$ = layui.jquery;

	//创建一个编辑器
 	var editIndex = layedit.build('news_content');
 	var addNewsArray = [],addNews;
 	form.on("submit(addNews)",function(data){
 		//是否添加过信息
	 	// if(window.sessionStorage.getItem("addNews")){
	 	// 	addNewsArray = JSON.parse(window.sessionStorage.getItem("addNews"));
	 	// }
	 	//显示、审核状态
 		var isShow = data.field.show=="on" ? "checked" : "",
 			newsStatus = data.field.shenhe=="on" ? "审核通过" : "待审核";

 		addNews = '{"newsName":"'+$(".newsName").val()+'",';  //文章名称
 		addNews += '"newsId":"'+new Date().getTime()+'",';	 //文章id
 		addNews += '"newsLook":"'+$(".newsLook option").eq($(".newsLook").val()).text()+'",'; //开放浏览
 		addNews += '"newsTime":"'+$(".newsTime").val()+'",'; //发布时间
 		addNews += '"newsAuthor":"'+$(".newsAuthor").val()+'",'; //文章作者
 		addNews += '"isShow":"'+ isShow +'",';  //是否展示
 		addNews += '"newsStatus":"'+ newsStatus +'"}'; //审核状态
 		addNewsArray.unshift(JSON.parse(addNews));

 		function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie != '') {
var cookies = document.cookie.split(';');
for (var i = 0; i < cookies.length; i++) {
var cookie = $.trim(cookies[i]);
// Does this cookie string begin with the name we want?
if (cookie.substring(0, name.length + 1) == (name + '=')) {
cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
break;
}
}
}
return cookieValue;
}
function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}



 		//弹出loading
 		var index = top.layer.msg('数据提交中，请稍候',{icon: 16,time:false,shade:0.8});
		   // console.log(addNews);
 			$.ajax({
					type: "post",
					url : "/web/savenewsList/",
					dataType:'json',
					data: addNews,
				    beforeSend: function (xhr, settings) {

					//此处调用刚刚加入的js方法
					var csrftoken = getCookie('csrftoken');
					if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);

					}
					},
					success: function(json){
						// window.sessionStorage.setItem("addNews",JSON.stringify(addNewsArray));
						 setTimeout(function(){
									top.layer.close(index);
									top.layer.msg("文章添加成功！");
									layer.closeAll("iframe");
									//刷新父页面
									parent.location.reload();
                         },2000);
					},
				   error: function(){
                         setTimeout(function(){layer.msg("操作失败！");
                            top.layer.close(index);
                            },1000);
                     }
					});

 		return false;
 	})
	
})

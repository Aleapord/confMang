$(function () {
    var user = sessionStorage.getItem("user");

    $.post({
       url:"../getuser/" ,
        data:{"name":user},
        success:function (data) {
           sessionStorage.setItem("userinf",data.userinf);
           sessionStorage.setItem("userimg",data.userimg);
            $(".blog-name").children("a").html(data.name);
            $(".bio").html("嗨，我叫"+data.name+"。"+data.userinf+"<br><a href=\"about.html\">发现我的更多</a>");
                $(".profile-image").attr('src','/images/'+data.userimg);
        }
    });

    $.ajax({
        url:"getAllConf/",
        success:function (data) {
            $("#text_cont").html("");
            addlist(data);
            addnav();
        }
    })
});

function aboutme() {
    $(".heading").html("我的信息");
    $("#text_cont").html(sessionStorage.getItem("userinf"));


}

function addlist(data) {
    $.each(data,function (idx,obj) {
        $("#text_cont").append("<div class=\"item mb-5\">\n" +
            "\t\t\t\t    <div class='id' style='display: block'>"+idx+"</div> " +
            "<div class=\"media\">\n" +
            "\t\t\t\t\t    <img class=\"mr-3 img-fluid post-thumb d-none d-md-flex\" src=\"/images/"+obj.confimg+"\" alt=\"image\">\n" +
            "\t\t\t\t\t    <div class=\"media-body\">\n" +
            "\t\t\t\t\t\t    <h3 class=\"title mb-1\"><a href=\"blog-post.html\">"+obj.confname+"</a></h3>\n" +
            "\t\t\t\t\t\t    <div class=\"meta mb-1\"><span class=\"date\">发布于： "+obj.conftime+"</span><span class=\"time\">3 次阅读</span><span class=\"comment\"><a href=\"#\">26 次提交</a></span></div>\n" +
            "\t\t\t\t\t\t    <div class=\"intro\">"+obj.confinf+"</div>\n" +
            "\t\t\t\t\t\t    <a class=\"more-link\" href=\"blog-post.html\">阅读更多 &rarr;</a>\n" +
            "\t\t\t\t\t    </div><!--//media-body-->\n" +
            "\t\t\t\t    </div><!--//media-->\n" +
            "\t\t\t    </div><!--//item-->" );
    })
}
function addnav() {
    $("#text_cont").append("<nav class=\"blog-nav nav nav-justified my-5\">\n" +
        "\t\t\t\t  <a class=\"nav-link-prev nav-item nav-link d-none rounded-left\" href=\"#\">Previous<i class=\"arrow-prev fas fa-long-arrow-alt-left\"></i></a>\n" +
        "\t\t\t\t  <a class=\"nav-link-next nav-item nav-link rounded\" href=\"blog-list.html\">Next<i class=\"arrow-next fas fa-long-arrow-alt-right\"></i></a>\n" +
        "\t\t\t\t</nav>")

}


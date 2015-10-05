本程序已使用py2exe封装，无需python即可运行

程序在.\bin目录下，双击vip.exe即可运行

###ChangeLog
2015-10-5<br>
* 根据PEP8格式化代码

2015-10-5<br>
* 修改yk.py，调用reqs.py发起HTTP请求，增加了两个新UA<br>
####技术信息：
req.py包含函数reqs，其通式为：<br>
`str reqs(url,encode='utf-8')`<br>
调用req.reqs()，可以用get方法请求url，返回值为字符串，即所请求页面的全部HTML内容<br>
示例代码：<br>
<pre>
    import req
    html=req.reqs('https://github.com') \#页面为UTF-8的页面不需要提供编码
    dz=req.reqs('http://discuz.net','gbk') \#当请求Discuz页面时，discuz可能采用GBK编码
</pre>

2015-10-4<br>
* 原迅雷源站已经失效，更新了源站
* 将程序的HTTP请求部分统一封装为reqs.py,加入随机UA功能

2015-9-26<br>
更新爱奇艺VIP算法

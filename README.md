��������ʹ��py2exe��װ������python��������

������.\binĿ¼�£�˫��vip.exe��������

###ChangeLog
2015-10-5<br>
* ����PEP8��ʽ������

2015-10-5<br>
* �޸�yk.py������reqs.py����HTTP����������������UA<br>

####������Ϣ��<br>
req.py��������reqs����ͨʽΪ��<br>
`str reqs(url,encode='utf-8')`<br>
����req.reqs()��������get��������url������ֵΪ�ַ�������������ҳ���ȫ��HTML����<br>
ʾ�����룺<br>
<pre>
    import req
    html=req.reqs('https://github.com') \#ҳ��ΪUTF-8��ҳ�治��Ҫ�ṩ����
    dz=req.reqs('http://discuz.net','gbk') \#������Discuzҳ��ʱ��discuz���ܲ���GBK����
</pre>

2015-10-4<br>
* ԭѸ��Դվ�Ѿ�ʧЧ��������Դվ
* �������HTTP���󲿷�ͳһ��װΪreqs.py,�������UA����

2015-9-26<br>
���°�����VIP�㷨

#-*-encoding:utf8-*-
import re
title=""
with open("./netti.txt", "r") as f:
	data=f.read().replace("คำอธิบายของผู้แปล จบ","</span>").replace("คำอธิบายของผู้แปล","<span style='font-style: italic; font-size: 12;'>")
	index=""
	#gen by one stop page
	result=""
	for l in data.split("\n"):
		z=l.split(" ")
		if re.search("^\+",z[0]) or (re.search("^ ?[0-9]*\.",z[0]) and ( len(l)<70 and ( l[-4:]=="หาระ" or l[-7:]=="สัมปาตะ" or l[-7:]=="วิภังค์" ))) :
			l="<h2>%s</h2>"%l
		result+=l+"</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"	
	with open("./public/netti-single-file.html", "w") as f0:
		f0.write("""<html><head><meta charset="utf-8" /><meta name="description" content="เนตติปกรณ์แปล" /><title>เนตติปกรณ์แปล</title></head>
		<script>
		window.onload = function () {
    var toc = "";
    var level = 0;

    document.getElementById("contents").innerHTML =
        document.getElementById("contents").innerHTML.replace(
            /<h([\d])>([^<]+)<\/h([\d])>/gi,
            function (str, openLevel, titleText, closeLevel) {
                if (openLevel != closeLevel) {
                    return str;
                }

                if (openLevel > level) {
                    toc += (new Array(openLevel - level + 1)).join("<ul>");
                } else if (openLevel < level) {
                    toc += (new Array(level - openLevel + 1)).join("</ul>");
                }

                level = parseInt(openLevel);

                var anchor = titleText.replace(/ /g, "_");
                toc += "<li><a href=\\"#" + anchor + "\\">" + titleText
                    + "</a></li>";

                return "<h" + openLevel + "><a name=\\"" + anchor + "\\">"
                    + titleText + "</a></h" + closeLevel + ">";
            }
        );

    if (level) {
        toc += (new Array(level + 1)).join("</ul>");
    }

    document.getElementById("toc").innerHTML += toc;
};</script>
<body><script type="text/javascript" id="cool_find_script" src="find6.js"></script><style>.highlight{	background-color: blue;}.find_selected{	background-color: green;} a {color: blue;text-decoration: none; /* no underline */}</style><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;" id="contents">สารบัญเนตติ <a href="./title/index.html">ห้วเรื่อง</a>, <a href="./num/index.html">เลขข้อ</a> | <a href="./search.html">ค้นหา</a>, <a href="./netti.txt">text</a></br>
<h2>เนตติปกรณ์แปล </h2>    <div id="toc">
        <h3>สารบัญ</h3>
    </div><hr />%s</td></tr></tbody></table><center><i>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%result)			
	#gen by number
	for l in data.split("\n["):
		try:
			i=int(l.split("]",1)[0])
		except:
			continue
		n="%03d"%i
		if title !="": index+="""<li><a href="./%s.html">ข้อ %s (%s)</a></li>"""%(n,i,title)
		with open("./public/num/%s.html"%n, "w") as f2:
			f2.write("""<html><head><meta charset="utf-8" /><meta name="description" content="ข้อ %s %s ใน เนตติปกรณ์" /><TITLE>ข้อ %s %s ใน เนตติปกรณ์</TITLE></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><center><i>นโม ตัสสะ ภควโต อรหโต สัมมาสัมพุทธัสสะ</i></br>สารบัญ: <a href="../title/index.html">ห้วเรื่อง</a>, <a href="./index.html">เลขข้อ</a> | ไฟล์เดียว: <a href="../netti-single-file.html">html</a>, <a href="../netti.txt">text</a> | <a href="../title/index.html">[ค้นหา]</a> <a href="./index.html">[สารบัญ]</a> <a href="%s.html"><ก่อนนี้]</a> <a href="%s.html">[ถัดไป></a> <h2>เนตติปกรณ์แปล : %s</h2></center>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[%s</td></tr></tbody></table><center><a href="../title/index.html">[ค้นหา]</a> <a href="./index.html">[สารบัญ]</a> <a href="%s.html"><ก่อนนี้]</a> <a href="%s.html">[ถัดไป></a></center></body></html>"""%(n,title, n,title, "%03d"%(i-1), "%03d"%(i+1), title, l.replace("\n", "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"),"%03d"%(i-1),"%03d"%(i+1)))

		z=l.split("\n")[-1].split(" ")
		if re.search("^ ?[0-9]*\.|\+",z[0]):
			title= " ".join(z)
	with open("./public/num/index.html", "w") as f3:
		f3.write("""<html><head><meta charset="utf-8" /><meta name="description" content="สารบัญเลขข้อเนตติปกรณ์แปล" /><title>สารบัญเลขข้อเนตติปกรณ์แปล</title></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;">สารบัญเนตติ <a href="../title/index.html">ห้วเรื่อง</a>, <a href="./index.html">เลขข้อ</a> | เนตติไฟล์เดียว <a href="../netti-single-file.html">html</a>, <a href="../netti.txt">text</a></br><h2>เนตติปกรณ์แปล : สารบัญเลขข้อ</h2><ul>%s</ul></td></tr></tbody></table><center><i> <a href="../title/index.html">[ไปยังสารบัญหัวเรื่อง]</a> | <a href="../netti-single-file.html">หน้าค้นหา</a></br>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(index,))
	#gen by title
	cont=""
	title=""
	ltitle=""
	index=""
	titleChanged=0
	i=0
	for l in data.split("\n["):
		z=l.split("\n")[-1].split(" ")
		cont+="\n["+l
		print (l[0:15])
		if re.search("^ ?[0-9]*\.|^ ?\+",z[0]):
			i+=1
			ltitle=title
			title= " ".join(z).strip("+| ")
			index+="""<li><a href="./%s.html">%s</a></li>"""%(i,ltitle)
			with open("./public/title/%s.html"%i, "w") as f2:
				#print (re.sub("<.*?>|สารบัญ.*?สารบัญ", "", cont)[0:55]+"\n--------\n")
				#ถ้าเป็นหน้าแรก ไม่ต้องไรท์อะไรลงไป
				if i>1:
					f2.write("""%s</td></tr></tbody></table><center><a href="../title/index.html">[ค้นหา]</a> <a href="./index.html">[สารบัญ]</a> <a href="%s.html"><ก่อนนี้]</a> <a href="%s.html">[ถัดไป></a></br>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(cont.replace("\n", "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"),i-1,i+1))
				cont="""<html><head><meta charset="utf-8" /><meta name="description" content="%s ใน เนตติปกรณ์" /><TITLE>%s ใน เนตติปกรณ์</TITLE></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><center><i>นโม ตัสสะ ภควโต อรหโต สัมมาสัมพุทธัสสะ</i></br>สารบัญ: <a href="./index.html">ห้วเรื่อง</a>, <a href="../num/index.html">เลขข้อ</a> | ไฟล์เดียว: <a href="../netti-single-file.html">html</a>, <a href="../netti.txt">text</a> | <a href="../title/index.html">[ค้นหา]</a> <a href="./index.html">[สารบัญ]</a> <a href="%d.html"><ก่อนนี้]</a> <a href="%d.html">[ถัดไป></a> <h2>เนตติปกรณ์แปล : %s</h2></center>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"""%(title, title, i, i+2, title)
				
	with open("./public/title/%s.html"%i, "w") as f2:
		f2.write("""%s</td></tr></tbody></table><center><a href="../title/index.html">[ค้นหา]</a> <a href="./index.html">[สารบัญ]</a> <a href="%s.html"><ก่อนนี้]</a> <a href="%s.html">[ถัดไป></a></br>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(cont.replace("\n", "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"),i-1,i+1))
	with open("./public/title/index.html", "w") as f3:
		f3.write("""<html><head><meta charset="utf-8" /><meta name="description" content="สารบัญเนตติปกรณ์แปล" /><title>สารบัญเนตติปกรณ์แปล</title></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><h2>ค้นเนตติปกรณ์แปล</h2><FORM action="../search.html" method="get"><input type=text id=kw autofocus name=kw > <button>ค้น</button></FORM><hr/>สารบัญเนตติ <a href="./index.html">ห้วเรื่อง</a>, <a href="../num/index.html">เลขข้อ</a> | เนตติไฟล์เดียว <a href="../netti-single-file.html">html</a>, <a href="../netti.txt">text</a></br><h2>เนตติปกรณ์แปล : สารบัญหัวเรื่อง</h2><ul>%s</ul></td></tr></tbody></table><center><i><a href="../num/index.html">[ไปยังสารบัญเลขข้อ]</a> | <a href="../search.html">หน้าค้นหา</a></br>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(index,))

			

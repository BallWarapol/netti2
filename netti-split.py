#-*-encoding:utf8-*-
import re
title=""
with open("./เนตติ.txt", "r") as f:
	data=f.read()
	index=""
	#gen by one stop page
	result=""
	for l in data.split("\n"):
		z=l.split(" ")
		if re.search("^\+",z[0]) or (re.search("^ ?[0-9]*\.",z[0]) and ( len(l)<70 and ( l[-12:]=="วาระ" or l[-21:]=="สัมปาตะ" or l[-21:]=="วิภังค์" ))) :
			l="<h2>%s</h2>"%l
		result+=l+"</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"	
	with open("./docs/เนตติปกรณ์(จบ).html", "w") as f0:
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
<body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;" id="contents"><h2>เนตติปกรณ์แปล </h2>    <div id="toc">
        <h3>สารบัญ</h3>
    </div><hr />%s</td></tr></tbody></table><center><i> <a href="../num/index.html">[ไปยังสารบัญหัวเรื่อง]</a>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%result)			
	#gen by number
	for l in data.split("\n["):
		try:
			i=int(l.split("]",1)[0])
		except:
			continue
		n="%03d"%i
		if title !="": index+="""<li><a href="./ข้อ%s.html">ข้อ %s (%s)</a></li>"""%(n,i,title)
		with open("./docs/num/ข้อ%s.html"%n, "w") as f2:
			f2.write("""<html><head><meta charset="utf-8" /><meta name="description" content="เนตติ-ข้อ %s (%s)" /></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><h2>เนตติปกรณ์แปล ข้อ  %s (%s)</h2><CENTER><i><a href="./index.html">[สารบัญ]</a></i></CENTER>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[%s</td></tr></tbody></table><center><i><a href="./index.html">[สารบัญ]</a> (ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(n,title, n,title,l.replace("\n", "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")))
		z=l.split("\n")[-1].split(" ")
		if re.search("^ ?[0-9]*\.|\+",z[0]):
			title= " ".join(z)
	with open("./docs/num/index.html", "w") as f3:
		f3.write("""<html><head><meta charset="utf-8" /><meta name="description" content="สารบัญเลขข้อเนตติปกรณ์แปล" /><title>สารบัญเลขข้อเนตติปกรณ์แปล</title></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><h2>เนตติปกรณ์แปล : สารบัญเลขข้อ</h2><ul>%s</ul></td></tr></tbody></table><center><i> <a href="../title/index.html">[ไปยังสารบัญหัวเรื่อง]</a>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(index,))
	#gen by title
	cont=""
	title=""
	ltitle=""
	index=""
	for l in data.split("\n["):
		z=l.split("\n")[-1].split(" ")
		cont+="\n["+l
		if re.search("^ ?[0-9]*\.|\+",z[0]):
			ltitle=title
			title= " ".join(z)
			index+="""<li><a href="./เนตติ-%s.html">%s</a></li>"""%(title,title)
			with open("./docs/title/เนตติ-%s.html"%ltitle, "w") as f2:
				f2.write("%s</td></tr></tbody></table><center><i>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"%(cont.replace("\n", "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")))
				cont="""<html><head><meta charset="utf-8" /><meta name="description" content="เนตติ-%s" /></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><h2>เนตติปกรณ์แปล : %s</h2><CENTER><i><a href="./index.html">[สารบัญ]</a></i></CENTER>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"""%(title, title)
	with open("./docs/title/เนตติ-%s.html"%ltitle, "w") as f2:
		f2.write("""%s</td></tr></tbody></table><center><i><a href="./index.html">[สารบัญ]</a> (ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(cont.replace("\n", "</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")))
	with open("./docs/title/index.html", "w") as f3:
		f3.write("""<html><head><meta charset="utf-8" /><meta name="description" content="สารบัญเนตติปกรณ์แปล" /><title>สารบัญเนตติปกรณ์แปล</title></head><body><table style="width: 609px; margin-left: auto; margin-right: auto; "><tbody><tr ><td style="width: 608px; text-align: justify;"><h2>เนตติปกรณ์แปล : สารบัญหัวเรื่อง</h2><ul>%s</ul></td></tr></tbody></table><center><i><a href="../num/index.html">[ไปยังสารบัญเลขข้อ]</a>(ไม่สงวนลิขสิทธิ์)</i></center></body></html>"""%(index,))
			

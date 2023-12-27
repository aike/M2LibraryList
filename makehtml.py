import os
import glob
import datetime

dir1 = "F:/dtm/NI/Maschine 2 Factory Selection/"
dir2 = "F:/dtm/NI/Maschine 2 Factory Library/"

def dirdiff(dir1, dir2):

  file1 = glob.glob(dir1 + '**/*', recursive=True)
  file2 = glob.glob(dir2 + '**/*', recursive=True)

  file1_noroot = sorted(list(map(lambda x: x.replace('\\','/').replace(dir1, ""), file1)), key=str.casefold)
  file2_noroot = sorted(list(map(lambda x: x.replace('\\','/').replace(dir2, ""), file2)), key=str.casefold)

  # "Bass Synth"フォルダと "Bass"フォルダの子要素を正しくソートできないので、末尾にスラッシュを追加
  file3 = list(set(file1_noroot + file2_noroot))
  for i in range(len(file3)):
    if (os.path.isdir(dir1 + file3[i])) or (os.path.isdir(dir2 + file3[i])):
      file3[i] = file3[i] + "/"

  file_all = sorted(file3, key=str.casefold)

  dirno = 0
  dirs = {}
  cnt_sel = 0
  cnt_ful = 0

  for f in file_all:
    if f.startswith("Documentation"):
      continue

    clsstr = ""
    isdir = False
    if (os.path.isdir(dir1 + f) or os.path.isdir(dir2 + f)):
      f = f[:-1]
      isdir = True
      dirno += 1
      clsstr = "p" + str(dirno)
      dirs[f] = dirno

    fname = os.path.basename(f)
    d = os.path.dirname(f)
    l = 0
    while (d != ""):
      l += 1
      if clsstr != "":
        clsstr = clsstr + " "
      clsstr = clsstr + "c" + str(dirs[d])
      d = os.path.dirname(d)
    clsstr = clsstr + " l" + str(l)
    if (os.path.dirname(f) != ""):
      clsstr = clsstr + " h"

    if isdir:
      clsstr = clsstr + " d"
 
    print('<tr class="' + clsstr + '"><td>', end='')
    if f in file1_noroot:
      print(fname, end='')
    print("</td><td>", end='')
    if f in file2_noroot:
      print(fname, end='')
    print("</td></tr>")

    if not isdir:
      if f in file1_noroot:
        cnt_sel += 1
      if f in file2_noroot:
        cnt_ful += 1

  return cnt_sel, cnt_ful

print("<html>")
print("<head>")
print("<title>Maschine 2 Factory Selection vs Full Factory Library</title>")
print("<link rel=Stylesheet href=style.css>")
print("</head>")
print("<body>")
print('<div id="title"><h1>Maschine 2 Factory Selection vs Full Factory Library</h1></div>')
print('<div id="control"><div id="collapse">Collapse All</div><div id="expand">Expand All</div>')
print('<input type="search" id="search" placeholder="Search..."></div>')
print("<table>")
print("<tr>")
print('<th>Factory Selection<span id="cnt_selection">(0000 items)</span></th>')
print('<th >Full Factory Library<span id="cnt_full">(00000 items)</span></th>')
print("</tr>")

cnt_sel, cnt_ful = dirdiff(dir1, dir2)

print("</table>")
print('<div id="update">{} update</div>'.format(str(datetime.datetime.today().date())))
print('<div id="about"><a href="https://github.com/aike/M2LibraryList">about</a></div>')
print('<div id="cnt_selection_value" value="{}" style="display:none"/>'.format(cnt_sel))
print('<div id="cnt_full_value" value="{}" style="display:none"/>'.format(cnt_ful))
print('<script src="script.js"></script>')
print("</body>")
print("</html>")

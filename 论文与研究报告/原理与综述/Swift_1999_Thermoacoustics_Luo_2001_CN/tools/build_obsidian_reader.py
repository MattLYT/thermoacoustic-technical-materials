"""Build an Obsidian reading layer from the preserved MinerU transcription."""
from pathlib import Path
import hashlib
import json
import re
from bs4 import BeautifulSoup
from PIL import Image
import yaml

PACKAGE = Path(__file__).resolve().parents[1]
VAULT = PACKAGE.parents[3]
STEM = '热声学_统一方法_Swift著_罗二仓译'
SOURCE = PACKAGE/'parsed'/(STEM+'_MinerU全文.md')
OUT = PACKAGE/'阅读版'
ENTRY = PACKAGE/(STEM+'.md')
digest = lambda value: hashlib.sha256(value).hexdigest()
raw = SOURCE.read_text(encoding='utf-8')
source_hash = digest(SOURCE.read_bytes())
assert source_hash == '9e9f19f3eb327a5230e8a59ded62e7face2c695883fb80fb7a242c74e77d3a01'
body = raw.split('\n---\n',1)[1].lstrip()
matches = list(re.finditer(r'^## 第[一二三四五六七]章 .+$',body,re.M))
assert len(matches)==7
appendix = body.index('\n## 附录\n')+1
preface = body.index('## 序 言')
sections = [('Swift热声学_00_前言与符号','前言与符号',body[preface:matches[0].start()],1,12)]
pages=[13,43,80,105,122,178,203,233]
titles=['绪论','声波','功率','效率','超出Rott热声学的问题','硬件','测量']
for i,m in enumerate(matches):
    end=matches[i+1].start() if i<6 else appendix
    sections.append((f'Swift热声学_{i+1:02d}_{titles[i]}',f'第{i+1}章 {titles[i]}',body[m.end():end],pages[i],pages[i+1]-1))
sections.append(('Swift热声学_08_附录索引与文献','附录、索引与参考文献',body[appendix+len('## 附录'):],233,254))
OUT.mkdir(exist_ok=True)
report={'input_sha256':source_hash,'input_path':str(SOURCE.relative_to(PACKAGE)),
        'generated_files':[],'html_tables_converted':0,'image_embeds':0,
        'transformations':['分章和相邻章导航','重建标题层级和节目录','本地图片使用Obsidian嵌入并限制宽度',
                           '无合并单元格的HTML表格转Markdown；首行保留为数据行',
                           '原封面和目录由入口及章节导航替代；原始解析稿保持不变'],
        'scientific_content':'保留原始公式、段落和数字；未经英文底本逐式校对',
        'math_repairs':[]}

def table_to_md(match):
    soup=BeautifulSoup(match.group(0),'html.parser')
    assert not soup.select('[rowspan], [colspan]')
    rows=[]
    for row in soup.select('tr'):
        cells=[]
        for cell in row.find_all(['td','th'],recursive=False):
            cell=''.join(str(c) for c in cell.contents).strip().replace('|','&#124;').replace('\n',' ')
            cells.append(cell)
        rows.append(cells)
    width=max(map(len,rows))
    # A neutral header keeps the original first row in the body of the table.
    result=['| '+' | '.join(f'列{i+1}' for i in range(width))+' |',
            '| '+' | '.join('---' for _ in range(width))+' |']
    result += ['| '+' | '.join(row+['']*(width-len(row)))+' |' for row in rows]
    report['html_tables_converted']+=1
    return '\n'+'\n'.join(result)+'\n'

for index,(name,title,text,start,end) in enumerate(sections):
    text=re.sub(r'<table>.*?</table>',table_to_md,text,flags=re.S)
    def image(match):
        target=PACKAGE/'images'/Path(match.group(1)).name
        assert target.is_file(),target
        report['image_embeds']+=1
        with Image.open(target) as img:
            width=min(640,img.width)
        return '![[%s|%d]]'%(target.name,width)
    text=re.sub(r'!\[[^\]]*\]\((\.\./images/[^)]+)\)',image,text)
    lines=[]
    toc=[]
    math=False
    for line in text.splitlines():
        if line.strip()=='$$': math=not math
        if not math and (heading:=re.match(r'^#{1,6}\s+(.+)',line)):
            label=heading[1].strip()
            if re.match(r'^\d+\.\d+(?:\s*\.\s*|\s+)\d+',label): level=3
            elif re.match(r'^\d+\.\d+',label): level=2
            elif label.startswith('例子：'): level=4
            elif index==8 and re.fullmatch('[A-Z]',label):level=3
            else: level=2
            # Unique explicit block IDs avoid ambiguity from repeated example headings.
            anchor=f'sec-{len(toc)+1:02d}'
            toc.append((level,label,anchor))
            lines += ['#'*level+' '+label,'',f'^{anchor}']
        else: lines.append(line.rstrip())
    assert not math,'Unbalanced display-math delimiters'
    metadata={'title':title+' · Swift热声学中文译本','record_role':'machine-transcription'}
    nav=[f'[[{STEM}|教程入口]]']
    if index: nav.append(f'[[{sections[index-1][0]}|上一部分]]')
    if index+1<len(sections):nav.append(f'[[{sections[index+1][0]}|下一部分]]')
    head='---\n'+yaml.safe_dump(metadata,allow_unicode=True,sort_keys=False)+'---\n\n# '+title+'\n\n'+' · '.join(nav)+'\n\n'
    head+=f'> [!info] 来源与核对\n> [[热声学-中文版(1).pdf#page={start}|原 PDF 第 {start}–{end} 页]]。本稿整理阅读结构；公式及数字仍需核对原页。\n\n'
    if index==0:head+='封面与原始目录见 PDF 第 1–4 页；本阅读版以分章导航替代原目录。\n\n'
    head+='> [!contents]- 本部分目录\n'+'\n'.join(f'> {"  "*(level-2)}- [[#^{anchor}|{label.replace("|","¦")}]]' for level,label,anchor in toc)+'\n\n'
    output=head+'\n'.join(lines).strip()+'\n\n---\n\n'+' · '.join(nav)+'\n'
    target=OUT/(name+'.md')
    target.write_text(output,encoding='utf-8',newline='\n')
    report['generated_files'].append({'path':str(target.relative_to(PACKAGE)).replace('\\','/'),
                                    'sha256':digest(target.read_bytes()),'sections':len(toc)})
    # All display formulas must be byte-for-byte equivalent after line-end trimming.
    formula=lambda s:re.findall(r'\$\$\s*\n(.*?)\n\$\$',s,re.S)
    assert [f.strip() for f in formula(text)]==[f.strip() for f in formula(output)]

entry=ENTRY.read_text(encoding='utf-8')
start_marker='<!-- obsidian-reader-start -->'
end_marker='<!-- obsidian-reader-end -->'
block=start_marker+'\n\n## Obsidian 分章阅读\n\n原始解析稿保留在 `parsed/`；以下阅读稿重建标题层级、节目录、图片尺寸及表格格式，便于在 Obsidian 中阅读。\n\n'
block+='\n'.join(f'- [[{name}|{title}]]' for name,title,*_ in sections)
block+='\n\n'+end_marker+'\n\n'
if start_marker in entry:
    entry=re.sub(re.escape(start_marker)+r'.*?'+re.escape(end_marker)+r'\n*',block,entry,flags=re.S)
else:entry=entry.replace('## 来源与版本',block+'## 来源与版本',1)
ENTRY.write_text(entry,encoding='utf-8',newline='\n')
assert digest(SOURCE.read_bytes())==source_hash
(PACKAGE/'parsed/Obsidian阅读版校验记录.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'chapters':len(sections),'images':report['image_embeds'],'tables':report['html_tables_converted'],'raw_unchanged':True},ensure_ascii=False))

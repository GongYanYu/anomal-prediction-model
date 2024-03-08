import os
from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

need_bold_list='月主题、次主题、时间、设计意图、活动目标、活动准备、活动过程、活动延伸、活动反思'.split('、')

def run_modify_word(file_path,font_name='宋体'):
    try:
        doc = Document(file_path)
    except:
        print('run except file_path'+file_path)
        return
    for para in doc.paragraphs:

        para.paragraph_format.line_spacing  = 1.25

        need_bold=False
        for item in need_bold_list:
            if item in para.text:
                need_bold=True
                break

        # 指定段落
        para.paragraph_format.first_line_indent  = Pt(0 if need_bold else 2*12)


        for run in para.runs:
            # # 字体加粗
            run.font.bold = need_bold
            # # 字体设置为斜体
            # run.font.italic = True
            # # 字体下划线
            # run.font.underline = True
            # # 设置划线
            # # run.font.strike = True
            # # 设置字体大小未24号字体
            run.font.size = Pt(12)
            # # 设置字体颜色
            # run.font.color.rgb = RGBColor(255, 0, 0)
            run.font.name = font_name
            r = run._element.rPr.rFonts
            r.set(qn('w:eastAsia'), font_name)

    doc.save(file_path)

def main():
    file_dir_path = 'D:\\Documents\\WorkDocument\\test\\教案'
    count=0
    for base_path, folder_list, file_list in os.walk(file_dir_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for file_path in file_list:
            count+=1
            file_path_temp=base_path+'\\'+file_path
            print('index={},file_path={}'.format(count,file_path_temp))
            run_modify_word(file_path_temp)


if __name__ == "__main__":
    main()

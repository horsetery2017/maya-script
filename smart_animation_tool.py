#coding:utf-8
###############################
#author:horsetery chen
#horsetery@gmail.com
#20060101
#此程序通过文本序列生成动画
#word 为动画文本序列
#prefix 为物体 
#attribute 为物体需要动画的属性
#遵循以下规则：
# - 为延时设置
# * 为属性归零设置
###############################

import maya.cmds as cmds
class smart_ani:
    def __init__(self):
        self.post=""
        self.t=0        
        self.pre=""
        self.word=""
        self.dict=[]                    

    def create_ui(self):
        self.window = cmds.window(title="自动动画工具")
        cmds.columnLayout()
        cmds.text( label='【自动动画工具】\n本工具可以依据文本序列自动生成动画\n使用方法：\n在prefix填入动画物体名称\n在attribute中填入需要动画的属性\n在word中填入动画属性的名称')
        cmds.text( label='word' )
        self.word_ = cmds.textField(w=800)
    
        cmds.text( label='prefix')
        self.prefix = cmds.textField(w=800)
    
        cmds.text( label='attribute' )
        self.attribute = cmds.textField(w=800)
    
        cmds.rowColumnLayout(numberOfColumns=2)
        self.clear_bt=cmds.button( label='clear')
        self.create_bt=cmds.button( label='create')
        
        cmds.button(self.clear_bt,edit=True,command=self.clear_ani)
        cmds.button(self.create_bt,edit=True,command=self.main)        
        

        cmds.showWindow(window)
 
    def set_ani(self):
        for i in self.dict:
            if self.post==i:
                cmds.setKeyframe(self.pre+"."+self.post,t=self.t*5,v=1)
            else:
                cmds.setKeyframe(self.pre+"."+i,t=self.t*5,v=0)        
        
    def clear_ani(self,s):
        self.get_info()
        for i in self.dict:
            cmds.cutKey(self.pre+"."+i)
            
    def get_info(self):    
        self.pre=cmds.textField(self.prefix,query=True,tx=True)
        self.word=cmds.textField(self.word_,query=True,tx=True)
        dict_=cmds.textField(self.attribute,query=True,tx=True)  
              
        for i in dict_.split(','):
            self.dict.append(i)         
        
    def main(self,s):
        self.get_info()
        for i in self.word.split(','):
            for j in self.dict:
                if i==j:
                    self.post=i
                    
                if i=='-':
                    self.t=self.t+1
                if i=='*':
                    self.post='*'
        
                self.set_ani()   
            self.t=self.t+1
                   
t=smart_ani()
t.create_ui()      
        
   



            
    

    




from abotcommon import send
from qqbot.utf8logger import DEBUG
import re
import subprocess

def toolProcess(context):
    txt = context.content.replace('[@ME]','')
    cmd = getToolCMD(txt)
    if cmd == None:
        send(context,'解析错误，请以【@QQBot tool cmd】或者【@QQBot 工具 命令】格式发送。发送【@QQBot tool help】查询所有命令')
        return
    for helper in cmdHelpers:
        if any(k in cmd for k in [helper.cmd,helper.cmdCN]):
            helper.method(context,cmd)
            return
    if any(k in cmd for k in ['help','帮助']):
        cmdHelp(context)
    else:
        send(context,'未知命令，发送【@QQBot tool help】查询所有命令')

class CmdHelper:
    def __init__(self, method, cmd, cmdCN, desc, etc):
        self.method = method
        self.cmd = cmd
        self.cmdCN = cmdCN
        self.desc = desc
        self.etc = etc
     
def cmdIsInvalid(cmd):
    #TODO 也许有更好的处理办法
    return any(k in cmd for k in ['&','\\','>','<'])

def getToolCMD(txt):
    m = re.match(r"^\s*[tool|工具]+\s*(\S.*)$",txt)
    if m != None:
        return m[1]
    return None

def cmdHelp(context):
    str = "以下是目前所有的命令：\n\n"
    for help in cmdHelpers:
        str += "┌─[{0}] {1}\n".format(help.cmd,help.desc)
        str += "├─中文指令：{0}\n".format(help.cmdCN)
        str += "└─使用方法：{0}\n".format(help.etc)
    send(context,str)

def cmdNslookup(context,cmd):
    help = cmdHelpers[0]
    p = re.compile("^\s*[{0}|{1}]+\s*(\S.*)$".format(help.cmd,help.cmdCN))
    m = p.match(cmd)
    if cmdIsInvalid(cmd):
        send(context,"包含非法字符")
        return
    if m == None or len(m[1]) <= 1: #不要问我这里为什么会等于1，鬼知道
        send(context,'参数错误。{0}'.format(help.etc))
    else:
        send(context,subprocess.getoutput(help.cmd + ' ' + m[1]))

# 注册工具集
cmdHelpers = [
    CmdHelper(cmdNslookup,'nslookup','解析域名','返回指定域名的DNS解析结果','直接解析：nslookup z.cn，指定dns解析：nslookup z.cn 8.8.8.8')
]
from qqbot.utf8logger import DEBUG
from qqbot import qqbotsched
from random import choice
from abotcommon import Context,send
from abotcmd import toolProcess
import re
import datetime

def onStartupComplete(bot):
    glist = bot.List('group', ':like:Android')
    for g in glist:
        bot.SendTo(g,'QQBot被神秘力量复活，复活时间：%s' % (datetime.datetime.now().strftime("%y/%m/%d %H:%M")))

def onQQMessage(bot, contact, member, content):
    context = Context(bot, contact, member, content)
    # 当收到 QQ 消息时被调用
    # bot     : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    # contact : QContact 对象，消息的发送者
    # member  : QContact 对象，仅当本消息为 群或讨论组 消息时有效，代表实际发消息的成员
    # content : str 对象，消息内容
    if bot.isMe(contact, member) == False:
        CONTENT = content.upper()
        if contact.ctype == 'group':
            if '下载' in content :
                downloadLink(context)
            elif any(k in CONTENT for k in ['文档','API','DOCUMENT']):
                documentLink(context)
            elif any(k in CONTENT for k in ['教程','基础','学习','GUIDE','指南']):
                learnLink(context)
        if '@ME' in content:
            if any(k in CONTENT for k in ['TOOL','工具']):
                toolProcess(context)
            else:
                stupidStr = choice(LongText.aStupidGuyAtMe)
                if '%' in stupidStr:
                    stupidStr = stupidStr % member.name
                send(context,  stupidStr)

def downloadLink(context):
    CONTENT = context.content.upper()
    if any(k in CONTENT for k in ['AS','ANDROID STUDIO']):
        send(context, 'Android Studio官方下载地址：https://developer.android.google.cn/studio/')
    elif 'GRADLE' in CONTENT:
        send(context, 'Gradle下载地址：https://gradle.org/install/')
    elif 'JDK10' in CONTENT:
        send(context, 'JDK-10下载地址：https://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html')
    elif 'JDK8' in CONTENT:
        send(context, 'JDK-8下载地址：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html')
    elif any(k in CONTENT for k in ['JAVA','JDK']):
        send(context, 'JDK下载地址：https://www.oracle.com/technetwork/java/javase/downloads/index.html')

def documentLink(context):
    CONTENT = context.content.upper()
    if any(k in CONTENT for k in ['JAVA','JDK']) and '7' not in CONTENT:
        send(context, '这有一份OpenJDK 8的文档链接，请保存书签：https://docs.oracle.com/javase/8/docs/api/。如果想要jdk7的文档请回复“请皇上赐我一份JDK7的文档”。')
    elif 'JDK7' in CONTENT:
        send(context, '这有一份OpenJDK 7的文档链接，请保存书签：https://docs.oracle.com/javase/7/docs/api/')
    elif any(k in CONTENT for k in ['ANDROID','安卓']) and 'STUDIO' not in CONTENT:
        send(context, '这里有一份Android的文档链接，请保存书签：https://developer.android.google.cn/reference/')
    elif any(k in CONTENT for k in ['ANDROID STUDIO','AS','安卓死丢丢']):
        send(context, '这里有一份Android Studio的文档链接，请保存书签：https://developer.android.google.cn/studio/intro/')
    elif 'OKHTTP' in CONTENT:
        send(context, '这里有一份OKHttp的文档链接，请保存书签：http://square.github.io/okhttp/')
    elif 'RETROFIT' in CONTENT:
        send(context, '这里有一份Retrofit的文档链接，请保存书签：http://square.github.io/retrofit/')

def learnLink(context):
    CONTENT = context.content.upper()
    if 'JAVA' in CONTENT:
        send(context,LongText.learnJava)
    elif any(k in CONTENT for k in ['ANDROID','安卓']):
        send(context,LongText.learnAndroid)

@qqbotsched(hour='07', minute='00', day_of_week='mon-fri')
def morningTask(bot):
    glist = bot.List('group', ':like:Android')
    for g in glist:
        bot.SendTo(g,'睡你麻痹起床了，赶紧去给资本家打工。')

@qqbotsched(hour='23', minute='00', day_of_week='mon-fri')
def nightTask(bot):
    glist = bot.List('group', ':like:Android')
    for g in glist:
        bot.SendTo(g,'各位大佬，赶紧睡觉了，都他妈十一点了。像你们这种穷逼，只有身体才是资本。')

@qqbotsched(hour='7-21/1')
def updateGroup(bot):
    glist = bot.list('group',':like:Android')
    for g in glist:
        bot.Update(g)



class LongText:
    learnJava = """
书籍推荐（*为深入/高级）：
1. 《第一行代码：Java》-- https://www.amazon.cn/dp/B071YD54L8
2. 《Java疯狂讲义》-- https://www.amazon.cn/dp/B078XY2JMH
3. 《*Java编程思想/Thinking in Java》-- https://www.amazon.cn/dp/B0011F7WU4
4. 《*深入理解Java虚拟机》-- https://www.amazon.cn/dp/B00D2ID4PK

入门网站推荐：
1. http://www.runoob.com/java/java-tutorial.html
2. https://www.w3cschool.cn/java/
3. http://www.weixueyuan.net/java/rumen/
欢迎在 https://github.com/zedcn-com/android-qqbot-plugin 通过PR或者issue提交你的推荐。 
"""

    learnAndroid = """
========================
官方入门教程：https://developer.android.google.cn/guide/
========================
书籍推荐（*为深入/高级）：
1. 《第一行代码：Android》-- https://www.amazon.cn/dp/B01MSR5D04
2. 《Android从入门到精通（再到转行）》-- https://www.amazon.cn/dp/B00NHCI0RI
入门网站推荐：
1. http://www.runoob.com/w3cnote/android-tutorial-intro.html
2. https://www.w3cschool.cn/android/
欢迎在 https://github.com/zedcn-com/android-qqbot-plugin 通过PR或者issue提交你的推荐。 
"""
    aStupidGuyAtMe = [
        "%s，what are you 弄啥lei。",
        "Surprise montherf**ker. %s",
        "%s的鸡鸡飞啦！",
        "%s满♂身♂大♂汉",
        "%s，你好骚啊！",
        "%s，你食💩真骚！",
        "都听我说一句，我爱中国共产党，好了你们继续。",
        "一根指向ZZ的指针 ==> %s"
    ]
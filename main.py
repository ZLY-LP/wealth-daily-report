import feedparser
from datetime import datetime
from deep_translator import GoogleTranslator


def translate_text(text):
    try:
        return GoogleTranslator(
            source="auto",
            target="zh-CN"
        ).translate(text)
    except:
        return text



def format_time(item):

    if hasattr(item, "published"):
        return item.published

    elif hasattr(item, "updated"):
        return item.updated

    else:
        return "时间未知"



def get_news(section, source, url, count=5):

    print("\n")
    print("=" * 45)
    print(section)
    print("=" * 45)

    print("新闻来源：" + source)

    try:

        feed = feedparser.parse(url)

        if not feed.entries:

            print("暂无最新资讯")
            return []

        result=[]


        for item in feed.entries[:count]:

            title = translate_text(
                item.title
            )

            time = format_time(item)

            print("\n【发布时间】")
            print(time)

            print("【新闻】")
            print(title)


            result.append(title)


        return result


    except Exception as e:

        print("读取失败:", e)

        return []



today=datetime.now().strftime("%Y-%m-%d")


print("财富日报")
print("日期："+today)



all_news=[]



# ============================
# 全球经济
# ============================

news=get_news(
    "🌏 全球经济雷达",
    "BBC Business",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    5
)

all_news.extend(news)



# ============================
# AI科技
# ============================


news=get_news(
    "🤖 AI科技前沿",
    "Google AI Blog",
    "https://blog.google/technology/ai/rss/",
    5
)

all_news.extend(news)



# ============================
# 科技趋势
# ============================


news=get_news(
    "🚀 科技产业趋势",
    "MIT Technology Review",
    "https://www.technologyreview.com/feed/",
    5
)

all_news.extend(news)



# ============================
# 中国经济观察
# ============================


print("\n")
print("="*45)
print("🇨🇳 中国经济观察")
print("="*45)


print("""
新闻来源：
中国政府公开信息

重点关注：

- 宏观经济政策
- 产业升级
- 科技创新
- 制造业发展
- 消费趋势

说明：
中国权威RSS数据将在后续版本接入。
""")



# ============================
# 商业机会
# ============================


print("\n")
print("="*45)
print("💼 商业机会观察")
print("="*45)



opportunities=[]


rules={

"AI":
"人工智能应用、企业自动化、智能软件服务",

"人工智能":
"AI应用生态、企业数字化服务",

"能源":
"新能源产业链、能源管理技术",

"电":
"能源基础设施升级",

"医疗":
"AI医疗、生命科学技术",

"机器人":
"机器人应用和智能制造"


}



for key,value in rules.items():

    for n in all_news:

        if key in n:

            opportunities.append(value)

            break



if opportunities:

    for i,o in enumerate(set(opportunities),1):

        print(
            str(i)+"."+o
        )

else:

    print("""
今日重点关注：

1. 技术创新带来的产业变化

2. 企业效率提升机会

3. 新兴行业长期趋势
""")



# ============================
# 财富思维
# ============================


print("\n")
print("="*45)
print("📚 财富思维")
print("="*45)


thoughts=[

"真正的财富来自理解趋势，而不是追逐热点。",

"优秀投资者研究产业变化，而不是预测每天涨跌。",

"长期机会往往隐藏在技术进步和社会变化中。",

"提高认知，是普通人最值得投资的资产。",

"信息很多，关键是找到影响未来的变化。"

]


print(
    thoughts[
        datetime.now().day % len(thoughts)
    ]
)



print("\n")
print("="*45)
print("本日报由财富日报自动系统生成")
print("="*45)

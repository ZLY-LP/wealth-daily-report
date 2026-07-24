import feedparser
from datetime import datetime, timezone, timedelta
from deep_translator import GoogleTranslator


# ===============================
# 翻译
# ===============================

def translate_text(text):
    try:
        return GoogleTranslator(
            source="auto",
            target="zh-CN"
        ).translate(text)
    except:
        return text



# ===============================
# 判断国家/地区
# ===============================

def detect_country(text):

    text = text.lower()

    if any(k in text for k in [
        "china",
        "中国",
        "人民币",
        "国务院",
        "beijing"
    ]):
        return "🇨🇳 中国"


    if any(k in text for k in [
        "us",
        "america",
        "美国",
        "federal reserve",
        "美元",
        "washington"
    ]):
        return "🇺🇸 美国"


    if any(k in text for k in [
        "uk",
        "britain",
        "英国",
        "london"
    ]):
        return "🇬🇧 英国"


    if any(k in text for k in [
        "japan",
        "日本",
        "东京"
    ]):
        return "🇯🇵 日本"


    if any(k in text for k in [
        "europe",
        "欧盟",
        "euro"
    ]):
        return "🇪🇺 欧洲"


    if any(k in text for k in [
        "google",
        "openai",
        "microsoft",
        "gemini",
        "ai"
    ]):
        return "🇺🇸 美国科技"


    return "🌐 国际"



# ===============================
# 时间转换北京时间
# ===============================

def get_beijing_time(item):

    try:

        if hasattr(item, "published_parsed"):

            utc_time = datetime(
                *item.published_parsed[:6],
                tzinfo=timezone.utc
            )

            bj_time = utc_time + timedelta(hours=8)

            return bj_time.strftime(
                "%Y-%m-%d %H:%M"
            )


        return "时间未知"


    except:

        return "时间未知"




# ===============================
# 新闻读取
# ===============================

def get_news(section, source, url, count=5):


    print("\n")
    print("="*45)
    print(section)
    print("="*45)


    print("新闻来源：", source)


    news_list=[]


    try:

        feed=feedparser.parse(url)


        if not feed.entries:

            print("暂无最新资讯")
            return []


        for index,item in enumerate(
            feed.entries[:count],
            1
        ):


            original=item.title


            chinese=translate_text(
                original
            )


            country=detect_country(
                original+" "+chinese
            )


            time=get_beijing_time(item)


            print("\n【"+str(index)+"】")

            print("国家/地区：")
            print(country)


            print("发布时间：")
            print(time)


            print("新闻：")
            print(chinese)


            news_list.append(chinese)



        return news_list



    except Exception as e:

        print(
            "读取失败:",
            e
        )

        return []





today=datetime.now().strftime(
    "%Y-%m-%d"
)


print("财富日报")

print("日期："+today)




all_news=[]



# ===============================
# 全球经济
# ===============================


news=get_news(

    "🌏 全球经济雷达",

    "BBC Business",

    "https://feeds.bbci.co.uk/news/business/rss.xml",

    5
)


all_news.extend(news)




# ===============================
# AI科技
# ===============================


news=get_news(

    "🤖 AI科技前沿",

    "Google AI Blog",

    "https://blog.google/technology/ai/rss/",

    5
)


all_news.extend(news)




# ===============================
# 科技趋势
# ===============================


news=get_news(

    "🚀 科技产业趋势",

    "MIT Technology Review",

    "https://www.technologyreview.com/feed/",

    5
)


all_news.extend(news)




# ===============================
# 中国经济观察
# ===============================


print("\n")
print("="*45)
print("🇨🇳 中国经济观察")
print("="*45)


china_news=get_news(

    "中国政策信息",

    "中国政府网",

    "https://www.gov.cn/rss/zhengce.xml",

    5

)


all_news.extend(china_news)




# ===============================
# 商业机会
# ===============================


print("\n")
print("="*45)

print("💼 商业机会观察")

print("="*45)



rules={


"人工智能":
"AI应用、企业自动化、智能软件服务",


"AI":
"人工智能产业链、企业数字化机会",


"能源":
"新能源、能源管理、基础设施升级",


"机器人":
"智能制造、工业自动化方向",


"医疗":
"AI医疗、生物科技方向"



}



found=set()



for key,value in rules.items():

    for news in all_news:

        if key.lower() in news.lower():

            found.add(value)



if found:

    for i,item in enumerate(found,1):

        print(
            str(i)+". "+item
        )


else:

    print(
        "今日关注：产业升级、技术创新、数字化趋势。"
    )




# ===============================
# 财富思维
# ===============================


print("\n")
print("="*45)

print("📚 财富思维")

print("="*45)



thoughts=[

"趋势变化创造机会，认知提升创造财富。",

"不要只关注价格变化，更要理解价值变化。",

"长期财富来自持续学习和正确判断。",

"真正的优势来自比别人更早看见变化。",

"信息只是资源，理解信息才是能力。"

]


print(
    thoughts[
        datetime.now().day % len(thoughts)
    ]
)



print("\n")
print("="*45)

print(
    "本日报由财富日报自动系统生成"
)

print("="*45)

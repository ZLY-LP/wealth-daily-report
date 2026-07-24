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
# 新闻价值过滤
# ===============================

def useful_news(title):

    keywords = [

        "market",
        "economy",
        "economic",
        "business",
        "trade",
        "oil",
        "energy",
        "bank",
        "rate",
        "inflation",
        "AI",
        "artificial",
        "technology",
        "chip",
        "cloud",
        "robot",
        "policy",
        "industry",
        "company",
        "investment",
        "finance"

    ]


    text = title.lower()


    for k in keywords:

        if k.lower() in text:

            return True


    return False




# ===============================
# 国家判断
# ===============================

def detect_country(text):

    t=text.lower()


    if any(x in t for x in [
        "china",
        "中国",
        "beijing",
        "人民币"
    ]):
        return "🇨🇳 中国"


    if any(x in t for x in [
        "us",
        "america",
        "美国",
        "google",
        "openai",
        "nasa"
    ]):
        return "🇺🇸 美国"


    if any(x in t for x in [
        "uk",
        "britain",
        "英国",
        "london"
    ]):
        return "🇬🇧 英国"


    if any(x in t for x in [
        "japan",
        "日本"
    ]):
        return "🇯🇵 日本"


    if any(x in t for x in [
        "europe",
        "eu",
        "欧洲"
    ]):
        return "🇪🇺 欧洲"


    return "🌐 国际"





# ===============================
# 北京时间
# ===============================

def get_time(item):

    try:

        utc=datetime(
            *item.published_parsed[:6],
            tzinfo=timezone.utc
        )

        bj=utc+timedelta(hours=8)


        return bj.strftime(
            "%Y-%m-%d %H:%M"
        )

    except:

        return "时间未知"





# ===============================
# 新闻影响分析
# ===============================

def impact_analysis(text):

    t=text.lower()


    if "ai" in t or "人工智能" in t:

        return (
            "影响方向：AI应用、企业自动化、软件服务"
        )


    if "oil" in t or "能源" in t:

        return (
            "影响方向：能源价格、制造成本、资源产业"
        )


    if "trade" in t or "关税" in t:

        return (
            "影响方向：全球贸易、供应链、出口企业"
        )


    if "rate" in t or "利率" in t:

        return (
            "影响方向：金融市场、房地产、消费"
        )


    return (
        "影响方向：关注产业变化和长期趋势"
    )





# ===============================
# 新闻读取
# ===============================

def get_news(title,source,url,count=5):


    print("\n")
    print("="*45)

    print(title)

    print("="*45)


    print("新闻来源：",source)


    feed=feedparser.parse(url)


    num=0


    for item in feed.entries:


        if num>=count:
            break


        original=item.title


        if not useful_news(original):

            continue


        chinese=translate_text(
            original
        )


        country=detect_country(
            original+" "+chinese
        )


        print("\n【新闻】",num+1)

        print("国家/地区：")
        print(country)


        print("发布时间：")
        print(get_time(item))


        print("事件：")
        print(chinese)


        print(
            impact_analysis(chinese)
        )


        num+=1



    if num==0:

        print(
            "暂无高价值资讯"
        )





# ===============================
# 开始日报
# ===============================


print("财富日报")

print(
"日期："+
datetime.now().strftime("%Y-%m-%d")
)



all_news=[]



get_news(

"🌏 全球经济雷达",

"BBC Business",

"https://feeds.bbci.co.uk/news/business/rss.xml",

5

)



get_news(

"🤖 AI科技前沿",

"Google AI Blog",

"https://blog.google/technology/ai/rss/",

5

)



get_news(

"🚀 科技产业趋势",

"MIT Technology Review",

"https://www.technologyreview.com/feed/",

5

)




# ===============================
# 中国经济
# ===============================


print("\n")
print("="*45)

print("🇨🇳 中国经济观察")

print("="*45)


print("""
来源：
中国官方公开信息

重点观察：

1. 宏观政策
2. 产业升级
3. 制造业变化
4. 科技创新
5. 消费趋势

后续接入稳定数据源。
""")





# ===============================
# 商业机会
# ===============================


print("\n")
print("="*45)

print("💼 商业机会观察")

print("="*45)


print("""
今日重点关注：

1. AI企业服务

人工智能从技术突破走向商业应用，
软件服务和自动化工具值得长期关注。


2. 能源产业链

能源价格变化可能影响上下游产业。


3. 数字化升级

传统行业效率提升仍存在大量机会。
""")





# ===============================
# 财富思维
# ===============================


print("\n")
print("="*45)

print("📚 财富思维")

print("="*45)



words=[

"真正的机会，来自看懂变化之后的行动。",

"关注产业趋势，比追逐短期热点更重要。",

"财富增长，本质是认知不断升级。",

"信息很多，判断力才是稀缺能力。"

]


print(
words[
datetime.now().day % len(words)
]
)



print("\n")
print("="*45)

print(
"本日报由财富日报自动系统生成"
)

print("="*45)

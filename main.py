import feedparser
from datetime import datetime, timezone, timedelta
from deep_translator import GoogleTranslator


output = []


def write(text=""):
    print(text)
    output.append(text)



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
# 国家判断
# ===============================

def detect_country(text):

    t = text.lower()


    if any(x in t for x in [
        "china",
        "中国",
        "人民币",
        "beijing"
    ]):

        return "🇨🇳 中国"



    if any(x in t for x in [
        "usa",
        "us ",
        "america",
        "美国",
        "google",
        "openai",
        "microsoft"
    ]):

        return "🇺🇸 美国"



    if any(x in t for x in [
        "uk",
        "britain",
        "英国"
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

        utc = datetime(
            *item.published_parsed[:6],
            tzinfo=timezone.utc
        )

        bj = utc + timedelta(hours=8)


        return bj.strftime(
            "%Y-%m-%d %H:%M"
        )

    except:

        return "未知"





# ===============================
# 新闻过滤
# ===============================

def useful_news(title):

    keys=[

        "economy",
        "market",
        "trade",
        "business",
        "energy",
        "oil",
        "AI",
        "technology",
        "chip",
        "robot",
        "finance",
        "bank",
        "rate",
        "policy",
        "industry"

    ]


    t=title.lower()


    for k in keys:

        if k.lower() in t:

            return True


    return False





# ===============================
# 新闻分析
# ===============================

def impact(text):

    t=text.lower()


    if "ai" in t or "人工智能" in t:

        return "影响方向：人工智能应用、软件服务、企业效率提升"



    if "oil" in t or "energy" in t:

        return "影响方向：能源价格、产业成本、资源市场"



    if "trade" in t or "tariff" in t:

        return "影响方向：全球贸易、供应链、制造业"



    if "rate" in t:

        return "影响方向：金融市场、房地产、消费"



    return "影响方向：产业趋势和长期投资机会"






# ===============================
# RSS读取
# ===============================

def get_news(title,source,url,count=5):


    write("\n")
    write("="*45)
    write(title)
    write("="*45)


    write(
        "新闻来源："+source
    )


    feed=feedparser.parse(url)


    num=0


    for item in feed.entries:


        if num>=count:

            break


        if not useful_news(item.title):

            continue


        chinese=translate_text(
            item.title
        )


        country=detect_country(
            item.title+" "+chinese
        )


        write("")

        write(
            "【新闻】"+str(num+1)
        )


        write(
            "国家/地区："+country
        )


        write(
            "发布时间："+get_time(item)
        )


        write(
            "事件："+chinese
        )


        write(
            impact(chinese)
        )


        num+=1





# ===============================
# 开始
# ===============================


write("财富日报")

write(
    "日期："+datetime.now().strftime("%Y-%m-%d")
)





# 全球经济

get_news(

"🌏 全球经济雷达",

"BBC Business",

"https://feeds.bbci.co.uk/news/business/rss.xml"

)




# AI

get_news(

"🤖 AI科技前沿",

"Google AI Blog",

"https://blog.google/technology/ai/rss/"

)




# 科技

get_news(

"🚀 科技产业趋势",

"MIT Technology Review",

"https://www.technologyreview.com/feed/"

)




# ===============================
# 中国经济
# ===============================


write("\n")
write("="*45)

write("🇨🇳 中国经济观察")

write("="*45)



get_news(

"中国政策观察",

"中国政府网",

"https://www.gov.cn/rss/zhengce.xml",

3

)




# ===============================
# 全球市场
# ===============================


write("\n")
write("="*45)

write("📈 全球市场观察")

write("="*45)



get_news(

"市场动态",

"Reuters Business",

"https://feeds.reuters.com/reuters/businessNews",

5

)




# ===============================
# 地缘资源
# ===============================


write("\n")
write("="*45)

write("🌍 地缘资源观察")

write("="*45)



get_news(

"能源与供应链",

"BBC Business",

"https://feeds.bbci.co.uk/news/business/rss.xml",

3

)




# ===============================
# 商业机会
# ===============================


write("\n")
write("="*45)

write("💼 商业机会观察")

write("="*45)



write("""
1. AI企业服务

人工智能商业化仍是长期趋势。

2. 能源产业链

关注能源价格变化带来的产业机会。

3. 数字化升级

传统行业效率提升存在机会。
""")





# ===============================
# 财富思维
# ===============================


write("\n")
write("="*45)

write("📚 财富思维")

write("="*45)



thoughts=[

"真正的财富来自理解变化。",

"投资机会往往隐藏在产业升级中。",

"长期主义是财富积累的重要能力。",

"信息只是资源，认知才是优势。"

]


write(
    thoughts[
        datetime.now().day % len(thoughts)
    ]
)




write("\n")
write("="*45)

write(
"本日报由财富日报自动系统生成"
)

write("="*45)





# ===============================
# 保存日报文件
# ===============================


with open(
    "wealth_daily.txt",
    "w",
    encoding="utf-8"
) as f:


    f.write(
        "\n".join(output)
    )

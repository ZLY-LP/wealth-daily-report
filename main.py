import feedparser
from datetime import datetime
from deep_translator import GoogleTranslator


# ===============================
# 翻译函数
# ===============================

def translate_text(text):
    try:
        result = GoogleTranslator(
            source="auto",
            target="zh-CN"
        ).translate(text)

        return result

    except Exception:
        return text



# ===============================
# 新闻读取函数
# ===============================

def get_news(title, url, count=5):

    print("\n")
    print("=" * 45)
    print(title)
    print("=" * 45)

    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            print("暂无最新资讯")
            return []

        news_list = []

        for item in feed.entries[:count]:

            original = item.title

            chinese = translate_text(original)

            news_list.append(chinese)

            print(chinese)

        return news_list


    except Exception as e:

        print("读取失败:", e)

        return []



# ===============================
# 日期
# ===============================

today = datetime.now().strftime("%Y-%m-%d")


print("财富日报")
print("日期：" + today)



all_news = []



# ===============================
# 全球经济
# ===============================

news = get_news(
    "🌏 全球经济雷达",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    5
)

all_news.extend(news)



# ===============================
# AI科技
# ===============================

news = get_news(
    "🤖 AI科技前沿",
    "https://blog.google/technology/ai/rss/",
    5
)

all_news.extend(news)



# ===============================
# 科技趋势
# ===============================

news = get_news(
    "🚀 科技产业趋势",
    "https://www.technologyreview.com/feed/",
    5
)

all_news.extend(news)



# ===============================
# 中国经济观察
# ===============================

print("\n")
print("=" * 45)
print("🇨🇳 中国经济观察")
print("=" * 45)


print("""
重点关注：

1. 宏观政策变化
2. 新能源产业
3. 人工智能产业
4. 制造业升级
5. 消费趋势

（后续增加中国权威RSS数据源）
""")



# ===============================
# 商业机会观察
# ===============================

print("\n")
print("=" * 45)
print("💼 商业机会观察")
print("=" * 45)



keywords = {

    "AI": "人工智能应用、企业自动化、智能软件方向值得关注",

    "人工智能": "AI产业链、应用落地、企业服务可能出现机会",

    "energy": "能源产业、资源价格变化值得关注",

    "能源": "新能源、能源管理方向值得关注",

    "technology": "科技创新和产业升级可能带来机会",

}



matched = False


for key,value in keywords.items():

    for news in all_news:

        if key.lower() in news.lower():

            print(value)

            matched = True

            break



if not matched:

    print("""
今日重点关注：

科技创新、
产业升级、
数字化转型。

持续观察长期趋势变化。
""")



# ===============================
# 财富思维
# ===============================


print("\n")
print("=" * 45)
print("📚 财富思维")
print("=" * 45)


thoughts = [

"投资不是预测未来，而是理解长期趋势。",

"信息差创造机会，认知差决定结果。",

"优秀投资者关注变化，而不是追逐噪音。",

"财富增长来自长期积累和正确选择。",

"看懂产业变化，比预测短期价格更重要。"

]


index = datetime.now().day % len(thoughts)


print(thoughts[index])



print("\n")
print("=" * 45)

print("本日报由财富日报自动系统生成")

print("=" * 45)

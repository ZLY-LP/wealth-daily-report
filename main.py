import feedparser
from datetime import datetime


def get_news(title, url, count=5):
    print("\n" + title)
    print("=" * 30)

    feed = feedparser.parse(url)

    for item in feed.entries[:count]:
        print("• " + item.title)


today = datetime.now().strftime("%Y-%m-%d")


print("财富日报")
print("日期：" + today)

print("\n============================")


# AI科技资讯
get_news(
    "🤖 AI科技前沿",
    "https://feeds.feedburner.com/oreilly/radar",
    5
)


# 全球财经资讯
get_news(
    "🌏 全球财经观察",
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    5
)


# 科技资讯
get_news(
    "🚀 科技趋势",
    "https://www.technologyreview.com/feed/",
    5
)


print("\n============================")

print("""
💼 商业机会观察

根据今日资讯持续跟踪：
AI应用
科技创新
产业变化
全球经济趋势

============================

📚 财富思维

持续获取信息，
提升认知，
寻找长期机会。
""")

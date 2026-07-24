import feedparser
from datetime import datetime


def get_news(title, url, count=5):
    print("\n" + title)
    print("=" * 35)

    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            print("暂无最新资讯")
            return

        for i, item in enumerate(feed.entries[:count], 1):
            print(f"{i}. {item.title}")

    except Exception as e:
        print("资讯获取失败：", e)


today = datetime.now().strftime("%Y-%m-%d")


print("财富日报")
print("日期：" + today)

print("\n================================")


# 中国经济观察
get_news(
    "🇨🇳 中国经济观察",
    "https://www.gov.cn/pushinfo/v150203/index.htm",
    5
)


# AI科技资讯
get_news(
    "🤖 AI科技前沿",
    "https://www.36kr.com/feed",
    5
)


# 全球财经观察
get_news(
    "🌏 全球经济观察",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    5
)


# 科技趋势
get_news(
    "🚀 科技产业趋势",
    "https://www.ithome.com/rss/",
    5
)


print("""
================================

💼 商业机会观察

今日重点关注：

1. 人工智能正在改变传统行业效率。
2. 企业数字化转型仍是长期趋势。
3. 新技术应用可能带来新的商业机会。

关注方向：

AI应用
智能制造
新能源
数字经济


================================

📚 财富思维

每天提升一点认知：

真正长期的财富增长，
来自持续学习、
理解趋势、
发现变化。


================================

本日报由财富日报自动系统生成。
""")

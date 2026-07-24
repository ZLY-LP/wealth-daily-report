import feedparser
from datetime import datetime


def get_news(section, url, count=5):
    print("\n")
    print("=" * 45)
    print(section)
    print("=" * 45)

    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            print("暂无可靠资讯更新")
            return

        for i, item in enumerate(feed.entries[:count], 1):
            title = item.get("title", "无标题")
            print(f"{i}. {title}")

    except Exception as e:
        print("资讯读取失败：", e)


today = datetime.now().strftime("%Y-%m-%d")


print("财富日报")
print("日期：" + today)


# ===============================
# 全球经济雷达
# ===============================

get_news(
    "🌏 全球经济雷达",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    5
)


# ===============================
# AI科技前沿
# ===============================

get_news(
    "🤖 AI科技前沿",
    "https://blog.google/technology/ai/rss/",
    5
)


# ===============================
# 科技产业趋势
# ===============================

get_news(
    "🚀 科技产业趋势",
    "https://www.technologyreview.com/feed/",
    5
)


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
2. 新兴产业发展
3. 制造业升级
4. 消费和投资趋势

（后续接入中国权威数据源）
""")


# ===============================
# 商业机会观察
# ===============================

print("\n")
print("=" * 45)
print("💼 商业机会观察")
print("=" * 45)

print("""
今日关注方向：

1. AI应用商业化

人工智能正在从技术探索进入实际应用阶段，
企业服务、自动化工具、内容生产等领域值得长期关注。

2. 数字化转型

传统行业提升效率的需求，
可能带来新的服务机会。

3. 新技术产业链

关注技术变化带来的上下游机会。
""")


# ===============================
# 财富思维
# ===============================

print("\n")
print("=" * 45)
print("📚 财富思维")
print("=" * 45)

print("""
财富增长不仅取决于资金，
更取决于认知。

每天关注：
趋势变化、
产业方向、
商业规律。

长期积累，
才能发现真正的机会。
""")


print("\n")
print("=" * 45)
print("本日报由财富日报自动系统生成")
print("=" * 45)

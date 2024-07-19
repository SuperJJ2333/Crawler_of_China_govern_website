import re

# 假设 news_item 是包含新闻内容的字符串
news_item = '''
<span class="jcse-news-date" style="float:left;">
				江苏省人民政府	2018-01-05
			</span>
'''

# 正则表达式查找日期
date_search = re.search(r'class="jcse-news-date"[^>]*>\s*([^<]+)\s*</span>', news_item)
date = date_search.group(1).strip() if date_search else "No date found"

print("发布日期:", date)

from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '海东市',
        'province_name': '青海省',
        'province': 'Qinghai',

        'base_url': 'http://www.haidong.gov.cn/search/Default.aspx',

        'total_news_num': 3,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="GridView1"]//tr/td[@align="left"]',
                     'title': 'x://a',
                     'date': ['x://tr[2]/td/text()[2]'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    headers = {"Host":"www.haidong.gov.cn","Cache-Control":"max-age=0","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Origin":"http://www.haidong.gov.cn","Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Referer":"http://www.haidong.gov.cn/search/Default.aspx","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"security_session_verify=fd88e2ddcdb5eba52255e7bebd6869dc; ASP.NET_SessionId=ht1lhorl4gabc1o5ibuzbsrr; arialoadData=false","Content-Length":"5499"}

    post_data = {'__VIEWSTATE': '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', '__VIEWSTATEGENERATOR': 'CCE6BD4A', '__EVENTVALIDATION': 'FHgcvusv/SbqbioeO1C3wGbXjB+sBJpyazK+vmu70KhD9BjEF6+qILWdLuWovykZaZLKKsOn9h5VKlxvWfQ1Tc3wXHb9SHir7B0I92PxL2iwWV4bYMlkdQw0TvSKi1a+hXqeA71Gt+//SGZb3IH9spTlE0b1A28G3tJaekrJbRgRWm+GdtrbB+k8XJJqx7qRjpkbXXzAZlMvDglkE0TWt+kVsEwLrE/ys+B1I3E0qjErJaS2q3KZF4MDHiQsajsLwduU3h908in3bwCk/A8JTksQ5MnHI1rAwijsCk+GOWvrF4w2UtF2XLaXCKP5B6MK4vp+hj3jq+qYOjNs8mGCQ7V/2SxCpMYiihiSnr6Q/1671wBzGIJv/MXwN+DU4Sy/iUl1xTCs/jMOMirvs0fJQGA4OTeussOM7NVdruCEWxHgVMnZl5HZQNo+kVSRAq0bKJP96VXtjdEeNTiPzGtXF4N1JUSP91gG0LKjzYO7YKSG0wHeSGhH7pOBX1dNJg55R6YBV14z/YwjtBdvCO6rlF74mygU6qU/x7rTBw==', 'TextBox1': '考察学习', 'Button1': '搜索', 'CheckBox1': 'on', 'chkHeader': 'on', 'RadioButtonList1': '4', 'cdate1': '', 'cdate2': ''}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      )
    scraper.run()

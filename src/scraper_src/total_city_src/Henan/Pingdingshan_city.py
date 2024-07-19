import json
import re
from html import unescape
from urllib.parse import unquote

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = data_list

    extracted_news_list = []

    # 正则表达式提取所有列表项
    pattern = re.compile(r'<li>.*?<a href="(.*?)">.*?<h2>(.*?)</h2>.*?<i class="date Cdate">日期：(.*?) </i>.*?</li>',
                         re.DOTALL)
    data_dict = re.findall(pattern, news_dict)

    for item in data_dict:
        try:
            url, raw_title, date = item
            # 清理标题中的HTML标签
            cleaned_title = re.sub(r'<[^>]+>', '', raw_title)

        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if not url.startswith('http') and not url.startswith('https'):
            url = 'http://www.gswuwei.gov.cn' + url

        news_info = {
            'url': url,
            'date': date.strip(),
            'topic': cleaned_title.strip()
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：API
    提取方法：JSON -- result -- 
            re：unquote：href="visit/link.do\?url=([^"&]+), 
            r'class="jcse-news-date">([\d-]+)</span>', 
            r'&title=(.*?)\">'
    """

    city_info = {
        'city_name': '平顶山市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://user.pds.gov.cn/api/User/T?parms=opt/search/',

        'total_news_num': 17,
        'each_page_news_num': 10,
    }

    headers = {"Accept": "text/plain, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br, zstd",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
               "Content-Length": "10230", "Content-Type": "text/plain", "Host": "user.pds.gov.cn",
               "Origin": "https://pds.gov.cn", "Referer": "https://pds.gov.cn/", "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    post_data = '{"fulltext":true,"isallsites":"false","sitename":"","sitedir":"","siteids":"","channelindex":"","channelname":"","channelids":"","type":"Title","word":"学习考察","dateattribute":"AddDate","datefrom":"","dateto":"","since":"","pagenum":10,"ishighlight":true,"isdefaultdisplay":false,"publishmentsystemid":"1","ajaxdivid":"ajaxElement_1_1","template":"NLSQ62sDQn7D5HjYIR3TcDNfoc7gbcn6uGQGWAmzkLXPRfZgoMpfF0slash0MkhrT0yNCJNn8wi95WsrnNeox13f0add00add0Wv74B83btNR0slash040add03az5xZriwELXcCng7BuNWq7D0add0Z0add0RspyP5PazsbvxY6PlFIbZp0SNkuXRYB1o7FZcFA7ucXLuCgolL9bObk4iodaHj9q3OSrSalOcmIi7bx9awxLHKQD9ZGm61zFrE44cer0add0PTN0slash0JiRI3JU91rLeywbzOH3OIK11pHHldwws6KjQEn2mrQoNGVHd42zov7H5TGqNFCstzVyY7n9LFc8ZsQYKa2MAOyU2qqm6LwJV0qqVgC5KT3YQw49t3hs27AkgO2mKL2hKf60PkF1PI2NWYTq7ecOcCgMYzyz7i80FE7d9TdPfrg8d9FSaKR0LYxdhtzwKoEBCVcyH89cmR4IDSu5x88OCQKQQ8Sclvwb0zb0add0T0add00slash0NrU4Riza6e6ZYuJ0AizMf0slash0kRvdPtC6Llb85v6uauwulOuYYSRY9YHebPBTK6KZlNMcKUX4YqGYl80slash010add0TWGOGXc90XL0slash0bEmlqiok2M0add01zJFbiYYbji0add0ZQLenkd16cDVdme1SVi0CeoGvIJ9OAP2VtIPFzNBTFw0tSPp80add0iPf10slash0ZFXncuIYt5tCHrbbKv0QJVJ2Q78oocD9PLCBrWMhGLDbCDhd5ZM5rZ9P0G8fcYTkckBPPg1yiHj6XSQYkp0887vykBVnKxbnBGpm4b0add0WLQUvMwY44EhZEr8vR19QgGErgZ0dAP2itn9mkgQUD0add0Hk5anoYTA1WOucqod8fgmhCdfwahGZNXR78VoSuQ3HoSCsdVtDiyu0CCO0slash0wX0add05V0slash0e8S0zNTf0add0eltSkm51MlTyUNsRWkg4pHBBJy87kwwz1O0slash0rs0add0N9kP36nTuRoXRVWUhh4Mxhc9gyS78fDBNu2ELdyDHWmZPuP7g0slash0SvpEu7uji0slash0KTxbcOZS00dyji8H6nJpwgOT2FacZwwl0Yy0add0Qtie1oBUzlzv0slash0pGcnjvBztUWAeiaNqwBa7SPqqHQgcHgNboqnSOppZYRcQVWz9nTeKJzi7sXSJb3LwAwqHzHWZpfUZhP5MYe7JNRLbrX6xwIZWJlfjAceKCxHF8oDAEX0slash06VmLQR0add0jUmQTZC4NTsX0add00slash0CbG9IslJjNj7jfktt8prf8YoXSb3Dw0add00add07CkR80slash0IxyYgzyz1uCr1ziL3lV5fnQbLTRHjM7s0add0qy6nr0tRiC1xGjpeJgai3SPX7n8lboOCiZ7An1mMvZdcXvZmErtznZzqRwGMUEdGP0slash0PzJ1pmLWidvjVvV0slash0gipdZHMZJ9NoQLj0EFBmOKAQzSL7UhNNN0slash0kYhXdi4YmSmJYJiZV8HMee1xaDpzXa3JJ0add0IKZWVXCa1JdkcVssoa83FI3Pt88x1OEAC6okDgGDOzXcYbGCyEo6Np0slash0RQ7okU6xJjQ8Df3XNYRqXph0add0GOTEgZ9nnLQp4lwWtnmj8n7evN0GWKJHn8MHSPb1MqSrPNiighsAx883HxlkUiIFqT1KIlCswTjC2GycQTZT2pB8IBMDggwx5B33RMZvQ263tZFFyael41BWB6xn999dj0QPb3pPyJQ0A1iP5I1ywpx3TlYntWzc57aHOW0NtvAaj0add0TQ2Tkwt5Wuw9ezrCal1gyNjm6jcOCoeocRBFn76KueXbD2HM4WmVGu0add0VYmSZzdhMxIdezmt4EwT6FUyANKU08naxBvDWTCj20c8rdr9CfBIUkP0add0g9DSqDzoSIARXY8N14I9pfWfoRmSoN5f0add007h63wW2LdJf1RKH4zaEmu4MrafubCQGAIUUIHbzfNHJcOEAPaFA8kS8LO7ohKhjvKSRuR6Fi11kZksXYluzXZIOIfeQGSsFF4RNTl4C9xmU0slash0BHf6vWhhbnehgd9y0slash0rJVmeosTl47anKMOOJz4bwN2vd925u9CctTS9oHTQZ4286DcY1fAGIHCGghWQjpq899M377AMHLdgjv6j1qxANBeF0slash0b0a9BVzCGkurQ1X8eoaEnq9HUW5Z3iD0slash0YpTT870slash0ZYfkB4w4M8fLKDaBcozcBTMnE0add0iENHfsUyjksqWLFM57x0add0l2Wc9112l0slash0suSFGc50add0YpAgE1ari9Ug0UH60Zj0add0zN1SJvW06fZaqxMmQR4JPvEeCBLktrXZn0slash06IWf3E0T5YO3TdedKfUrgVz5i0slash0LWIrFP0add0bp5toz323G2rp0add0BocPx9ZN0slash0if3DOx96Qk0add09R1RcLTerNZVXGmHS1op2BUfs09372pYnpu3EkQcDcfWoNKifgKze40slash0WIfjgODX01jgALlRbTpLYetADI7xn0add0TbUCf0slash092GTjV8ypxp8jtocnRgbjeUgDN0vfyZWxYvoxGInz34r7uiKxbF0slash01WB1UBIS5b1e1U5G9byFMaaTHAWYV4rWGuK9IACZwfVVmDBX0Qw2anecg8MUhg76UOGlpfJWx7ikTI7MtSayMnIi2iXZNMNnMUep6vcyo0slash09TvfmqIyoWgUaM4ExLjLThl44o6abOaLksMfskX90yj8R2Y0add0mL0Pcy9YSJXu30add0gOVFgVM9bRykZy0add0V4HTTW2tzsc6gtXbsBH0slash0wQBrzCzEtxUuc1ZiJdZbGVcVT60add0XERHD9dwALSXBXfEVICwWkBNyeX5r61fWnMQgBlGgBHexklXu3eoRIdfgz3QNpNKJz5riVekR4sQy2st0add03l2XMZS8aETGOEQKbNaCR84ciI2kJSvgAQOjh4KBBAxazRjqHwk7DyG1F1uuZ8NEhn1VKgEy2E5J9ssxZLDVjdIue4fIeJLOYSvaZwXTLC49ozctwAcavfxlemkHXbuvzS3by8o2JEv6o88G6yKRV0slash0bkDgzu5vuFM0fVp769Tbs54NNi1Z0slash0VLkVb60add0Ftv2x5mYFh6KOeCr4PddRpitoZ7Raxzi0add0uJ9VUxif0slash08RaBYT9DmEjYMTp6sWC2LFdgqP0Zku4QWNT3L0slash03jt7cvYvf6OcY0add0ktKIG6G00add00PnPJuGEeZ0slash05Cm65AVWGPVQ7zjP9TWCFlg0kdi0QHbOC4ysbVBcSgTy8LBVq0slash0SaIAV0add0ywQNlzR60add0bmS4it0maS0slash0hJfLIXhU47s9PuZ0add0af0add087UXgLC1Dpxj3Dlw7HvWtS8Pajsndr0XLsHeyOvN7q9o8NFq0slash0kZDe0slash0yVB2q3q4MUOGCCJuBpBfhjBJ21BlnGvyVqHazgB68oek0add083Jh7jwNzp5mr0slash0pwi0yb3WJVArWNiWC9X0t0add0sKk5CPK0add0g0add0KKfeXddQnrd7OOkzSFXp7322e6O0add0zkjSg0add0XMGisRN1M8yWHnATj5AZXyPfYFvBkXJXaBu1dlVFthyDBtN7hh3xwF9ThBjX0add07pkzJGLLyME3C7Vuwix0OaNE0slash0vtxA3JEpbg5PqifLqfhPo2E6sTcL6IzqllJhXSxbX5acxpM0add0tWYIH8n9v6xzVRf0eCTNpe0add0rSXt8Lj6kKEVIpmiyHSjwB8xjJ2nTdyzrIVCzjNALBGFDG85RByurE2MIQ1ntZQmbgOyFSUKQ5XprtJvw1IA7qUpktd4m5dIKmqgOCMptt1RBmu4X1ZGVntlsSBbKTeYYfd2MOiMPlQxmeHKeHtQAja0wV6LUWcorMSXxgqAJV8zQGd14H73idE8BCVxc5hlrw0FyWA3oapuOpdvjdUfBRbLFO1MlfbcAihxNjFtUQwIBKD1gi55v0rqux7XEAdOX0ayBIk55q2rKb3nL2OcQb5vC10slash01Ur9lMgZMRx0add0xXARRkvzqImLE71LBn0APJip2ZF4AqAsWq8PsJpNU0slash0M1GS3NJE0vguYoNLhz2mnp8sf5DanpXE7UftwpDPWmer82eJP7E6upiLjn6ChGVeKZ7jzJOVvqKQKjVZZrCBNRqpPYMzv1c0LrIHV7vb06vLWO2GPk8e57jpkjgYFeeSbJyyyDQEgJd3foZKoUKCo245c0add0h0slAy7R0Ds3LQztKOl9aecpBVEPrPaqRQ9UYFsscnrij2MhbqS0slash0A97U0slash0uFirl6ULOC4WzJoE8VDjscir0NadWMDroOoUJpxkmH0YwltzWyd0add0ZD9UL0slash0QqOO4flLTKrr39osZgta0TbClfQabj6i0DOEJlwV08CU3L9rPjryyRB3z55gILBaMDTVhi9gKV9CFgbs0slash0bFbcveIvH0slash0mv4XIHWmxKBuK56Vh5PW0OEf3sLvf0ecYO6ytSTHaOSleubjcWZz9PcfE11TayGc3DoCi5Tn8B3DTjphIavXT2I6HJ6oFLR7ufBkG4DVEfExzrqSIFw7zJAjtz88u9n5pZTSRVdIURHWs1aI7kaGbrz0slash0WKK3s2JbchTF4kODsXxCRHQPZkYsJQCBUNV21n1JVmGFLBKs4oPBC3OdAye70slash0zCoEHReLig3d0thkwkgu3V5m4VpRs1ZvkzUwh5AqOZzjuhpjeJeNqAjNkEkv1gMmuuC42ndLR9sW2BQa0sBK3W1NyJX15KSWF0slash0cvo9mHg0add0TEZ0fhhry9eKnOKK0slash0QNuwqKCV0DMCFtBaAHOrVKwUWogeGMzla7Z9r0add0CG0tNk7mG57VWeA1TBApGFv38QNffZEWFJTXADBJz8ZrIR0add0mFgYi0slash0f5rzLydpez6zLtkWTH4r6cy0slash0LY5RPfASUR0xZvaWK2GaetPPQy18DnnTHF0slash0PhLqk4aym0slash0kmJ0add0NvP0Z9BkfNr5z5hv0add0ZX8PE00slash0cjzOrtIYDaNjW2UB1ckOzeFeQeykDBrgZzqKYw0add0EJPJZzklUECtOJjX0slash0Zww2jq0slash0iSnQkPS5tUMCKw9j258BGwQEpYVIoE3A60add0P2mwoo3PIEm0slash0cKv6SQAXmFKrtxo8gTYeqt7vmUEVT8GipCoqlCAS7W6WyfBbUcqpTio0add0a5Gypi3OMEpKHkPkpRuay0add0aEsNHn9JOgo3BYekSlKRai80add0eVBJLSLjL7MLYxwlbhRDJeBKu0add0wqWB3nVbkK0slash0zAlJra0slash0UmHm5WgnsTMMwYG0slash0Y0VGScc0slash0oMgooprOipfaw0add0pTrGxOcqoex4A0slash0OcU0LMJ7e13y0add0meNNt0add0MxWTuT0KpCEVXmQzpmPQgoKZRBjDMSunCvlvKWKGTvaRfJT1UYS0sVi5YgIk5ed9kzf1NykGnLP1giMd3m5brl0slash00add05yRQhGb3Ng3VtabCkBipvUqz8pZ0add0X6sTzRmHRUrGiE6Uv0slash0wlN0uAeOgBbLS0add09RBBKonxkBdZ1zCMUJ2ynk60fvljAhmztW6fKtRbSrfYk657c6HO0add0gNlQp7OFyqUHugtx0GklWmln46wCI9myDRbrKGeg5LLU0x806HCI8DWLmBXCWXY8i4dGf0slash0Yp6aRTrXaOAbL0add0f9yyEJSlED0mWWbmC8xhbteBCpJ1q8iRYkz9kJesMAu6wkOjLSyMbVtyF1cHoHNihQBjcParil3tXuo5J0TIOxgXtVbdTPfOH04HygEADnk9hfFZS87M4hpKKuOF1KOF0hlvrY2Sl9fpzP9s8sLSOKPYt9GBegHxB73EFJa7BjCcdtw8z2lL0add0U0TPkjgp9f8kg8Vap5IficaexpICRVUvFYvUKyeaT82DnH10add0UJjPAR0add06EhLhE7KW1A2dxq1NWiEzxqqiaJaRHJF0QESQtXEfoWMH0slash0sPhh4G6l4sfHXUefug30add0QYplWYK4H3UPyUQ0add0Cq9mvMcQ9DmQVJAQVw5pjZDM2JfdWmDVivJF0add0h1zzEJAp0add0gB0add0BQcZl1j0slash0Hd7PTDp1evQd0add02z879VXxOVddy9sgYHT0slash0V2Jwr7KK2o20N5TpAmqp1jX0slash0jzQ0slash0iInE5mPJKK41y2QPY3c1yDKZo9IiXScq77YBdZpEmPc3rYkEdAJTl12rqt4UpiBdPURKKyea2lcZist0oyZqvOXVSx16QJQMKV60f29sMW30add01RzEhteqr0add0zwOWbn0add0M0fJSzO10slash0qvgTmHI0slash0KmJ6P4Agx03YeZUFIG0slash02HpJOAxSJBbqydw6d0Z2A0slash0Zta4UybM0slash0x0add0ZEAIyURf0hnkBhxnAgNOk0slash0Ex063lcyKW0slash0iSnP2emJy4dat4yIslEKY0slash0gZ2RIv3ri8Xi6KVcENJolVnw7lyxaNuLTwvki5F1OVTGKBBV0KbQdgkjcP0Y9sRr2Z0OrD6TBpdt89GezJSLw0R2Fp8IqzlyuY98C7x2p9csjheU1ZThWi6ZsyMZ486FkhJqUH0add0MXZw1JmNFUM0add0p8sx7wdLRqvPR8O6dngX89yKqC8dp9LR1qDrTZMogK7VHfwQURoVEuCt0add09GEvvUuLxSYw9PIVUawe7z0slash0bcpdmv8O2yU4Eq0add0ps6yai7cStPWQkqXdb6xsN00HBSrsHll0XI1KcT4rXPXdM9c0add09WBXmILqRzPsPWFaLQzC1rdtTaJquwKXEukgeb6lnr3cEnsZs3LhX7Js2rEjfxvhjgvvAi0add05d420HJWkytATknBjzeLRt692cIA1sLQ6zBQm7x7GRnTOaTdD0slash0l9XbZ04cq8pfgRpniM0N9bjTcUPzP88p89SPuY2SLbrn4t8yRK7G940slash0IPAWSownjUl0add09Oc2S1ujkacCOBNIIDCh0fBWzpz0QpRI2qJ3q0slash0tdYWt0slash0Xn6twl3TbkK0slash0eNN0add0jgUp9u8ZgJyHhocyYXfbrps48XD0add0YGzm0add022j1gzLK5MW0add0F7YyaypjDSl3owAaK2ZRg2iIOc9YLuyCyzk5Y8N44320add0x5gZQnDicJTMrsLe7KmlqxHPh8qsShf6iqPCP2OdBrR8F585HABjVjotsrNC0MOtlis0fhTwvJ4AtZ2GSQO7p1rdr6OiBNj69oTfe9jIRKegDwXD0slash0o8SBGR7gZKAaE5z3qcmd5x80add0NyelpSu0X5OvKZX6tn0add0X7EWKvddDqR1oV0add0hxoqRGdw7h7zZpZZOZM6c8O10slash0xzL68HpjosHAWCl0S7Mdgui2aMxAlWlPSyYplgeGpSN6aZQJmNUjCltA342rLO0aNqWlT0slash0NGLWcQuUDbN121a0add0OC5bD2ozDSndbwIlSuRZiYXxYdrCuRbUfrdQ5CWrJgcoiqxlSNOlvRap5dYIFNLV36gEFP30xE0add0bKY5x4q4VjP6xVX0iTGgJChQdue8KWvoKzgCuJSI7Y0QlGIzigb00slash00slash0Yfx8eTpCbxhPEDB3yXpwRGO20add0eUsVJLSom5DObYg2UNyNtIrU6UtKSxj3Z7Hq4v0lhR70slash0e0URl6N47IM20add0Asnr6nkge0add0VhE9HH4e0add0T5EGsuZCdGOnSZkeRVJMaeZ0slash0GOUbA4dNZW9QoOlZXlmRdzFa9cB3Qa8kuZ0slash0r0slash0oioqPjp3oIB4feeCjjRigv69W0LMXq9dV0Jor0slash0yAdfkM8jamV2CPmbUlc30slash0itAEgiRhfrML0MdLznOHpT3R0rqAlRAX60slash00SdeUtLSDZv9lu40U5Xc9f0add0XZfia5F5YA3efyFjg16uSAlwXMbmty4FTLfOknHw64OhPtk6Gr5cOP0slash0N9PEYzsWg2T5LAoMs6fKiseifXKtFChptLgu0slash0dGqmidE4AJeMbpABc6Ef30slash031KoG30K5KLdRv5ipilu2z0AcrO0add0xFwCzY5fJGLwcpbMn539Qb2JqttXhDvWFJnmns0g9R9siIwbZFwstcsnTK0kmCeCtqUBSAKVC3M5HChE1eXbN7EST3j0slash0qKKF0slash00oMYAF6wPrJmsCBUvModdlprmCUrSr5amumf8MUeU2VPFIhaBpcLS4SF0slash0lODuNg30slash09T290add0aqMtmFwC5zATGsG0add0dXxvla7Q7NKGHErOPGilS1i2cYdSRjeQKI1E0slash0s3EkVlNLR8CNOvOsEm4CLsjA2Lbl3YO0add0Hd92fVDyuoXVfDdotYg0add0RpiCzgr0Zc6t0slash0CuS0add01IAdDFRVkTp2iP042d3nfd6an280oOvePjNYKI9SlPqMQWr9kV2wwoOFHDHWQJYn0slash07vnOY0slash0OFWI7ALHPs7pWXPCeqBMO1LX1aok6C4vdomVPcn60XkZkDMa0slash0z11b7D0slash09B0add08y5MSmQPcnKmKRkE9zm1rEWYgMdUsXH11SO4fCpgI0add0HWAKl40vqB6xgHeSVaT7doyy0slash0oObqrPH2vEeD4sawC2u0slash0lNDN3sZ109HhWob70slash0ShtcmDX8UwSiezxdL0Zx00tX0slash0q5b50b4qy6lkrY7yA6Jky6noIlddRaYxxKdCxAZFVf9CrRCXRMsm90N6B0slash0CaSVjoydjSBl0jafF0add0JLJbaogjnRyUkZt86O0MBLpldBq0ts2cWYfcNnNj0slash0GvdbF2FpY1UzNcMKOdipmyyq5DAvh10add0pEsbfjLvRrJhVGXdOVYLWO7z9nADDzES3jYGkm2Opyn1DbypW9xzEUvuwlzsLaPJuIFZ3mcZtYm0slash0XGKYoaqpljbNotHVeHN8DGdBRWU8zY3vZoDHEjRVXY2sA105eYXracgJxl2z1PVYHG91MK7psDuVIa0add0wmONrw8pTol999zWS4qBzsNrTqhfQEfLZz0slash0a50YP0add0TQBS6qyYnJiJp7NzzXBkGhtPmA2T0zlo3ZnZ66bai8WsK0add0RYEb7OrEEwLqP9K0jYlO8QKQNAFwgOiF4ARoXzgJqyB8eCXX9YzJzTeAunuNp0CLAhCmKUGbhX0slash0hj6KQTVzKbt2lN5bXoXk5blWxGELyIpTg2G6eBgNSRqneQhctpm0add0pKkqwb6OmnAxJd8491qQoepx7IfsZMEeIk2iak0add0S9nXrsfKtGgQQrKn0tELSbFSWNb1BiNrEDIJOT8lGf6KyAeg05fWsEqJXdcHm7KDm8M07sti9NzXOjC20slash0ltLvd","nosplit":"True","channelid":"1","page":"2"}'
    post_data = json.loads(post_data)

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, is_post_by_json=True)
    scraper.run()

import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('page', {}).get('content', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('trs_time', '')
            url = item.get('url', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：API
    提取方法：JSON -- page -- content -- title, trs_time, url
    """

    city_info = {
        'city_name': '湖北省',
        'province_name': '湖北省',
        'province': 'province_web_data',
        'base_url': 'https://www.hubei.gov.cn/igs/front/search.jhtml?position=TITLE&timeOrder=&code=872801132c71495bbe5a938f6acff5aa&orderBy=all&pageSize=10&type=&time=&chnldesc=&pageNumber={page_num}&aggrFieldName=chnldesc&sortByFocus=true&siteId=50&name=%E6%B9%96%E5%8C%97%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&sitename=%E6%B9%96%E5%8C%97%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&sitetype=%E7%9C%81%E6%94%BF%E5%BA%9C&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&6LDjm9Ls=0c04WxGlqElYOvuLvuyIgH2wI0hUyY2lVxws.T6PJko10LxRHRoAeAEM4g0xm9yDzXbVuq0Ts3WxqnS8dmIRY.v0ceq2L72FVJCl0F_zCkQRsLiQ2gzp2.pqZhLgFsybi8YG4qREe989',

        'total_news_num': 121,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=FA6A6E6CDD616CBA10BFAF3744F4B395; _trs_uv=ly3zosn3_3027_g0id; uuid=139b4659-aabd-4239-a686-47da791f577e; 97badf5c34b18827e4=24803fbc5fd4622644cb84cb8ce5f78f; _trs_ua_s_1=lye9o88m_3027_9alt; Hm_lvt_5544783ae3e1427d6972d9e77268f25d=1719899388,1720520820; Hm_lpvt_5544783ae3e1427d6972d9e77268f25d=1720520820; HMACCOUNT=A202F23FD4E0D795; token=c07fa9ae-e4ef-4db9-8368-ab39ebf6a0b5; 924omrTVcFchP=04EbEh53TcpeJX2PJPQS7An.xZSLnWIgNgf7rKubzLgk3FM_DJbZQd5BoEGNqSBIONyJF6LIaQTNWy0xrmNpFOxF_aEfi4bir7TqnRZvMTNFje4ya3.ewBId7PAsNOxLFOj5tAkQLYiKonL143pHMVz8EkhR_n_J3eWXkNiZpaaF8HlAFjWRdF8PAs3QogT.OeeOwAiSdJlOtDy.Cek0pBInRdhYISK7BL8t1mc737qMLzFJdPtSAfk.ETUjo0UETRloSsYKpy1cyoBvsfqk_nYgkSra3Fco_WaT0S1rlnuJ78BMVMojGruxIK2YLoSCvPDdbz50umzg_NGyxPMn1l5mGFSSbOnXXiHmsaEctW03","Host":"www.hubei.gov.cn","Referer":"https://www.hubei.gov.cn/site/hubei/search.html","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()

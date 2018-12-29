# -*- coding: utf-8 -*-
from builtins import range
import scrapy
import json
import re
from scrapy.http import FormRequest
from hangzhouhotel.items import HangzhouhotelItem
from hangzhouhotel.items import commentItem
from scrapy import Request


class HzhotelSpider(scrapy.Spider):
    name = 'hzhotel'
    Hotel_list_url = "http://www.ly.com/hotel/api/tmapi/search/hotellist"
    Hotel_info_url = "https://www.ly.com/HotelInfo-{id}"
    Hotel_comment_url="http://www.ly.com/hotel/api/tmapi/comment/list/?hotelid={Id}&page={page}&pageSize={pageSize}&commentType=0&roomTypeId=&tripPurposeId=&RankType=1&mainTagId=&subTagId=&antitoken=bbf8b47ee54e5bee512ce588dedf27ec"
    referer="https://www.ly.com/HotelInfo-{reid}.html"


    def start_requests(self):
        for i in range(1,5):
            formdata = {
                'CityId': '385',
                'BizSectionId': '',
                'SectionId': '5191',
                'Word': '秀洲区',
                'PriceRegion': '',
                'Range': '',
                'HotelStar': '',
                'ChainId': '',
                'HasStandBack': '0',
                'Facilities': '',
                'BreakFast': '',
                'PayType': '',
                'SortType': '0',
                'Instant': '',
                'LabelId': '',
                'WordType': '1',
                'ThemeId': '',
                'Latitude': '',
                'Longitude': '',
                'ComeDate': '2018-12-29',
                'LeaveDate': '2018-12-30',
                'PageSize': '20',
                'Page': str(i),
                'antitoken': '173c3cbcef9743345508def6f366c2c1',
                'IsSeo': '0',
                'iid': '0.4408395304904118',
                'TraceId': 'ac1cde21-c6bd-4644-920a-eb38e7aded95',
                'HotelType': '0',
            }
            yield FormRequest(self.Hotel_list_url,formdata=formdata, callback=self.hotel_parse)

    def hotel_parse(self, response):

        id=re.findall(r'"Id":"([0-9]+)"',response.text)
        name = re.findall(r'"Name":"(.+?")', response.text)
        address=re.findall(r'"Address":"<i class=\\"add\\">(.+?)</i>', response.text)
        url = re.findall(r'"ImgUrl":"(.+?)"', response.text)
        lon = re.findall(r'"Lon":"(.+?)"', response.text)
        lat = re.findall(r'"Lat":"(.+?)"', response.text)
        grade = re.findall(r'"Grade":"(.+?)"', response.text)

        for i in range(len(id)):
            item = HangzhouhotelItem()
            item["Id"]=id[i]
            item["Name"]=name[i]
            item["Address"]=address[i]
            item["ImgUrl"]=url[i]
            item["Lon"]=lon[i]
            item["Lat"]=lat[i]
            item["Grade"] = grade[i]
            headers = {
                "Connection": "keep-alive",
                "Host": "www.ly.com",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cookie": "GnHotelData=%7B%22CnHotelComeDate%22%3A%222018-12-28%22%2C%22CnHotelLeaveDate%22%3A%222018-12-29%22%2C%22CnHotelCityName%22%3A%22%25E5%2598%2589%25E5%2585%25B4%22%2C%22CnHotelCityId%22%3A%22385%22%2C%22CnHotelParCityId%22%3A%220%22%2C%22Keyword%22%3A%22%22%2C%22KeywordId%22%3A%220%22%2C%22KeywordType%22%3A%220%22%2C%22Longitude%22%3A%22%22%2C%22Latitude%22%3A%22%22%7D; NewProvinceId=31; NCid=383; NewProvinceName=%E6%B5%99%E6%B1%9F; NCName=%E6%9D%AD%E5%B7%9E; Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1545811659,1545895077,1545957527; Hm_lpvt_64941895c0a12a3bdeb5b07863a52466=1545957527; 17uCNRefId=RefId=4140683&SEFrom=baidu&SEKeyWords=%E5%90%8C%E7%A8%8B; TicketSEInfo=RefId=4140683&SEFrom=baidu&SEKeyWords=%E5%90%8C%E7%A8%8B; CNSEInfo=RefId=4140683&tcbdkeyid=&SEFrom=baidu&SEKeyWords=%E5%90%8C%E7%A8%8B&RefUrl=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E5%2590%258C%25E7%25A8%258B%26rsv_spt%3D1%26rsv_iqid%3D0xdaf2948500031448%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_t%3D80bcsRaHGDo8ge%252B2WdlkJq1V3Igj4f0UWQmEMAmHblpIvM0870mlzgaLLT33m%252F5kVYGC%26rsv_sug2%3D0%26inputT%3D5864%26rsv_sug4%3D6408; __tctmu=144323752.0.0; __tctmz=144323752.1545957525307.8.1.utmccn=(organic)|utmcmd=organic|utmEsl=utf-8|utmcsr=baidu|utmctr=%e5%90%8c%e7%a8%8b; longKey=1545810753890123; __tctrack=0; ASP.NET_SessionId=g0hkr14igg52wal0wa2i4f0x; qdid=-9999; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1545815723,1545828100,1545895079,1545957529; Hm_lvt_f97c1b2277f4163d4974e7b5c8aa1e96=1545815723,1545828100,1545895079,1545957529; wangba=1545957529175; __tccgd=144323752.0; __tctmd=144323752.205661717; __tctma=144323752.1545810753890123.1545810753214.1545981390281.1545984051385.12; td_sid=MTU0NTk4NDA1Myw4N2JlOWU5NWRmYzRlMjFmNjU4NGRiNGUyYjhmNzM2ZDcxNGZiYzZlN2FmNmNhNzgyNDQyNjQ2ZmVkZTE2MjQ3LGUyZjRmZWUyYTYwN2Y1MzM5NjY4ZWYyMGFiOTBkOGEzMmZmNTcyOWJmZDE4MWU3MTFiY2EwZTJiOTUxZGRhMjM=; k_st=60.191.114.2|1545984053; td_did=MeW2ibCApPGyzxbzymlshlod%2FHgzSAIziJ6LFyKxXapp5lsry%2ByS5SYGJaogApIlP5eka5JdMU3lmZJ26VjOVVaoT5jCadhcLIutDOPkC2BEPXSUjs%2BZYbM%2BBsKdfYHcADTVNdJbQp7PjXlHqOMlc2982OkPmggZb9pt%2FEKkdrKYABm3jX%2BgpPy385JdoWLvXmUAikUY90ha8npGdk6O7w%3D%3D; t_q=1545984053127; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1545985573; __tctmc=144323752.98176409; __tctmb=144323752.3158266228496443.1545984051385.1545985573028.2; Hm_lpvt_f97c1b2277f4163d4974e7b5c8aa1e96=1545985573; route=c038dd5908962e8c5b7d772a7ac50921",
                "Referer": self.referer.format(reid=id[i]),
            }
            r=Request(self.Hotel_comment_url.format(Id=id[i], pageSize=10, page=1), headers=headers,meta={'id':id[i],'headers':headers},
                          callback=self.hotel_comment_parse)
            yield r
            yield item



    def hotel_comment_parse(self, response):
        result = json.loads(response.text)
        id=response.meta['id']
        headers=response.meta['headers']


        for key in result['response']['body']['dpList']:
            item = commentItem()
            for field in item.fields:
               item["hotelId"] = id
               item[field]=key.get(field)
            yield item

        totalPage=result['response']['body']['pageInfo'].get('totalPage')
        page=result['response']['body']['pageInfo'].get('page')

        if totalPage is not None and page is not None:
            if int(totalPage) > int(page):
                page=int(page)+1
                yield Request(self.Hotel_comment_url.format(Id=id, pageSize=10, page=str(page)), headers=headers,meta={'id':id,'headers':headers},
                              callback=self.hotel_comment_parse)












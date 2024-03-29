# -*- coding: utf-8 -*-
import json

import scrapy
from u17.items import U17Item


class YaoqiSpider(scrapy.Spider):
    name = 'yaoqi'
    allowed_domains = ['www.u17.com']
    start_urls = ['http://www.u17.com/comic_list/th99_gr99_ca99_ss99_ob0_ac0_as0_wm0_co99_ct99_p2.html?']

    def start_requests(self):
        url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
        data = {
            'data[group_id]': 'no',
            'data[theme_id]': 'no',
            'data[is_vip]': 'no',
            'data[accredit]': 'no',
            'data[color]': 'no',
            'data[comic_type]': 'no',
            'data[series_status]': 'no',
            'data[order]': '2',
            'data[page_num]': '1',
            'data[read_mode]': 'no',
        }

        headers = {
            'Referer': url,
            'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            'Host': 'www.u17.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        }
        for page in range(500):
            data['data[page_num]'] = '%d' % (page + 1)

            yield scrapy.FormRequest(
                url=url,
                headers=headers,
                method='POST',
                formdata=data,
                callback=self.parse,
            )

    def parse(self, response):
        json_result = json.loads(response.text)
        comic_list = json_result['comic_list']
        for comic in comic_list:
            item = U17Item()
            item['comic_id'] = comic['comic_id']
            item['name'] = comic['name']
            item['cover'] = comic['cover']
            item['category'] = comic['line2']
            yield item

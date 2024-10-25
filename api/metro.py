import requests
import json
from typing import Any
from json import JSONDecodeError

from .base import ParserBase


ADDRESSESS = [
    {
    'latitude': 55.755246,
    'longitude': 37.617779
    },
    {
    'latitude': 59.937797,
    'longitude': 30.315599
    },
]
HEADERS: dict[str, str] = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_slid_server=66266ecb9fe8242f1601fc10; active_order=0; tabbar=0; allowedCookieCategories=necessary%7Cfunctional%7Cperformance%7Cpromotional%7Cthirdparty%7CUncategorized; PLP_tags=2; bmpl_test=1; pickupStore=24; alcoclubStoreId=24; pdp_abc_20=3; plp_bmpl_bage=0; metro_api_session=qRDNw6wJxwpL5iWKknr05UVpQEDCAar695JQYvbs; metro_user_id=7bcf6308429a52df9ed283719824a96e; _slid=66266ecb9fe8242f1601fc10; _slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1729883479%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1729883479; _ym_uid=1729876279455349246; _ym_d=1729876279; tmr_lvid=749b46f961bd29f56e805e188ad713dc; tmr_lvidTS=1729876279463; _gcl_au=1.1.2004649351.1729876280; _ym_isad=2; uxs_uid=27307f60-92f4-11ef-8a52-132ef835f5f9; _fbp=fb.1.1729878413869.259555167604125992; _gid=GA1.2.890221717.1729878414; _ga=GA1.1.416731041.1729876280; mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A192c4a94047101f-0b402119d3b88e-26011951-1fa400-192c4a94047101f%22%2C%22%24device_id%22%3A%20%22192c4a94047101f-0b402119d3b88e-26011951-1fa400-192c4a94047101f%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; mp_88875cfb7a649ab6e6e310368f37a563_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A192c4a94087105f-0027254b4e3aa6-26011951-1fa400-192c4a94087105f%22%2C%22%24device_id%22%3A%20%22192c4a94087105f-0027254b4e3aa6-26011951-1fa400-192c4a94087105f%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; mindboxDeviceUUID=0fde093a-570a-4aa9-8207-951220657923; directCrm-session=%7B%22deviceGuid%22%3A%220fde093a-570a-4aa9-8207-951220657923%22%7D; metroStoreId=356; _ga_VHKD93V3FV=GS1.1.1729876279.1.1.1729880152.0.0.0',
    'origin': 'https://online.metro-cc.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://online.metro-cc.ru/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class Metro(ParserBase):
    base_url = 'https://online.metro-cc.ru'
    session = requests.Session()


    def loader(self):
        self.driver.get(f'{self.base_url}')
        self.driver.implicitly_wait(15)
        self.session.headers.update(HEADERS)
        browser_cookies = {cookie['name']: cookie['value'] for cookie in self.driver.get_cookies()}
        self.session.cookies.update(browser_cookies)
        for address in ADDRESSESS:
            # Get address cookies
            response = self.session.post(
                'https://api.metro-cc.ru/marketplace/v1/Logistics/order_types',
                json={
                    'delivery_coordinates': [
                        address
                    ],
                }
            )
            data = response.json()['addresses'][0]['delivery']['store']
            self.store_id = data['id']
            file_name = data['address']
            result = self._load_category()
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)

    def _load_category(self) -> list[dict[str, Any]]:
        result = []
        json_data = {
            'query': '\n  query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $priceLevelsOnline: Boolean) {\n    category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevelsOnline: $priceLevelsOnline) {\n      id\n      name\n      slug\n      id\n      parent_id\n      meta {\n        description\n        h1\n        title\n        keywords\n      }\n      disclaimer\n      description {\n        top\n        main\n        bottom\n      }\n      breadcrumbs {\n        category_type\n        id\n        name\n        parent_id\n        parent_slug\n        slug\n      }\n      promo_banners {\n        id\n        image\n        name\n        category_ids\n        type\n        sort_order\n        url\n        is_target_blank\n        analytics {\n          name\n          category\n          brand\n          type\n          start_date\n          end_date\n        }\n      }\n\n\n      dynamic_categories(from: 0, size: 9999) {\n        slug\n        name\n        id\n        category_type\n        dynamic_product_settings {\n          attribute_id\n          max_value\n          min_value\n          slugs\n          type\n        }\n      }\n      filters {\n        facets {\n          key\n          total\n          filter {\n            id\n            hru_filter_slug\n            is_hru_filter\n            is_filter\n            name\n            display_title\n            is_list\n            is_main\n            text_filter\n            is_range\n            category_id\n            category_name\n            values {\n              slug\n              text\n              total\n            }\n          }\n        }\n      }\n      total\n      prices {\n        max\n        min\n      }\n      pricesFiltered {\n        max\n        min\n      }\n      products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters)  {\n        health_warning\n        limited_sale_qty\n        id\n        slug\n        name\n        name_highlight\n        article\n        new_status\n        main_article\n        main_article_slug\n        is_target\n        category_id\n        category {\n          name\n        }\n        url\n        images\n        pick_up\n        rating\n        icons {\n          id\n          badge_bg_colors\n          rkn_icon\n          caption\n          type\n          is_only_for_sales\n          caption_settings {\n            colors\n            text\n          }\n          sort\n          image_svg\n          description\n          end_date\n          start_date\n          status\n        }\n        manufacturer {\n          name\n        }\n        packing {\n          size\n          type\n        }\n        stocks {\n          value\n          text\n          scale\n          eshop_availability\n          prices_per_unit {\n            old_price\n            offline {\n              price\n              old_price\n              type\n              offline_discount\n              offline_promo\n            }\n            price\n            is_promo\n            levels {\n              count\n              price\n            }\n            online_levels {\n              count\n              price\n              discount\n            }\n            discount\n          }\n          prices {\n            price\n            is_promo\n            old_price\n            offline {\n              old_price\n              price\n              type\n              offline_discount\n              offline_promo\n            }\n            levels {\n              count\n              price\n            }\n            online_levels {\n              count\n              price\n              discount\n            }\n            discount\n          }\n        }\n      }\n      argumentFilters {\n        eshopAvailability\n        inStock\n        isPromo\n        priceLevelsOnline\n      }\n    }\n  }\n',  # noqa E501
            'variables': {
                'isShouldFetchOnlyProducts': True,
                'slug': 'jogurty',
                'storeId': int(self.store_id),
                'sort': 'default',
                'size': 100,
                'from': 30,
                'filters': [
                    {
                        'field': 'main_article',
                        'value': '0',
                    },
                ],
                'attributes': [],
                'in_stock': False,
                'eshop_order': False,
            },
        }
        response = self.session.post('https://api.metro-cc.ru/products-api/graph', json=json_data)
        try:
            data = response.json()
        except JSONDecodeError as e:
            raise e('Could not load products')
        for product in data['data']['category']['products']:
            # Check if product available
            stocks = product['stocks'][0]
            if stocks['value'] == 0:
                continue
            if old_price := stocks['prices']['old_price']:
                price = old_price
                discount = stocks['prices']['price']
            else:
                discount = None
                price = stocks['prices']['price']

            result.append({
                'id': product['id'],
                'name': product['name'],
                'url': self.base_url + product['url'],
                'price': price,
                'price_dicsount': discount,
                'brand': product['manufacturer']['name']
            })
        return result
        


import json

from social.tests.backends.oauth import OAuth2Test


class WeixinOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.weixin.WeixinOAuth2'
    expected_username = 'NICKNAME'
    access_token_body = json.dumps({
        "access_token":"ACCESS_TOKEN",
        "expires_in":7200,
        "refresh_token":"REFRESH_TOKEN",
        "openid":"OPENID",
        "scope":"SCOPE"
    })
    user_data_body = json.dumps({
        "openid":"OPENID",
        "nickname":"NICKNAME",
        "sex":1,
        "province":"PROVINCE",
        "city":"CITY",
        "country":"COUNTRY",
        "headimgurl": "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
        "privilege":[ "PRIVILEGE1", "PRIVILEGE2" ],
        "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL",
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()

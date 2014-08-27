#coding:utf8
# author:hepochen@gmail.com  https://github.com/hepochen
"""
Weixin OAuth2 backend, docs at:
    http://psa.matiasaguirre.net/docs/backends/weibo.html
"""
from social.backends.oauth import BaseOAuth2


class WeixinOAuth2(BaseOAuth2):
    """Weixin (or Weixin) OAuth authentication backend"""
    name = 'weixin'
    ID_KEY = 'openid'
    USER_DATA_URL = 'https://api.weixin.qq.com/sns/auth'
    AUTHORIZATION_URL = 'https://open.weixin.qq.com/connect/qrconnect'
    ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    REFRESH_TOKEN_URL = 'https://api.weixin.qq.com/sns/oauth2/refresh_token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    DEFAULT_SCOPE = ['snsapi_login']
    EXTRA_DATA = [
        ('openid', 'id'),
        ('expires_in', 'expires'),
        ('nickname', 'username'),
        ('headimgurl', 'avatar_url'),
        ('sex', 'gender'),
        ('unionid', 'unionid'),
    ]

    def auth_params(self, *args, **kwargs):
        params = super(WeixinOAuth2, self).auth_params(*args, **kwargs)
        params['appid'] = params.pop('client_id')
        return params

    def auth_complete_params(self, *args, **kwargs):
        params = super(WeixinOAuth2, self).auth_complete_params(*args, **kwargs)
        params['appid'] = params.pop('client_id')
        params['secret'] = params.pop('client_secret')
        return params

    def refresh_token_params(self, token, *args, **kwargs):
        params = super(WeixinOAuth2, self).refresh_token_params(*args, **kwargs)
        params['appid'] = params.pop('client_id')
        params['secret'] = params.pop('client_secret')
        return params

    def get_user_details(self, response):
        username = response.get('nickname', '')
        fullname, first_name, last_name = self.get_user_names(
            first_name=username
        )
        return {'username': username,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

    def user_data(self, access_token, *args, **kwargs):
        params = {
                'access_token': access_token,
                'openid': kwargs['response']['openid'],
                }
        return self.get_json(self.USER_DATA_URL, params=params)

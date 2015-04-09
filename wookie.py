import oauth2 as oauth
import urlparse

FACEBOOK_APP_ID = '502502796557079'
FACEBOOK_SECRET = '48ef54a8c925e8cc9c209e1f8e47bbc2'

consumer = oauth.Consumer(FACEBOOK_APP_ID, FACEBOOK_SECRET)
client = oauth.Client(consumer)

request_token_url = 'https://www.facebook.com/dialog/oauth'

resp, content = client.request(request_token_url, "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

request_token = dict(urlparse.parse_qsl(content))

print resp
print content

print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

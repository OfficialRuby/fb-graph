import config
import facebook
page_id ="101545692359170"
link="https://docs.djangoproject.com/en/3.2/ref/applications/"
message='''
Application configuration objects store metadata for an application. Some attributes can be configured in AppConfig subclasses. Others are set by Django and read-only.
'''
graph = facebook.GraphAPI(config.access_token)
facebook_page_id = config.page_id
# graph.put_object(facebook_page_id, "feed", message=message, link=link)
print("Post published")

'''import facebook

access_token = 'EAAD4XughBqwBAFZBEpemH1pDNvdQi798x3yovULhvkozSGRiZAm11zMZA6tKvwMrkHWdVVVhVnw8bMT5jqKJcPbjnZB8iJNMDdOoMZCHwArZAn41EVX1tMYwps1l2B3fAAxP5z6XigFIfybqbbnO7KXWwCYOZCeb7ONHjBCAPGUcXBfUEQZB0LSO'

# Initialize the Graph API with your access token
graph = facebook.GraphAPI(access_token)
#message = "Hello there, you're doing great okay? keep going!"
# Post a message to your Facebook timeline
graph.put_object(parent_object='https://www.facebook.com/mariaam.ayman15', connection_name='feed', message = "Hello there, you're doing great okay? keep going!")
print('done')'''

import facebook
import requests
#Your Access Keys
page_id_1 = 100092271291518
facebook_access_token_1 = 'EAAJqhw69Nm0BANL04vUzZCwGxUxZAz9bZB9mLg2DqniYs2Qbc332HaHmBxWYgeuXozm3SMqxZAHquWvsEFZBJ7A39gSGBJeldsFWQnUvEUug3biFpBqZCWazXbup4SCwxFem1lortbv5Rhi2lLHpPE8OFgOOrXBE4jampEvZBZABfsmh80x2149e2dpeKZCtQ0P5Ft7KNvY2t3RwFMmZAk62CZB'
msg = 'Hello there, you are doing great okay? keep going!'
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
payload = { 'message': msg, 'access_token': facebook_access_token_1}
r = requests.post(post_url, data=payload)
print(r.text)
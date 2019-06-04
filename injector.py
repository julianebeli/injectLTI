import __init__
import config
from api.requestor2 import API
from context_ids import delete_context_id

cache_time = 60 * 60 * 24 * 5
api = API('beta', cache=cache_time)


def remover():
    remove_lti = []
    delete_method = 'delete_external_tool_accounts'
    method = 'list_external_tools_accounts'
    for context in delete_context_id:
        params = dict(methodname=method, account_id=context)
        api.add_method(**params)
        api.do()
        remove_lti.append(dict(methodname=delete_method, account_id=context,
                               external_tool_id=api.results[0]['id']))

    for entry in remove_lti:
        api.add_method(**entry)
        # api.do()


def installer():
    payload = dict(
        name=config.name,
        config_type="by_url",
        config_url=config.config_url,
        consumer_key=config.consumer_key,
        shared_secret=config.shared_secret,
        privacy_level="public"
    )
    print(payload)


if __name__ == '__main__':
    installer()

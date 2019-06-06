import json
import __init__
import config
from api.requestor2 import API
from context_ids import context_id
contexts = context_id[:5]
contexts = [31, ]

cache_time = 60 * 60 * 24 * 5
api = API('beta')


def remover():
    remove_lti = []
    delete_method = 'delete_external_tool_accounts'
    method = 'list_external_tools_accounts'
    for context in contexts:
        params = dict(methodname=method, account_id=context)
        api.add_method(**params)
        api.do()
        print(json.dumps(api.results, indent=4))
        if not api.response_error:
            for response in api.results:
                remove_lti.append(dict(methodname=delete_method, account_id=context,
                                       external_tool_id=response['id']))

    for entry in remove_lti:
        api.add_method(**entry)
        api.do()


def installer():
    LTI_settings = dict(
        name=config.name,
        config_type="by_url",
        config_url=config.config_url,
        consumer_key=config.consumer_key,
        shared_secret=config.shared_secret,
        privacy_level="public",
        methodname='create_external_tool_accounts'
    )
    for context in contexts:
        LTI_settings.update(dict(course_id=context))
        api.add_method(**LTI_settings)
        api.do()
        print(json.dumps(api.results, indent=4))


if __name__ == '__main__':
    remover()
    installer()

"""Shared test scaffolding: the service folder on the path and a reader's config in the environment."""
import json
import os
from pathlib import Path
import sys

SERVICE = Path(__file__).resolve().parent.parent / 'service'
sys.path.insert(0, str(SERVICE))

CONFIG = {
    'HUB_PHONE_CALLER_NAME': 'Sam Example',
    'HUB_PHONE_OWN_NUMBER': '+4917212345678',
    'HUB_PHONE_TIMEZONE': 'Europe/Berlin',
    'HUB_PHONE_AGENT_ID': 'agent_test',
    'HUB_PHONE_NUMBER_ID': 'phnum_test',
    'HUB_PHONE_DAILY_LIMIT': '5',
}
os.environ.update(CONFIG)
os.environ.pop('ELEVENLABS_API_KEY', None)


def example_order():
    return json.loads((Path(__file__).with_name('example-order.json')).read_text(encoding='utf-8'))

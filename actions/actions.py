import os
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
import matplotlib

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_relative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.now()
        hrs= (int(now.strftime("%H"))+5)%24
        min= (int(now.strftime("%M"))+30)%60
        offset=int(tracker.get_slot("number_of_hours"))
        final_time=hrs+offset
        time=final_time+":"+min
        print("Sure, I have scheduled a cleaning at "+time)
        dispatcher.utter_message(text="Sure, I have scheduled a cleaning at "+time)

        return []
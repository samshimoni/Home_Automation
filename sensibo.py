import requests
import json
import device


class SensiboClientAPI(device.Device):
    def __init__(self, api_key):
        self._api_key = api_key
        super(SensiboClientAPI, self).__init__("Sensibu")

    def is_alive(self):
        pass

    def _get(self, path, ** params):
        params['apiKey'] = self._api_key
        response = requests.get(self.cfg.sensibuUri + path, params=params)
        response.raise_for_status()
        return response.json()

    def _patch(self, path, data, ** params):
        params['apiKey'] = self._api_key
        response = requests.patch(self.cfg.sensibuUri + path, params=params, data=data)
        response.raise_for_status()
        return response.json()

    def devices(self):
        result = self._get("/users/me/pods", fields="id,room")
        return {x['room']['name']: x['id'] for x in result['result']}

    def pod_measurement(self, podUid):
        result = self._get("/pods/%s/measurements" % podUid)
        return result['result']

    def pod_ac_state(self, podUid):
        result = self._get("/pods/%s/acStates" % podUid, limit=1, fields="status,reason,acState")
        return result['result'][0]['acState']

    def pod_change_ac_state(self, podUid, currentAcState, propertyToChange, newValue):
        self._patch("/pods/%s/acStates/%s" % (podUid, propertyToChange),
                json.dumps({'currentAcState': currentAcState, 'newValue': newValue}))

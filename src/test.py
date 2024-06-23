import requests
import model



def test_model_positive():

    r = str(model.analyse("Вы милые люди")[0]['label'])
    assert r == 'neutral'


def test_model_negative():

    r = str(model.analyse("Вы твари")[0]['label'])
    assert r == 'toxic'

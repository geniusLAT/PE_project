import model


def test_model_negative():
    r = str(model.analyse("Вы тварь")[0]['label'])
    assert r == 'toxic'


def test_model_positive():
    r = str(model.analyse("Вы милые люди")[0]['label'])
    assert r == 'neutral'
    

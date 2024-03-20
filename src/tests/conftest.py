import requests
import ast
class TestAPI:
    def testa(self):
        res = requests.get('http://127.0.0.1:8000/modeles/')
        assert (ast.literal_eval(res.text)['Description'] == ["Unet", "UnetPlusPlus", "MAnet", "Linknet", "FPN", "PSPNet", "DeepLabV3", "DeepLabV3Plus", "PAN"])

    def testb(self):
        res = requests.post('http://127.0.0.1:8000/study/?User=1&FileName=1&Epochs=1&LR=0.1&ImgSize=224&BatchSize=32&Model=FPN&TestSize=0.1')
        assert (ast.literal_eval(res.text)['ModelName'] =="1-1")

    def testc(self):
        res = requests.get('http://127.0.0.1:8000/study/?ModelName=1-1')
        assert (ast.literal_eval(res.text)["train_loss"] == 1)
        assert (ast.literal_eval(res.text)["train_dice"] == 2)
        assert (ast.literal_eval(res.text)["val_loss"] == 3)
        assert (ast.literal_eval(res.text)["val_dice"] == 4)


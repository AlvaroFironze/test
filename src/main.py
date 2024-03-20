from fastapi import FastAPI,HTTPException
import datetime

app = FastAPI()
modeles = ["Unet", "UnetPlusPlus", "MAnet", "Linknet", "FPN", "PSPNet", "DeepLabV3", "DeepLabV3Plus", "PAN"]
model_counter = 1
training_threads={}
@app.get("/modeles/")
def get():
    global modeles
    return {"AnswerDate":datetime.datetime.now().isoformat(),"Description":modeles}
@app.post("/study/")
def post(User: str, FileName: str, Epochs:int,LR:float,ImgSize:int,BatchSize:int,Model:str,TestSize:float):
    if (Epochs<1 or LR<+0 or LR>1 or ImgSize<122 or ImgSize>1048 or BatchSize<1 or BatchSize <1 or BatchSize>100 or
            Model not in modeles or TestSize<=0 or TestSize>0.9):
        raise HTTPException(status_code=400, detail="Wrong parameters")
    global model_counter
    model_name = User+'-'+str(model_counter)
    model_counter += 1
    global training_threads
    training_threads[str(model_name)] = {'is_stop':False, 'epochs':Epochs}
    print(f"Training Model {model_name} started.")
    training_threads[model_name]['train_loss']=1
    training_threads[model_name]['train_dice'] =2
    training_threads[model_name]['val_loss']=3
    training_threads[model_name]['val_dice']=4
    return {"AnswerDate":datetime.datetime.now().isoformat(),"ModelName":model_name}
@app.get("/study/")
def get(ModelName:str):
    global training_threads
    if ModelName in training_threads:
        return {"AnswerDate": datetime.datetime.now().isoformat(), 'train_loss': training_threads[ModelName]['train_loss'],
                'train_dice': training_threads[ModelName]['train_dice'],'val_loss': training_threads[ModelName]['val_loss'],
                'val_dice': training_threads[ModelName]['val_dice']}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
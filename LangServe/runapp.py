from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from langserve import RemoteRunnable

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get('/form')
def form_post(request: Request):
    result = 'Provide your topic'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post('/form')
def form_post(request: Request, topic: str = Form(...)):
    joke_chain = RemoteRunnable("http://localhost:8000/chain/")
    result = joke_chain.invoke({"topic": topic})
    result = result.content.replace('\n\n',' ')

    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'topic': topic})


if __name__=='__main__':

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)

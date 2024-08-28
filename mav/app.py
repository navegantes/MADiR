from fastapi import FastAPI

app = FastAPI(
    title='MAV',
    description='',
    summary='Meu Acervo Virtual',
    root_path='/api/v1',
)


@app.get('/ola-mundo')
def read_root():
    return {'message': 'Olár Mundo!'}

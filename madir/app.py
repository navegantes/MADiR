from fastapi import FastAPI

app = FastAPI(
    title='MADiR',
    description='',
    summary='Meu Acervo Digital de Romances',
    root_path='/api/v1',
)


@app.get('/ola-mundo')
def read_root():
    return {'message': 'Olár Mundo!'}

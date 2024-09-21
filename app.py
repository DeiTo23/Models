from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div(children=[

    html.Div(className='header',children=[
        html.Img(className="chuzados", src='assets/chuzados.jpeg'),
        html.H1('TEAM PITOCHICO', className='main_title')
    ]),

    html.Div(className='contenedor_navegacion', children=[
        dcc.Link(html.Button('Enrique', className='boton edo_1'), href='/'),
        dcc.Link(html.Button('Mono', className='boton edo_2'), href='Edo2doOrden')
     ]),

    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)


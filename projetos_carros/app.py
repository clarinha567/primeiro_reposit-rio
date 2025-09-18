import streamlit as st 
### Coloca um titulo
# st.title("imune ao conhecimento")

# ### Escreve
# st.write("testando... esquerda e direita ")

# ### Cria uma barra lateral 
# st.sidebar.title("barra lateral")

# ### Criando uma lista 
# # nomes ficticios, qualquer semelhança é  coincidencia 

# nomes = ["julia" , "lara" , "alice" , "paula"]


# ### Cria a caixinha na barra lateral
# st.sidebar._selectbox("escolha um nome:" , nomes)

# ### Coloca o video na pagina do site
# st.video ("https://www.youtube.com/shorts/Dcj7im5lmlA")


st.sidebar.image("logo.pngg")
st.sidebar.title("Grand Lux Cars")

carros = ["Rolls-Royce" , "lamborghini" , "Mercedes-Benz" , "Range Rover Evoque" , "Audi Q3"]
opção = st.sidebar.selectbox('escolha seu próximo carro' , carros )


#Principal
st.title('Grand Lux Cars✨ Aqui o futuro da sua direção ganha forma')
st.image(f'{opção}.png')
st.markdown(f'## Voce escolheu o modelo: {opção}')
st.markdown('---')


dias = st.text_input(f'Por quantos dias o {opção} foi alugado?')
km = st.text_input(f'quantos km vc rodou com o {opção}?')


### Defina a Diária 
if opção == 'Rolls-Royce':
    diaria = 550

elif opção == 'lamborghini':
    diaria = 500   

elif opção == 'Mercedes-Benz':
    diaria = 600

elif opção == 'Range Rover Evoque':
    diaria = 620

elif opção == 'audi Q3':
    diaria = 680

### calcular 

if st.button('calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria 
    total_km = km * 0.15
    aluguel_total = total_dias * total_km

    st.warning(f'vc alugou a {opção} por {dias} e rodou {km}km. o valor total a pagar é R${aluguel_total:.2F}')
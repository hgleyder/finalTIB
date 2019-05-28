import React from 'react';
import './App.css';
import { Box, Button, TextInput, Grommet } from 'grommet';
import styled from 'styled-components';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import ProteinService from './service/backend'
import Logo from './assets/logo.png'
import BackgroundImage from './assets/bg.jpg'


const theme = {
  global: {
    font: {
      family: 'Roboto',
      size: '14px',
      height: '20px',
    },
  },
};

class App extends React.Component {
  state= {
    protein: '',
    results: '',
    showResults: false,
    loading: false,
  }

  clasificarProteina = async () => {
    const {protein} = this.state;
    this.setState({loading: true})
    const results = await ProteinService.clasificaProteina(protein);
    this.setState({ results: results.data, showResults: true, loading: false });
  }


renderLineChart =  () => {
  const  {results } = this.state;
  const data = results.probabilidades[0].map((p, index) => ({probabilidad: p, name: results.clases[index]}))
  return (
  <LineChart width={1400} height={500} data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
    <Line type="monotone" dataKey="probabilidad" stroke="#8884d8" />
    <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
    <XAxis dataKey="name" />
    <YAxis />
    <Tooltip />
  </LineChart>
)};
  render(){
    const {protein, showResults, loading} = this.state;
  return (
    <Grommet theme={theme}>
      <Background>
      <Box align="center" height="100vh">
        <Container>
        <img src={Logo} className="logo" alt="logo" />
          <TextInput
            placeholder="Escribe aqui la secuencia de aminoacidos"
            value={protein}
            onChange={event => this.setState({protein: event.target.value})}
          />
          <Button
            label={loading? "Cargando..." : "Clasificar Proteina"}
            primary 
            disabled={loading}
            onClick={this.clasificarProteina}
          />
          {showResults && this.renderLineChart()}
        </Container>
      </Box>
      </Background>
     </Grommet>
  );
  }
}

const Background = styled.div`
  background-image: url(${BackgroundImage});
`;

const Container = styled.div`
  display: flex;
  flex: 1;
  width: 80%;
  margin-top: 5rem;
  flex-direction: column;

  & > button {
    position: relative;
    top: 1rem;  
    width: 15rem;
  }

  & > .recharts-wrapper {
    margin-top: 2rem;
    margin-left: -3rem;
  }
  & > .logo{
    width: 40%;
    margin-top: -8rem;
  }
`;

export default App;

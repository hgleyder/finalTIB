import React from 'react';
import './App.css';
import { Box, Button, TextInput, Chart, Grommet } from 'grommet';
import styled from 'styled-components';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import ProteinService from './service/backend'


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
  }

  clasificarProteina = async () => {
    const {protein} = this.state;
    const results = await ProteinService.clasificaProteina(protein);
    console.log(results.data)
    this.setState({ results: results.data, showResults: true });
  }


renderLineChart =  () => {
  const  {results } = this.state;
  const data = results.probabilidades[0].map((p, index) => ({probabilidad: p, name: results.clases[index]}))
  return (
  <LineChart width={1400} height={600} data={data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
    <Line type="monotone" dataKey="probabilidad" stroke="#8884d8" />
    <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
    <XAxis dataKey="name" />
    <YAxis />
    <Tooltip />
  </LineChart>
)};
  render(){
    const {protein, showResults,} = this.state;
  return (
    <Grommet theme={theme}>
      <Box align="center" height="100vh">
        <Container>
          <TextInput
            placeholder="Escribe aqui la secuencia de aminoacidos"
            value={protein}
            onChange={event => this.setState({protein: event.target.value})}
          />
          <Button
            label="Clasificar Proteina"
            primary 
            onClick={this.clasificarProteina}
          />
          {showResults && this.renderLineChart()}
        </Container>
      </Box>
     </Grommet>
  );
  }
}

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
  }
`;

export default App;

import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Box, Button, TextInput, Grommet } from 'grommet';
import styled from 'styled-components';

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
  }
  render(){
    const {protein} = this.state;
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
            onClick={() => alert('hello, world')}
          />
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
`;

export default App;

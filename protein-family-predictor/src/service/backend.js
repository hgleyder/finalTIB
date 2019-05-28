import api from './api';

let proteinas = {};

proteinas.clasificaProteina = (sequence) =>
	api.post('/clasifica', { data: { sequence } });

export default proteinas;

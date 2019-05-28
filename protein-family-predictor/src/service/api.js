import axios from 'axios';

const api = axios.create({
	baseURL: 'http://localhost:5000/',
	timeout: 180000,
	headers: {
		Accept: 'application/json',
		'Content-Type': 'application/json',
	},
});

export default api;
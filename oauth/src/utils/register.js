const axios = require('axios');

const registerLocal = async (data) => {
    try {
        const response = await axios.post(`${process.env.BACKEND}`, data);
        return response.data;
    } catch (error) {
        throw new Error('Failed to register user');
    }
}
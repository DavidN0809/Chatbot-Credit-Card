// frontend/src/api.js

import axios from 'axios';

// Function to send prompt to backend and receive response
export const getLlamaResponse = async (text) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/generate", { text });
        return response.data.response;
    } catch (error) {
        console.error("Error fetching response:", error);
        return "An error occurred while generating the response.";
    }
};

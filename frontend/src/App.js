// frontend/src/App.js

import React, { useState } from 'react';
import { getLlamaResponse } from './api';

function App() {
    const [input, setInput] = useState("");
    const [output, setOutput] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await getLlamaResponse(input);
        setOutput(response);
    };

    return (
        <div className="App">
            <h1>Llama 3 Chatbot</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    rows="4"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Enter your prompt here"
                />
                <button type="submit">Generate</button>
            </form>
            <div>
                <h2>Response:</h2>
                <p>{output}</p>
            </div>
        </div>
    );
}

export default App;

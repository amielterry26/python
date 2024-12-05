const express = require('express');
const { spawn } = require('child_process');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static('public')); // For serving frontend files

// Routes
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

// Endpoint to calculate budget
app.post('/calculate', (req, res) => {
    const { income, expenses } = req.body;

    if (typeof income !== 'number' || !Array.isArray(expenses)) {
        return res.status(400).json({ error: 'Invalid input' });
    }

    // Call the Python script
    const pythonProcess = spawn('python3', ['path/to/your_script.py', JSON.stringify(req.body)]);

    let pythonOutput = '';

    pythonProcess.stdout.on('data', (data) => {
        pythonOutput += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            try {
                const result = JSON.parse(pythonOutput);
                res.json(result);
            } catch (error) {
                res.status(500).json({ error: 'Invalid response from Python script' });
            }
        } else {
            res.status(500).json({ error: 'Python script execution failed' });
        }
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

const express = require('express');
const { spawn } = require('child_process');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static('public')); // For serving frontend files

// Serve static files from the frontEnd folder
console.log()
app.use(express.static(path.join(__dirname, 'src/frontEnd')));

// Route for the homepage
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'src/frontEnd/index.html'));
});

app.post('/calculate', (req, res) => {
    const input = JSON.stringify(req.body);

    const pythonProcess = spawn('python3', ['PythonBudgetApp/src/backEnd/python/budgetCalculator.py', input]);

    let output = '';

    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
    });

    pythonProcess.stderr.on('data', (err) => {
        console.error(`Error: ${err}`);
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            try {
                res.json(JSON.parse(output));
            } catch (error) {
                res.status(500).send({ error: 'Invalid Python output' });
            }
        } else {
            res.status(500).send({ error: 'Python script execution failed' });
        }
    });
});


// Start server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
